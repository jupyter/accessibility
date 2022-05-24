# Architecture document for the `jupyter/accessibility` repository

- [Architecture document for the `jupyter/accessibility` repository](#architecture-document-for-the-jupyteraccessibility-repository)
  - [:world_map: Code Map](#world_map-code-map)
    - [:book: `/docs`](#book-docs)
    - [`jupyter-book` configuration files](#jupyter-book-configuration-files)
    - [:ballot_box_with_check: `/testing`](#ballot_box_with_check-testing)
    - [`/testing/tools`](#testingtools)
    - [`/testing/jupyterlab`](#testingjupyterlab)
    - [`/testing/notebooks`](#testingnotebooks)

## :checkered_flag: Introduction

Accessibility is a cross-cutting concern in Project Jupyter.
This repository exists as a monorepo to incubate accessibility tooling and resources.
In this repository, you will find the following:

1. The [Binder configuration files](./.binder)
2. [GitHub workflows and issues templates](./.github)
3. [Sphinx documentation](./docs) for the accessibility project
4. [Accessibility testing tools](./testing) for the user-facing core Jupyter software
5. The [`ja11y` python module](./pa11y-jupyter)

## :world_map: Code Map

This section talks briefly about various important directories and data structures.
When adding new tools or tests make sure to follow the convention of files and directories already established.

```ascii
.
├── .binder
├── .github
├── docs
├── pa11y-jupyter
├── testing
├── .gitpod.yml
├── .readthedocs.yaml
├── ARCHITECTURE.md
├── conf.py
├── CONTRIBUTING.md
├── dodo.py
├── LICENSE
├── noxfile.py
├── README.md
├── repos.toml
└── repos.yml
```

### :book: [`/docs`](./docs)

Contains the source for the Jupyter accessibility documentation as well as the [requirements](docs/requirements.txt) file.
The docs are built using [JupyterBook](https://jupyterbook.org/en/stable/intro.html) and [ReadTheDocs](https://readthedocs.org/).
To build the documentation locally run the following command:

```bash
    nox -s docs # build the documentation
```

### `jupyter-book` configuration files

* `docs/_toc.yml`: the table of contents. For more details on structuring docs using JupyterBook visit the
  [documentation for the table of contents](https://jupyterbook.org/customize/toc.html)
* `docs/_config.yml`: documentation configuration file. To learn more about the configuration options on
  [JupyterBook visit their configuration documentation page](https://jupyterbook.org/en/stable/customize/config.html)

### :ballot_box_with_check: [`/testing`](./testing)

Contains the testing tools and supporting scripts for the automated accessibility tests.

#### [`/testing/tools`](./testing/tool)

Contains common tools for the tests such as Dockerfiles and bash scripts. Any tool or script that will be reused by
multiple tests should be placed here to avoid duplication.

#### [`/testing/jupyterlab`](./testing/jupyterlab)

JupyterLab's accessibility tests and corresponding files to create your local development environment.
To learn more about how to set your environment and using the tests make sure to read the [/testing/jupyterlab/README.md](testing/jupyterlab/README.md) file.

#### [`/testing/notebooks`](./testing/notebooks)

Sample Jupyter notebooks used across the automated tests.

#### [`.gitpod.yml`](./.gitpod.yml)

Configuration file for Gitpod development. For more details see the [JupyterLab testing documentation](/testing/jupyterlab/README.md).
