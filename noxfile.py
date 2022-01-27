import nox


@nox.session(venv_backend="conda")
def build(session):
    session.install("doit")
    session.run("doit", *session.posargs)

@nox.session(reuse_venv=True)
def docs(session):
    session.install("jupyter-book")
    session.run("jb", "build", ".", "--toc", "docs/_toc.yml", "--config", "docs/_config.yml"), *session.posargs
