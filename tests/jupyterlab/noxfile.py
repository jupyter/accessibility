import nox
from pathlib import Path
from yaml import safe_load

# global variables
FILE = Path(__file__)
TEST_DIR = FILE.parent
ENV_FILE = TEST_DIR / "environment.yml"

# parse the env file
environment = safe_load(ENV_FILE.read_text())
dependencies = environment.get("dependencies")
# note this assumes that the last line is a pip package
# maybe can be improved in the future, but it works for now
requirements = dependencies.pop(-1).get("pip")


def install_environment(session):
    """Install conda dependencies - instead of creating a conda env through
    conda env create -f we install dependency into the session venv.
    This is faster than recreating, updating or pruning the environment using
    conda env...

    Args:
        session (nox.session): Nox session calling the function
    """
    for conda_pkg in dependencies:
        # installing conda dependencies
        session.conda_install(conda_pkg, channel="conda-forge")
        # installing pip dependencies
        for pkg in requirements:
            # We split each line in case there's a space for `-r`
            session.install(*pkg.split())


@nox.session(venv_backend="mamba", reuse_venv=True)
def a11y_tests(session):
    install_environment(session)
    session.run("yarn", "install")
    session.run("npx", "playwright", "install", "chromium")
    session.run("yarn", "run", "test")
