"""testing.py

tasks for testing things
"""
from pathlib import Path
from shutil import copytree, move

WHERE = Path()

FOLDER = Path(__file__).parent
AXE_TEMPLATE = FOLDER / "jupyter-axe"
DOIT_CONFIG = dict(verbosity=2)
TARGET = Path("jupyter-a11y-tests")


def task_playwright(prefix=TARGET / ".env", target=TARGET):
    """interactive testing of jupyter applications"""
    # should be able to modify templates to create different tests

    env = (target / ".env").absolute()
    conda = f"conda run --prefix {env} --live-stream --no-capture-output"
    yield dict(
        name="env",
        actions=[
            do(
                f"""conda create -yc conda-forge --prefix {env} python=3.9 "nodejs>=14,<15" yarn"""
            )
        ],
        uptodate=[env.exists()],
    )

    def mv(src, target):
        copytree(src, target, dirs_exist_ok=True)

    yield dict(
        name="copy-templates",
        actions=[(mv, [AXE_TEMPLATE, target])],
        uptodate=[target.exists()],
    )
    yield dict(
        name="install:yarn",
        actions=[do(f"{conda} yarn install", cwd=target)],
        # targets  yark lock
    )
    yield dict(
        name="install:python",
        actions=[do(f"{conda} pip install -r requirements.txt", cwd=target)],
    )
    yield dict(name="test", actions=[do(f"{conda} npx playwright test", cwd=target)])


def do(*args, cwd=WHERE, **kwargs):
    """wrap a Action for consistency"""
    from os import environ
    from doit.tools import CmdAction

    if len(args) == 1:
        args = args[0].split()
    kwargs.setdefault("env", {})
    kwargs["env"] = dict(environ)
    # kwargs["env"].update(ENV)
    return CmdAction(
        list(map(str, args)), shell=False, cwd=str(Path(cwd).resolve()), **kwargs
    )
