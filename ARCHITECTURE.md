# architecture document for the `jupyter/accessibility` repository

Accessibility is a cross cutting concern in Project Jupyter. This repository exists as a monorepo to incubate accessibility tooling and resources. In this repository, you will find 3 modules:

1. the `ja11y` python module
2. `jupyterlab` node packages
3. accessibility testing tools
4. sphinx documentation for the accessibility project.

## `/ja11y` the python module

### python configuration files

## `/packages` the node packages

### node configuration files

## `/docs` the docs

`jupyter-book`, a usability layer over `sphinx` for `jupyter` workflows, is our documentation tool.

    nox -s docs # build the documentation

### `jupyter-book` configuration files

* `docs/_toc.yml`
: the [table of contents](https://jupyterbook.org/customize/toc.html "documentation for the table of contents")  for the documentation
* `docs/_config.yml`
: documentation [configuration file](https://jupyterbook.org/customize/config.html)