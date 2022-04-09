# Contributing to jupyter/accessibility

## Code of Conduct

This project follows the [Jupyter Code of Conduct].

## Links
lol wut is a binder

wut is a doit



## Goal

> To facilitate improving the accessibility of interactive computing, we are trying to make it easy to:
>
> - capture the state of an accessibility feature across number of separate Jupyter
>   repositories at different states of development as [pull requests]
> - deploy them _together_ on [Binder] to share with people for testing
> - assess them on [GitHub Actions] to provide reports, raw data, and feedback
> - work as a team to get the pull requests merged
> - show progress towards an accessibility _Roadmap_

## Community Structure - The Jupyter Project and Subprojects
The work being done in this repository will begin by centering around advocating for accessibility and building accessiblility-centered features within the JupterLab, JupyterNotebook, and JupyterHub sub-projects within the larger Jupyter project. Some information to connect you to those projects and organizations is located below.
### The Jupyter Project
* [Jupyter Website]
* [Jupyter Gitter]

- [Check out the accessibility section of the community forum](https://discourse.jupyter.org/c/special-topics/accessibility) for ongoing conversations and brainstorms around accessibility in the Jupyter ecosystem.

### JupyterLab
[JupyterLab](http://jupyterlab.readthedocs.io/en/stable/) is the next-generation user interface for [Project Jupyter](https://jupyter.org) offering
all the familiar building blocks of the classic Jupyter Notebook (notebook,
terminal, text editor, file browser, rich outputs, etc.) in a flexible and
powerful user interface.
JupyterLab will eventually replace the classic Jupyter Notebook.
* [JupyterLab Repository]
* [JupyterLab Documentation]
* [JupyterLab Contribution Guide]
* [JupyterLab Accessibility Issues]


### JupyterNotebook
The Jupyter notebook is a web-based notebook environment for interactive computing.
* [JupyterNotebook Repository]
* [JupyterNotebook Documentation]
* [JupyterNotebook Contribution Guide]
* [JupyterNotebook Accessibility Issues]

### JupyterHub
With [JupyterHub](https://jupyterhub.readthedocs.io) you can create a
**multi-user Hub** that spawns, manages, and proxies multiple instances of the
single-user [Jupyter notebook](https://jupyter-notebook.readthedocs.io)
server.

[Project Jupyter](https://jupyter.org) created JupyterHub to support many
users. The Hub can offer notebook servers to a class of students, a corporate
data science workgroup, a scientific research project, or a high-performance
computing group.
* [JupyterHub Repository]
* [JupyterHub Documentation]
* [JupyterHub Contribution Guide]
* [JupyterHub Accessibility Issues]


## Core Workflow

1. get a free GitHub account
2. make one (or more) [pull requests] to one (or more) Jupyter repositories
3. make a pull request to `jupyter/accessibility:ci` that changes `repos.toml` to
   include the pull requests from **step 2**
   - the pull request _target_ should be the `ci` branch
4. construct the appropriate Binder link and paste the Markdown in (all of) the
   pull request(s)
5. gather and discuss findings
6. update the upstream pull requests
7. repeat steps 3+ as needed
8. get upstream pull requests merged

* What even is a binder?
* Where is jupyter/accessibility:ci? Is this just where the CI lies?

## Why is this so complicated?

Improving the accessibility of a Jupyter client may require touching many
repositories:

- the client code itself
- dependencies of the client
- the underlying server code, and its dependencies
- formal specifications such as the [Jupyter Kernel Messaging] or the [Jupyter Notebook Format]
  - changes at this level often require a new [Jupyter Enhancement Proposal] (JEP)

Each component likely has its own developer workflows and culture.
In this repository, we've tried to collect the workflows in a declarative, productive
way, that allows trying out _Code From The Future_, without blocking review until
_every_ pull request merged.

* links to jupyter respoisitories?


## On Binder

> Reproduce locally with `doit app docs`

To meet some of the above challenges, this repository's interactive state on [Binder]
is composed of a full live _development environment_ made of the (hopefully) harmonious
union of different repositories at different states of development from GitHub branches and
[pull requests].

Implemented in [repo2docker]'s [postBuild] stage, this allows for creating very
specific environments without re-inventing too much.

## On GitHub Actions

> Reproduce locally with `doit report`

The _GitHub Actions_ workflow performs many of the same steps as _Binder_, but also:

- runs `pa11y-ci` against all generated content
- uploads reports as _artifacts_ which are available to any GitHub user

## On Your Computer

You can do all of the things that happen on _Binder_ and _GitHub Actions_ on your
computer.

- Get [Miniforge] for `conda`
  > - if your computer runs Windows, please ensure you:
  >   - install `conda` on short path, e.g. `c:\mf`
  >   - clone this repo to a short path, e.g. `c:\git\a11y`
- Make an environment like the one in [Binder](./.binder/environment.yml)

  ```bash
  conda env update .binder/environment.yml
  conda activate a11y
  ```

- List all the `doit` tasks

  ```bash
  doit list --all --status
  ```

- Try out different `doit` tasks! The most _fun_ one is:

  ```bash
  doit start
  ```

  which actually... starts JupyterLab!

## Under the Hood

### doit

* Doit should be explained further

The workhorse of this approach is [doit]. It is a python-based tool that manages:

- running tasks
  - in the right order
    - when (parts of) files change

#### Why Not Just (make|docker|pants|scons|bazel|grunt|...)?

In building and delivering complex environments, we've found `doit` offers a
mix of portability, expressiveness, and productivity. Being python-based
we can be relatively sure it's going to work anywhere Jupyter works. Despite
it's quirks, python is good at reading strings and running processes. Ensuring
work isn't repeated is really important when welding together _n_ development
workflows.

> _**PRs welcome** to add alternative workflows that meet all these criteria!_

[doit]: https://pydoit.org/
[binder]: https://mybinder.org
[github actions]: https://github.com/features/actions
[jupyter code of conduct]: https://github.com/jupyter/governance/blob/master/conduct/code_of_conduct.md
[jupyter kernel messaging]: https://jupyter-client.readthedocs.io/en/stable/messaging.html
[jupyter notebook format]: https://nbformat.readthedocs.io/en/stable/
[miniforge]: https://github.com/conda-forge/miniforge/releases
[postbuild]: https://repo2docker.readthedocs.io/en/latest/config_files.html#postbuild-run-code-after-installing-the-environment
[pull requests]: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests
[repo2docker]: https://github.com/jupyterhub/repo2docker
[jupyter enhancement proposal]: https://github.com/jupyter/enhancement-proposals
[Jupyter Gitter]: https://gitter.im/jupyter/jupyter
[Jupyter Website]: https://jupyter.org/
[JupyterLab Repository]:https://github.com/jupyterlab/jupyterlab
[JupyterLab Documentation]:https://jupyterlab.readthedocs.io/
[JupyterLab Contribution Guide]: https://github.com/jupyterlab/jupyterlab/blob/master/docs/source/developer/contributing.rst
[JupyterNotebook Repository]: https://github.com/jupyter/notebook
[JupyterNotebook Documentation]:https://jupyter-notebook.readthedocs.io/
[JupyterNotebook Contribution Guide]:https://github.com/jupyter/notebook/blob/main/CONTRIBUTING.md
[JupyterHub Repository]: https://github.com/jupyterhub/jupyterhub
[JupyterHub Documentation]: https://jupyterhub.readthedocs.io/en/stable/
[JupyterHub Contribution Guide]:https://github.com/jupyterhub/jupyterhub/blob/main/CONTRIBUTING.md
[JupyterNotebook Accessibility Issues]: https://github.com/jupyter/notebook/issues?q=is%3Aopen+is%3Aissue+label%3Atag%3AAccessibility
[JupyterHub Accessibility Issues]: https://github.com/jupyterhub/jupyterhub/issues?q=is%3Aopen+is%3Aissue+label%3Aaccessibility
[JupyterLab Accessibility Issues]: https://github.com/jupyterlab/jupyterlab/issues?q=is%3Aopen+is%3Aissue+label%3Atag%3AAccessibility