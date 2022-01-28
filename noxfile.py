
from contextlib import suppress
from pathlib import Path

TOC = Path("docs", "_toc.yml")
CONFIG = Path("docs", "_config.yml")
CONF = Path("docs", "conf.py")

DOIT_CONFIG = dict(verbosity=2)


def task_docs():
    def config():
        with suppress(SystemExit):
            CmdAction(F"jb config sphinx --toc {TOC.absolute()} --config {CONFIG.absolute()} .".split(), shell=False)
    from doit.action import CmdAction
    
    yield dict(
        name="configure",
        file_dep=[TOC, CONFIG],
        actions=[
          config  
        ],
        targets=[CONF],
        clean=True,
    )
    yield dict(
        name="build",
        actions=[F"sphinx-build -c {CONF.parent} . _build/html"],
        targets=["_build/html/index.html"],
        uptodate=[False]
    )
try:
    import nox
except ModuleNotFoundError:
    pass
else:
    @nox.session(venv_backend="conda")
    def build(session):
        session.install("doit")
        session.run("doit", *session.posargs)

    @nox.session(reuse_venv=True)
    def docs(session):
        session.install("jupyter-book", "doit")
        session.run("doit", "-f", "noxfile.py", *session.posargs), 
