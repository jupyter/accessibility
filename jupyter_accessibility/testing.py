"""testing.py

tasks for testing things
"""
from pathlib import Path
from shutil import copytree, move

WHERE = Path()

FOLDER = Path(__file__).parent
TEMPLATES = FOLDER / "templates" / "pw"
DOIT_CONFIG = dict(verbosity=2)
def task_playwright(prefix=Path("ja11y", "pw-tests"), target=Path("tests")):
    """interactive testing of jupyter applications"""
    # should be able to modify templates to create different tests


    env = (target / ".env").absolute()
    yield dict(
        name="env",
        actions=[
            do(F"""conda create -yc conda-forge --prefix {env} python=3.9 "nodejs>=14,<15" yarn""")
        ],
        uptodate=[env.exists()]
    )
    def mv(*args, **kwargs):
        copytree(*args, **kwargs)
    yield dict(
        name="copy-templates",
        actions=[(mv, [TEMPLATES, target])],
        uptodate=[target.exists()],
    )
    yield dict(
        name="install:yarn",
        actions=[do(F"conda run --prefix {env} yarn install", cwd=target)],
        # targets  yark lock
    )
    yield dict(
        name="install:python",
        actions=[do(F"conda run --prefix {env} pip install -r requirements.txt", cwd=target)],
    )
    yield dict(
        name="test",
        actions=[do(F"conda run --prefix {env} npx playwright test", cwd=target)]
    )



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