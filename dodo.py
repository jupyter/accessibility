"""doit for interactive testing of accessibility in Jupyter
"""
import os
import pathlib
import doit.tools
import json
import shutil
import time
import sys
import random
import hashlib
import http.cookiejar
import urllib.request
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
CI = HERE / ".github"
PA11Y = HERE / "pa11y"
REPORTS = HERE / "reports"


# don't pollute the global state
LINKS = (HERE / "repos/.yarn-links").resolve()
YARN = ["yarn", "--link-folder", LINKS]
PIP = ["python", "-m", "pip"]

LAB_APP_DIR = pathlib.Path(sys.prefix) / "share/jupyter/lab"
LAB_APP_STATIC = LAB_APP_DIR / "static"
LAB_APP_INDEX = LAB_APP_STATIC / "index.html"

REPOS_YML = HERE / "repos.yml"
REPOS = safe_load(REPOS_YML.read_text())["repos"]
PATHS = {name: HERE / "repos" / name for name in REPOS}
HOST = "127.0.0.1"
PORT = 8080
LAB_PORT = 9999


MISSING_LUMINO_DOCS = [
    "default-theme",
    # TODO: https://github.com/jupyterlab/lumino/issues/154
    "polling",
]


def task_lint():
    """lint the source in _this_ repo"""
    all_py = [*HERE.glob("*.py"), *PA11Y.glob("*.py")]
    yield dict(
        name="py",
        doc="apply python source formatting and basic checking",
        file_dep=[*all_py],
        actions=[do("black", *all_py), do("flake8", "--max-line-length=88", *all_py)],
    )

    all_prettier = [
        *HERE.glob("*.yml"),
        *PA11Y.glob("*.json"),
        *PA11Y.glob("*.md"),
        *CI.rglob("*.yml"),
    ]

    # += [HERE.glob("*.md")]

    yield dict(
        name="prettier",
        doc="apply prettier source formatting",
        actions=[
            do(
                *YARN,
                "prettier",
                "--write",
                "--list-different",
                *all_prettier,
                cwd=PA11Y,
            )
        ],
        file_dep=[*all_prettier],
    )


def task_clone():
    """clone all the repos defined in `repos.yml`"""
    for name, spec in REPOS.items():
        path = PATHS[name]
        config = path / ".git/config"
        head = path / ".git/HEAD"

        yield dict(
            name=f"{name}:init",
            file_dep=[REPOS_YML],
            actions=[]
            if path.exists()
            else [
                (doit.tools.create_folder, [path]),
                do("git", "init", "-b", "work", cwd=path),
                do("git", "remote", "add", "origin", spec["origin"], cwd=path),
                do("git", "config", "user.email", "a11y@jupyter.org", cwd=path),
                do("git", "config", "user.name", "Jupyter Accessibility", cwd=path),
                do("git", "config", "advice.detachedHead", "false", cwd=path),
            ],
            targets=[config],
        )

        refs = spec["refs"]
        for i, ref in enumerate(refs):
            task_dep = []
            actions = [do("git", "fetch", "origin", ref["ref"], cwd=path)]
            commit = ref.get("commit") or ref["ref"]
            targets = []
            if i == 0:
                actions += [do("git", "checkout", "-f", commit, cwd=path)]
            else:
                prev = refs[i - 1]
                task_dep += [f"""clone:{name}:fetch:{i-1}:{prev["ref"]}"""]
                actions += [do("git", "merge", "--commit", commit, cwd=path)]

            if i == len(refs) - 1:
                targets = [head]

            yield dict(
                name=f"""{name}:fetch:{i}:{ref["ref"]}""",
                file_dep=[config],
                targets=targets,
                task_dep=task_dep,
                actions=actions,
            )


