# Contributing to jupyter/accessibility

## Code of Conduct

This project follows the [Jupyter Code of Conduct].

[jupyter code of conduct]: https://github.com/jupyter/governance/blob/master/conduct/code_of_conduct.md

## Goal

> To facilitate improving the accessibility of interactive computing, we are trying to make it easy to:
>
> - capture the state of an accessibility feature across number of separate Jupyter
>   repositories at different states of development as [pull requests]
> - deploy them _together_ on [Binder] to share with people for testing
> - assess them on [GitHub Actions] to provide reports, raw data, and feedback
> - work as a team to get the pull requests merged
> - show progress towards an accessibility _Roadmap_

[github actions]: https://github.com/features/actions
[binder]: https://mybinder.org
[pull requests]: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests

## Core Workflow

1. get a free GitHub account
2. make one (or more) [pull requests] to one (or more) Jupyter repositories
3. make a pull request to `jupyter/accessibility` that changes `repos.toml` to
   include the pull requests from **step 2**
4. construct the appropriate Binder link and put it in (all of) the pull request(s)
5. gather and discuss findings
6. update the upstream pull requests
7. repeat steps 3+ as needed
8. get upstream pull requests merged

## Why is this so complicated?

Improving the accessibility of a Jupyter client may require touching many
repositories:

- the client code itself
- dependencies of the client
- the underlying server code, and its dependencies
- formal specifications such as [Jupyter Kernel Messaging] or [Jupyter Notebook Format]

Each component has its own developer workflows and culture.
In this repository, we've tried to collect these development workflows in a
declarative, productive way.

[jupyter kernel messaging]: https://jupyter-client.readthedocs.io/en/stable/messaging.html
[jupyter notebook format]: https://nbformat.readthedocs.io/en/stable/

## On Binder

To meet some of the above challenges, this repository's interactive state on [Binder]
is composed of a full live _development environment_ made of the (hopefully) harmonious
union of different repositories at different states of development from GitHub branches and
[pull requests].

Implemented in [repo2docker]'s [postBuild] stage, this allows for creating very
specific environments without re-inventing too much.

[repo2docker]: https://github.com/jupyterhub/repo2docker
[postbuild]: https://repo2docker.readthedocs.io/en/latest/config_files.html#postbuild-run-code-after-installing-the-environment

## On GitHub Actions

The _GitHub Actions_ workflow performs many of the same steps as _Binder_, but also:

- runs `pa11y-ci` against all generated content
- uploads reports as _artifacts_ which are available to any GitHub user

## Under the Hood

### doit

The workhorse of this approach is [doit]. It is a python-based tool that manages:

- running tasks
  - in the right order
    - when (parts of) files change

> **Why Not Just (Makefile|Docker|your favorite tool)?**
>
> In building and delivering complex environments, we've found `doit` offers a
> mix of portability, expressiveness, and productivity.
>
> _PRs welcome_ to add alternative workflows!

[doit]: https://pydoit.org/
