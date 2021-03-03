# change the URLs in `./repos.yml`
import os
import pathlib
import doit.tools
import json
import shutil
import sys
import subprocess
from yaml import safe_load

DOIT_CONFIG = {
    "backend": "sqlite3",
    "verbosity": 2,
    "par_type": "thread",
}

os.environ.update(
    NODE_OPTS="--max-old-space-size=4096",
    PIP_DISABLE_PIP_VERSION_CHECK="1",
    PIP_IGNORE_INSTALLED="1",
    PIP_NO_BUILD_ISOLATION="1",
    PIP_NO_DEPENDENCIES="1",
    PYTHONIOENCODING="utf-8",
    PYTHONUNBUFFERED="1",
)

HERE = pathlib.Path(__file__).parent

# don't pollute the global state
LINKS = (HERE / "repos/.yarn-links").resolve()
YARN = ["yarn", "--link-folder", LINKS]
PIP = ["python", "-m", "pip"]

APP_DIR = pathlib.Path(sys.prefix) / "share/jupyter/lab"
APP_STATIC = APP_DIR / "static"
APP_INDEX = APP_STATIC / "index.html"


REPOS_YML = HERE / "repos.yml"
REPOS = safe_load(REPOS_YML.read_text())["repos"]
PATHS = {name: HERE / "repos" / name for name in REPOS}


def task_lint():
    all_py = [*HERE.glob("*.py")]
    yield dict(name="py", file_dep=[*all_py], actions=[do("black", *all_py)])


# add targets to the docstring to include in the dev build.
def task_clone():
    """clone all the repos defined in the doc string"""
    for name, spec in REPOS.items():
        path = PATHS[name]
        config = path / ".git/config"
        head = path / ".git/HEAD"

        uptodate = doit.tools.config_changed({name: spec})

        yield dict(
            name=f"init:{name}",
            file_dep=[REPOS_YML],
            actions=[]
            if path.exists()
            else [
                (doit.tools.create_folder, [path]),
                do("git", "init", cwd=path),
                do("git", "remote", "add", "origin", spec["origin"], cwd=path),
            ],
            targets=[config],
        )

        for i, ref in enumerate(spec["refs"]):
            task_dep = []
            actions = [do("git", "fetch", "origin", ref["ref"], cwd=path)]
            if i:
                task_dep += [f"""clone:fetch:{name}:{i-1}:{ref["refs"][i - 1]}"""]
                actions += [do("git", "merge", f"""origin/{ref["commit"]}""")]
            else:
                actions += [do("git", "checkout", "-f", ref["commit"], cwd=path)]

            yield dict(
                name=f"""fetch:{name}:{i}:{ref["ref"]}:{ref["commit"]}""",
                file_dep=[config],
                targets=[head],
                task_dep=task_dep,
                actions=actions,
            )


def task_setup():
    """ensure a working build of live development builds"""
    for path in PATHS.values():
        head = path / ".git/HEAD"
        pkg_json = path / "package.json"

        if pkg_json.exists():
            yield dict(
                name=f"yarn:install:{path.name}",
                file_dep=[pkg_json, head],
                actions=[do(*YARN, cwd=path)],
                targets=yarn_integrity(path),
            )

        setup_py = path / "setup.py"

        if setup_py.exists():
            py_deps = [head, setup_py] + (
                yarn_integrity(path) if pkg_json.exists() else []
            )
            yield dict(
                name=f"pip:install:{path.name}",
                file_dep=py_deps,
                actions=[
                    do(*PIP, "uninstall", "-y", path.name, cwd=path),
                    do(*PIP, "install", "-e", ".", cwd=path),
                    do(*PIP, "check"),
                ],
            )
            if path == REPOS.get("jupyterlab"):
                yield dict(
                    name=f"server:{path.name}",
                    file_dep=py_deps,
                    task_dep=[f"setup:pip:install:{path.name}"],
                    actions=server_extensions(path),
                )

        if pkg_json.exists():
            yield dict(
                name=f"yarn:build:{path.name}",
                file_dep=yarn_integrity(path),
                actions=[do(*YARN, "build", cwd=path)],
                targets=list(path.glob("packages/*/lib/*.js")),
                **(
                    dict(task_dep=[f"setup:pip:install:{path.name}"])
                    if setup_py.exists()
                    else {}
                ),
            )