def task_setup():
    """ensure a working build of repos"""

    yield dict(
        name=f"{PA11Y.name}:yarn:install",
        file_dep=[PA11Y / "package.json"],
        actions=[do(*YARN, cwd=PA11Y)],
        targets=[*yarn_integrity(PA11Y)],
    )

    for name, path in PATHS.items():
        head = path / ".git/HEAD"
        pkg_json = path / "package.json"

        if pkg_json.exists():
            yield dict(
                name=f"{name}:yarn:install",
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
                name=f"{name}:pip:install",
                file_dep=py_deps,
                actions=[
                    do(*PIP, "uninstall", "-y", path.name, cwd=path),
                    do(*PIP, "install", "-e", ".", cwd=path),
                    do(*PIP, "check"),
                ],
            )
            if path == PATHS.get("jupyterlab"):
                yield dict(
                    name=f"server:{path.name}",
                    file_dep=py_deps,
                    task_dep=[f"setup:{name}:pip:install"],
                    actions=enable_server_extensions(path),
                )

        if pkg_json.exists():
            yield dict(
                name=f"{name}:yarn:build",
                file_dep=yarn_integrity(path),
                actions=[do(*YARN, "build", cwd=path)],
                targets=list(path.glob("packages/*/lib/*.js")),
                **(
                    dict(task_dep=[f"setup:{name}:pip:install"])
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
    """rebuild apps with live modifications"""
    lab = PATHS.get("jupyterlab")

    if lab:
        dev_mode = lab / "dev_mode"
        dev_static = dev_mode / "static"
        dev_index = dev_static / "index.html"

        yield dict(
            name="build",
            doc="do a dev build of the current jupyterlab source",
            file_dep=[
                *LINKS.glob("*/package.json"),
                *LINKS.glob("*/*/package.json"),
                *sum(
                    [[*repo.glob("packages/*/lib/*.js")] for repo in PATHS.values()],
                    [],
                ),
            ],
            actions=[
                do(*YARN, "clean", cwd=dev_mode),
                do(*YARN, "build:prod", cwd=dev_mode),
            ],
            targets=[dev_index],
        )

        yield dict(
            name="deploy",
            doc="deploy the build dev application to $PREFIX/share/jupyter/lab",
            file_dep=[dev_index],
            actions=[
                lambda: [shutil.rmtree(LAB_APP_DIR, ignore_errors=True), None][-1],
                (doit.tools.create_folder, [LAB_APP_DIR]),
                lambda: [
                    shutil.copytree(dev_mode / subdir, LAB_APP_DIR / subdir)
                    for subdir in ["static", "schemas", "templates", "themes"]
                ]
                and None,
            ],
            targets=[LAB_APP_INDEX],
        )


def task_docs():
    """build documentation"""
    for path in PATHS.values():
        if not path.exists():
            continue

        if path == PATHS.get("jupyterlab"):
            tsdoc_index = path / "docs/api/index.html"
            yield dict(
                name="""jupyterlab:html:typedoc""",
                doc="build JupyterLab TypeScript API docs",
                file_dep=[*path.rglob("src/**/*.ts"), path / "package.json"],
                actions=[do(*YARN, "docs", cwd=path)],
                targets=[tsdoc_index],
            )

            lab_docs = path / "docs"
            lab_docs_src = lab_docs / "source"
            yield dict(
                name="jupyterlab:html:sphinx",
                doc="build JupyterLab docs",
                file_dep=[
                    tsdoc_index,
                    *lab_docs_src.rglob("*.rst"),
                    *lab_docs_src.rglob("*.css"),
                    *lab_docs_src.rglob("*.js"),
                ],
                actions=[
                    do(
                        "sphinx-build",
                        "-b",
                        "html",
                        "source",
                        "build/html",
                        cwd=path / "docs",
                    ),
                ],
                targets=[
                    path / "docs/build/html/.buildinfo",
                    path / "docs/build/html/index.html",
                ],
            )

        if path == PATHS.get("lumino"):
            lm_pkgs = sorted([p.parent for p in path.glob("packages/*/package.json")])
            lm_docs = [
                path / f"docs/api/{p.name}/index.html"
                for p in lm_pkgs
                if p.name not in MISSING_LUMINO_DOCS
            ]
            lm_index = path / "docs/api/index.html"
            yield dict(
                name="""lumino:html:typedoc""",
                doc="build Lumino TypeScript API docs",
                file_dep=[*path.rglob("packages/*/src/**/*.ts"), path / "package.json"],
                targets=lm_docs,
                actions=[do(*YARN, "docs", cwd=path)],
            )

            lm_index_text = "\n".join(
                [
                    """
                    <!doctype html>
                    <html>
                    <head><title>Lumino API Documentation</title></head>
                    <body><h1>Lumino API Documentation</h1><ul>
                    """,
                    *[
                        f"""
                        <li>
                        <a href="./{p.name}/index.html">{p.name.title()}</a>
                        </li>
                        """
                        for p in lm_pkgs
                        if p.name not in MISSING_LUMINO_DOCS
                    ],
                    """</ul></body></html>""",
                ]
            )

            yield dict(
                name="""lumino:html:index""",
                doc="build lumino docs index",
                file_dep=[*lm_docs],
                actions=[lambda: [lm_index.write_text(lm_index_text), None][-1]],
                targets=[lm_index],
            )


def task_report():
    path = PATHS.get("jupyterlab")

    if path:
        for task in yield_pa11y_static_tasks(path.name, path / "docs/build/html"):
            yield task

        lab_app_reports = REPORTS / "jupyterlab/app"
        lab_app_report_json = lab_app_reports / "pa11y-ci-jupyterlab-app.json"
        lab_app_report_html = lab_app_reports / "index.html"

        yield dict(
            name="jupyterlab:app:pa11y-ci:json",
            file_dep=[LAB_APP_INDEX],
            actions=[
                (doit.tools.create_folder, [lab_app_reports]),
                (run_pa11y_jupyterlab, [lab_app_report_json]),
            ],
            targets=[lab_app_report_json],
        )

        yield dict(
            name="jupyterlab:app:pa11y-ci:html",
            file_dep=[lab_app_report_json],
            actions=[
                (doit.tools.create_folder, [lab_app_report_html.parent]),
                (run_pa11y_html, [lab_app_report_json, lab_app_report_html.parent]),
            ],
            targets=[lab_app_report_html],
        )

    path = PATHS.get("lumino")

    if path is not None:
        for task in yield_pa11y_static_tasks(path.name, path / "docs"):
            yield task
        for task in yield_pa11y_static_tasks(path.name, path / "examples"):
            yield task



def task_start():
    """start applications"""
    if "jupyterlab" in REPOS:
        yield dict(
            name="jupyterlab",
            uptodate=[lambda: False],
            file_dep=[LAB_APP_INDEX],
            actions=[run_jupyterlab()],
        )


# utilities


def do(*args, cwd=HERE, **kwargs):
    """wrap a CmdAction for consistency"""
    return doit.tools.CmdAction(list(args), shell=False, cwd=str(pathlib.Path(cwd)))


def yarn_integrity(repo):
    """get the file created after yarn install"""
    return [repo / "node_modules/.yarn-integrity"]


def enable_server_extensions(repo):
    """enable server( )extensions in a repo"""
    enable = ["enable", "--py", repo.name, "--sys-prefix"]
    apps = ["serverextension"], ["server", "extension"]
    return sum(
        [[do("jupyter", *app, *enable), do("jupyter", *app, "list")] for app in apps],
        [],
    )


def run_jupyterlab():
    """start a jupyterlab application"""

    def jupyterlab():
        args = ["jupyter", "lab", "--debug", "--no-browser"]
        proc = subprocess.Popen(args, stdin=subprocess.PIPE)

        try:
            proc.wait()
        except KeyboardInterrupt:
            proc.terminate()
            proc.communicate(b"y\n")

        proc.wait()
        return True

    return doit.tools.PythonInteractiveAction(jupyterlab)


def yield_pa11y_static_tasks(name, path):
    """yield the pair of tasks for generating raw pa11y JSON and HTML"""
    html = [p for p in path.rglob("*.html") if "ipynb_checkpoints" not in str(p)]
    reports = REPORTS / f"{name}/{path.name}"
    report_json = reports / f"pa11y-ci-{name}-{path.name}.json"
    report_html = reports / "index.html"

    yield dict(
        name=f"{name}:{path.name}:pa11y-ci:json",
        file_dep=[*yarn_integrity(PA11Y), *html],
        actions=[
            (doit.tools.create_folder, [reports]),
            (run_pa11y_static, [path, html, report_json]),
        ],
        targets=[report_json],
    )

    yield dict(
        name=f"{name}:{path.name}:pa11y-ci:html",
        file_dep=[report_json],
        actions=[
            (doit.tools.create_folder, [report_html.parent]),
            (run_pa11y_html, [report_json, report_html.parent]),
        ],
        targets=[report_html],
    )


def make_pa11y_ci_process(json_report, pa11y_config):
    """start a pa11y-ci process which redirects its output to a JSON report"""
    pa11y_config_json = json_report.parent / f"{json_report.stem}-config.json"

    pa11y_config_json.write_text(json.dumps(pa11y_config, indent=2), encoding="utf-8")

    pa11y_args = [
        *YARN,
        "--silent",
        "pa11y-ci",
        "--json",
        "--config",
        pa11y_config_json,
    ]

    # use shell redirection, because very large :(
    return subprocess.Popen(
        "{} > {}".format(" ".join(map(str, pa11y_args)), json_report),
        shell=True,
        cwd=str(PA11Y),
        stdout=subprocess.PIPE,
    )


def make_static_server_url_stop(root, host=HOST, port=PORT):
    """start a tornado static file server"""

    server_args = [
        "python",
        str(PA11Y / "serve.py"),
        f"--host={host}",
        f"--port={port}",
        f"--path={root}",
    ]

    url = f"http://{host}:{port}/"

    def stop():
        server.terminate()
        server.wait()

    server = subprocess.Popen(server_args)

    return server, url, stop


def run_pa11y_static(root, html_files, json_report):
    """run pa11y against a local static HTML server"""
    server, url, stop_server = make_static_server_url_stop(root)

    pa11y_config = dict(
        urls=[f"{url}{p.relative_to(root).as_posix()}" for p in html_files],
    )

    pa11y_ci = None
    try:
        time.sleep(1)
        pa11y_ci = make_pa11y_ci_process(json_report, pa11y_config)
        pa11y_ci.wait()
    finally:
        if pa11y_ci is not None:
            pa11y_ci.terminate()
        stop_server()


def make_lab_cookie_url_stop(cwd=HERE):
    """run jupyterlab, with the URL, extracted cookie, and cleanup

    These gymastics are required to not pollute the generated URLs
    """
    token = hashlib.sha1(
        "-".join(["T", str(random.random()), "KEN"]).encode("utf-8")
    ).hexdigest()
    lab_args = [
        "jupyter",
        "lab",
        "--no-browser",
        f"--ServerApp.token={token}",
        f"--ServerApp.port={LAB_PORT}",
        "--debug",
    ]

    url = f"http://{HOST}:{LAB_PORT}/lab/"
    cookie = None
    lab = subprocess.Popen(lab_args, stdin=subprocess.PIPE, cwd=cwd)

    def stop():
        lab.terminate()
        lab.communicate(b"y\n")
        lab.wait()

    try:
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        retries = 10
        while retries:
            try:
                time.sleep(0.5)
                res = opener.open(f"{url}?reset&token={token}")
                break
            except urllib.error.URLError:
                retries -= 1
        cookie = res.headers["Set-Cookie"]
    except Exception:
        stop()

    return lab, cookie, url, stop


def run_pa11y_jupyterlab(json_report):
    """running pa11y-ci on JupyterLab"""
    report_root = json_report.parent

    lab, cookie, url, stop_lab = make_lab_cookie_url_stop()

    if cookie is None:
        return False

    # TODO: merge these defaults with a YAML/TOML file
    pa11y_config = dict(
        urls=[
            dict(
                headers=dict(Cookie=cookie),
                url=f"{url}",
                actions=[
                    "wait for element .jp-Launcher to be visible",
                    f"screen capture {report_root}/lab.png",
                ],
            )
        ]
    )

    pa11y_ci = None

    try:
        pa11y_ci = make_pa11y_ci_process(json_report, pa11y_config)
        pa11y_ci.wait()
    finally:
        if pa11y_ci is not None:
            pa11y_ci.terminate()
            pa11y_ci.wait()
        stop_lab()


def run_pa11y_html(json_report, output_dir):
    """finally generate the human-readable HTML report information"""
    subprocess.call(
        [
            *YARN,
            "pa11y-ci-reporter-html",
            "--source",
            json_report,
            "--destination",
            output_dir,
        ],
        cwd=PA11Y,
    )
