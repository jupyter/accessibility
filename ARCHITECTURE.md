# architecture document for the `jupyter/accessibility` repository

Accessibility is a cross cutting concern in Project Jupyter. This repository exists as a monorepo to incubate accessibility tooling and resources. In this repository, you will find 3 modules:

1. the `pa11y` python module
2. `jupyterlab` node packages #TODO REMOVE?
3. accessibility testing tools
4. sphinx documentation for the accessibility project.

## `/pa11y` the python module

### python configuration files

what is this now?
is this pa11ly-jupyter?

## `/packages` the node packages

### node configuration files #TODO REMOVE?

no longer exists

## `/docs` the docs

Documentation is generated using our documentation tool [jupyter-book](https://jupyterbook.org/intro.html), a usability layer over `sphinx` for `jupyter` workflows.

`jupyter-book` has two important configuration files.
* `docs/_toc.yml` -- the [table of contents](https://jupyterbook.org/customize/toc.html "documentation for the table of contents")  for the documentation
* `docs/_config.yml` -- the documentation [configuration file](https://jupyterbook.org/customize/config.html)


To build the documenation using [nox](https://nox.thea.codes/en/stable/index.html):

    nox -s docs # build the documentation

or

    python3 -m nox