def task_link():
    """link yarn packages across the repos"""
    # go to the direction and links the packages.
    lumino = PATHS.get("lumino")
    lab = PATHS.get("jupyterlab")

    if not (lumino and lab):
        return

    for pkg_json in lumino.glob("packages/*/package.json"):
        pkg = pkg_json.parent
        pkg_data = json.loads(pkg_json.read_text(encoding="utf-8"))
        pkg_name = pkg_data["name"]
        out_link = LINKS / pkg_data["name"] / "package.json"
        in_link = lab / f"node_modules/{pkg_name}/package.json"
        yield dict(
            name=pkg_name,
            file_dep=[*yarn_integrity(lumino), *yarn_integrity(lab), pkg_json],
            actions=[(doit.tools.create_folder, [LINKS]), do(*YARN, "link", cwd=pkg)],
            targets=[out_link],
        )

        yield dict(
            name=f"lab:{pkg_name}",
            uptodate=[
                doit.tools.config_changed(
                    {
                        pkg_name: (
                            in_link.exists() and in_link.resolve() == pkg_json.resolve()
                        )
                    }
                )
            ],
            file_dep=[out_link],
            actions=[do(*YARN, "link", pkg_name, cwd=lab)],
        )


def task_app():
    lab = PATHS.get("jupyterlab")

    if not lab:
        return

    dev_mode = lab / "dev_mode"
    dev_static = dev_mode / "static"
    dev_index = dev_static / "index.html"

    yield dict(
        name="build",
        file_dep=[
            *LINKS.glob("*/package.json"),
            *LINKS.glob("*/*/package.json"),
            *sum(
                [[*repo.glob("packages/*/lib/*.js")] for repo in PATHS.values()],
                [],
            ),
        ],
        actions=[do(*YARN, "build", cwd=dev_mode)],
        targets=[dev_index],
    )

    yield dict(
        name="deploy",
        file_dep=[dev_index],
        actions=[
            lambda: [shutil.rmtree(APP_DIR, ignore_errors=True), None][-1],
            (doit.tools.create_folder, [APP_DIR]),
            lambda: [
                shutil.copytree(dev_mode / subdir, APP_DIR / subdir)
                for subdir in ["static", "schemas", "templates", "themes"]
            ]
            and None,
        ],
        targets=[APP_INDEX],
    )


def task_start():
    if os.environ.get("NOT_ON_BINDER") is None:
        print("set the environment variable NOT_ON_BINDER to start")
        return

    if "jupyterlab" in REPOS:
        yield dict(
            name="lab",
            uptodate=[lambda: False],
            file_dep=[APP_INDEX],
            actions=[run_lab()],
        )


# utilities


def do(*args, cwd=HERE, **kwargs):
    """wrap a CmdAction for consistency"""
    return doit.tools.CmdAction(list(args), shell=False, cwd=str(pathlib.Path(cwd)))


def yarn_integrity(repo):
    """the file created after yarn install"""
    return [repo / "node_modules/.yarn-integrity"]


def server_extensions(repo):
    enable = ["enable", "--py", repo.name, "--sys-prefix"]
    apps = ["serverextension"], ["server", "extension"]
    return sum(
        [[do("jupyter", *app, *enable), do("jupyter", *app, "list")] for app in apps],
        [],
    )


def run_lab():
    def lab():
        args = ["jupyter", "lab", "--debug", "--no-browser"]
        proc = subprocess.Popen(args, stdin=subprocess.PIPE)

        try:
            proc.wait()
        except KeyboardInterrupt:
            proc.terminate()
            proc.communicate(b"y\n")

        proc.wait()
        return True

    return doit.tools.PythonInteractiveAction(lab)
