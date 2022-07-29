# We use nox to automate the process of running installing dependencies and building the documentation
# You can run an individual session by running `nox --session name`, for example:
# nox --sessions docs
# To get a list of available sessions, run:
# nox --list

import nox

nox.options.reuse_existing_virtualenvs = True
BUILD_COMMAND = ["-b", "html", "docs", "docs/_build/html"]


def install_deps(session):
    """Install dependencies for the project. Leveraging conda inside nox so that we can reuse the environment."""
    # Manually installing this because conda is a bit wonky w/ nox
    session.conda_install("--channel=conda-forge", "python=3.9")
    session.install("-r", "docs/requirements.txt")


@nox.session(venv_backend="conda")
def docs(session):
    """Install the necessary dependencies and build the docs.
    Recommended for CI - or if you do not need a realtime preview of the docs."""
    install_deps(session)
    session.run("jupyterbook", *BUILD_COMMAND)


@nox.session(name="docs-live", venv_backend="conda")
def docs_live(session):
    """Install necessary dependencies, buid the docs and use livereload.
    Recommended for local development - livereload allows you to see the changes in rea-time."""
    install_deps(session)

    cmd = ["sphinx-autobuild"]
    for path in ["*/_build/*", "*/tmp/*"]:
        cmd.extend(["--ignore", path])
    cmd.extend(BUILD_COMMAND)
    session.run(*cmd)
