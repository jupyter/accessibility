#!/usr/bin/env doit -f
"""https://github.com/jupyterlab/jupyterlab@408f30f
https://github.com/jupyterlab/lumino@09aec10
"""
# change the urls above to link different jupyter references.


import os
import pathlib
import doit.tools
import json

DOIT_CONFIG = {
    "backend": "sqlite3",
    "verbosity": 2,
    "par_type": "thread",
}

os.environ.update(
    PYTHONUNBUFFERED="1",
    PYTHONIOENCODING="utf-8",
    PIP_NO_DEPS="1",
    PIP_NO_BUILD_ISOLATION="1",
    PIP_DISABLE_PIP_VERSION_CHECK="1",
    PIP_IGNORE_INSTALLED="1"
)

HERE = pathlib.Path(__file__).parent

# don't pollute the global state
LINKS = (HERE / ".yarn-links").resolve()
YARN = ["yarn", "--link-folder", LINKS]
PIP = ["python", "-m", "pip"]

URLS = list(filter(bool, __doc__.splitlines()))


def task_lint():
    all_py = HERE.glob("*.py")
    yield dict(
        name="py",
        file_dep=[*all_py],
        actions=[["black", "--quiet", *all_py]]
    )


# add targets to the docstring to include in the dev build.
def task_clone():
    """clone all the repos defined in the doc string"""
    for url in URLS:
        path = url_to_path(url)
        yield dict(
            name=path.name,
            actions=[] if path.exists() else [do("git", "clone", "--depth=1", url)],
            targets=[path / "package.json"]
        )


def task_setup():
    """ensure a working build of live development builds"""
    for repo in map(url_to_path, URLS):
        yield dict(
            name=f"{repo.name}:yarn",
            file_dep=[repo / "package.json"],
            actions=[do(*YARN, cwd=repo)],
            targets=yarn_integrity(repo)
        )

        setup_py = repo / "setup.py"

        if setup_py.exists():
            yield dict(
                name=f"{repo.name}:pip",
                file_dep=yarn_integrity(repo),
                actions=[
                    do(*PIP, "uninstall", "-y", repo.name, cwd=repo),
                    do(*PIP, "install", "-e", ".", cwd=repo),
                    do(*PIP, "check")
                ]
            )

        yield dict(
            name=f"{repo.name}:build",
            file_dep=yarn_integrity(repo),
            actions=[
                do(*YARN, "build", cwd=repo)
            ],
            targets=list(repo.glob("packages/*/lib/*.js")),
            **(
                dict(task_dep=[f"setup:{repo.name}:pip"]) if setup_py.exists() else {}
            )
        )


def task_link():
    """link yarn packages across the repos"""
    # go to the direction and links the packages.
    lumino = [url_to_path(u) for u in URLS if "jupyterlab/lumino" in u][0]
    lab = [url_to_path(u) for u in URLS if "jupyterlab/jupyterlab" in u][0]

    for pkg_json in lumino.glob("packages/*/package.json"):
        pkg = pkg_json.parent
        pkg_data = json.loads(pkg_json.read_text(encoding="utf-8"))
        pkg_name = pkg_data["name"]
        out_link = LINKS / pkg_data["name"] / "package.json"
        in_link = lab / f"node_modules/{pkg_name}/package.json"
        yield dict(
            name=pkg_name,
            file_dep=[*yarn_integrity(lumino), *yarn_integrity(lab), pkg_json],
            actions=[
                (doit.tools.create_folder, [LINKS]),
                do(*YARN, "link", cwd=pkg)
            ],
            targets=[out_link]
        )

        yield dict(
            name=f"lab:{pkg_name}",
            uptodate=[doit.tools.config_changed({
                pkg_name: (
                    in_link.exists() and in_link.resolve() == pkg_json.resolve()
                )
            })],
            file_dep=[out_link],
            actions=[do(*YARN, "link", pkg_name, cwd=lab)]
        )

def task_config():
    """merge config"""
    # hoist the configurations from the existing repos like jupyterlab.
    # we'll use their start to begin with.
    return dict(actions="""cp jupyterlab/binder/start .
        cp jupyterlab/binder/jupyter_notebook_config.py .""".splitlines())

# def task_postBuild():
#     """recursively invoke all postBuilds"""
#     for repo in repos:
#         for postBuild in [*repo.rglob("postBuild")]:
#             yield dict(
#                 name=repo + str(postBuild),
#                 file_dep=[postBuild],
#                 actions=[
#                     doit.CmdAction([], shell=False, cwd=postBuild.parent)
#                 ]
#             )

# utilities

def url_to_path(x):
    """extract the local checkout name"""
    return pathlib.Path(x.rpartition("@")[0].rpartition("/")[2])

def do(*args, cwd=HERE, **kwargs):
    """wrap a CmdAction for consistency"""
    return doit.tools.CmdAction(list(args), shell=False, cwd=str(pathlib.Path(cwd)))

def yarn_integrity(repo):
    """the file created after yarn install"""
    return [repo / "node_modules/.yarn-integrity"]
