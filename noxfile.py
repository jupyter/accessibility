# We use nox to automate the process of running installing dependencies and building the documentation
# You can run an individual session by running `nox --session name`, for example:
# nox --sessions docs
# To get a list of available sessions, run:
# nox --list

import nox

# ensure we reuse environments instead of creating new ones each time
nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "conda"

DOCS_BUILD_DIR = "docs/_build/html"
BUILD_COMMAND = ["-b", "html", "docs", DOCS_BUILD_DIR]


def install_deps(session):
    """Install dependencies for the project - using conda. Leveraging conda inside nox so that we can reuse the environment."""

    # https://nox.thea.codes/en/stable/tutorial.html#testing-with-conda
    session.conda_install("--channel=conda-forge", "python=3.9")
    session.conda_install("--file", "docs/requirements.txt")


@nox.session(venv_backend="conda")
def docs(session):
    """Install the necessary dependencies and build the docs.
    Recommended for CI - or if you do not need a realtime preview of the docs."""

    install_deps(session)
    session.run("sphinx-build", *BUILD_COMMAND)


@nox.session(name="docs-live", venv_backend="conda")
def docs_live(session):
    """Install necessary dependencies, buid the docs and use livereload.
    Recommended for local development - livereload allows you to see the changes in real-time."""

    install_deps(session)

    session.run("jupyter-book", "config", "sphinx", "docs")
    cmd = ["sphinx-autobuild"]

    for path in ["*/_build/*", "*/tmp/*"]:
        cmd.extend(["--ignore", path])

    cmd.extend(BUILD_COMMAND)
    session.run(*cmd)
