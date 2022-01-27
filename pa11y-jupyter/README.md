# pa11y testing tools for Jupyter

This folder contains:

- the schema for validating the [`repos.toml`](../repos.toml) in the root of this repo
- a lightwieght server for hosting static HTML sites
  - we _could_ use the jupyter server, but don't need/want all the bells and whistles
- a minimal (as possible) nodejs environment to run `pa11y-ci` and its reporters

## Future Goals

- extract _tasks_ from [`dodo.py`](../dodo.py) into more configurable, reusable
  components in this folder

- create macros for `pa11y` [actions] for common Jupyter tasks

- improve reporting, e.g. by collecting all generated reports into an interactive
  summary Jupyter Notebook/Book

- release this capability to an appropriate channel for one-click installation
  - ideally PyPI, npmjs.com, conda-forge
    - or if need be, DockerHub, or GitHub Actions

[actions]: https://github.com/pa11y/pa11y#actions
