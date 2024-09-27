# Jupyter Accessibility

🔔 Looking for [accessibility docs?](https://jupyter-accessibility.readthedocs.io/en/latest/accessibility-docs.html)

Welcome to the GitHub repository for the [Jupyter](https://jupyter.org/) Accessibility Project.
This [software subproject](https://jupyter.org/governance/software_subprojects.html) was formed in early 2019. Its goal is to gather stakeholders interested in working to make Jupyter's
core user-facing software and related tooling accessible.

These core user-facing software include:

- [Classic Jupyter Notebook](https://github.com/jupyter/notebook)
- [JupyterLab](https://github.com/jupyterlab/jupyterlab)
- [JupyterHub](https://github.com/jupyterhub/jupyterhub)

> **Important notice**
> As of August 2022 this software **is not accessible.**
> Significant work will be required to reach that goal. In the meantime, you can track the progress and initiatives in our [Jupyter Accessibility Team Compass](https://jupyter-accessibility.readthedocs.io)

Community projects:

- [jupyterlab-a11y-checker](https://github.com/berkeley-dsep-infra/jupyterlab-a11y-checker)

No longer maintained community projects (not recommended):

- [Jupyter Notebook a11y toolbar](https://github.com/uclixnjupyternbaccessibility/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/accessibility_toolbar) (part of a UCL master's project).

## Getting involved 🙌🏼

### Join the conversation 💬

- [Check out the accessibility section of the community forum](https://discourse.jupyter.org/c/special-topics/accessibility) for ongoing conversations and brainstorms around accessibility in the Jupyter ecosystem.
- [Jupyter Notebook Accessibility Issues](https://github.com/jupyter/notebook/issues?q=is%3Aopen+is%3Aissue+label%3Atag%3AAccessibility)
- [JupyterHub Accessibility Issues](https://github.com/jupyterhub/jupyterhub/issues?q=is%3Aopen+is%3Aissue+label%3Aaccessibility)
- [JupyterLab Accessibility Issues](https://github.com/jupyterlab/jupyterlab/issues?q=is%3Aopen+is%3Aissue+label%3Atag%3AAccessibility)
- Review and join in contributing to [accessibility issues identified for the ongoing CZI EOSS grant](docs/funding/czi-grant-roadmap.md)
- If you find something that you think should be labeled for accessibility, feel free to label it or add a comment.

### Join our JupyterLab accessibility meetings 🤝

Anyone is welcome to attend, if they would like to discuss a topic or to listen in.

- **When**: every other Thursday (check the [community calendar](https://jupyter.readthedocs.io/en/latest/community/content-community.html#jupyter-community-meetings)) at [9:00 AM Pacific Time](https://dateful.com/convert/san-francisco-california?t=900am)
- **Where**: [`jovyan` Zoom](https://zoom.us/my/jovyan?pwd=c0JZTHlNdS9Sek9vdzR3aTJ4SzFTQT09)
- **What**: [current agenda](https://hackmd.io/WnaWXboXSiGoqWvev_fAvA). Feel free to add items to the upcoming event's agenda 🎉

We also have a [public archive of all the previous meeting notes](https://jupyter-accessibility.readthedocs.io/en/latest/community/meeting-minutes/jupyterlab-accessibility-meetings/index.html).

## Links to accessibility standards and resources 🔗

One of our goals is to collect information about accessibility and create documentation to empower the Jupyter community to help us make our software accessible. Please use this section to begin to aggregate relevant third party standards, guides, and documentation related to this:

- [Web Content Accessibility Guidelines 2.1](https://www.w3.org/TR/WCAG21/) - W3C Recommendation
- [The A11Y Project](https://a11yproject.com/)
- [18F Accessibility Guide](https://accessibility.18f.gov/)
- [The tota11y toolbar](https://khan.github.io/tota11y/) is a lightweight Javascript toolbar for quick a11y analysis.
- [The WAVE tool](http://wave.webaim.org/report#/http://z2jh.jupyter.org/) is a web analyzer for page accessibility.

## Contributing to this repo

### Pre-commit hooks 🧹

This repository uses the `prettier` [pre-commit hook](https://pre-commit.com/) to standardize our YAML and markdown structure.

1. Before you can run the hooks, you need to install the pre-commit package manager:

   ```bash
   # using pip
   pip install pre-commit

   # if you prefer using conda
   conda install -c conda-forge pre-commit
   ```

2. From the root of this project, install the git hook scripts:

   ```bash
   # install the pre-commit hooks
   pre-commit install
   ```

3. Optional- run the hooks against the files in this repository

   ```bash
   # run the pre-commit hooks
   pre-commit run --all-files
   ```

Once installed, the pre-commit hooks will run automatically when you make a commit in version control.

### Building the documentation 📖

The documentation is built with [the Jupyter Book documentation engine](https://jupyterbook.org/en/stable/index.html).

Follow the instructions below to build the documentation.

#### Automatically with `nox`

The easiest way to build the documentation in this repository is to use [the `nox` automation tool](https://nox.thea.codes/), a tool for quickly building environments and running commands within them.
This ensures that your environment has all the dependencies needed to build the documentation.

To do so, follow these steps:

1. Install `nox`

   ```bash
   pip install nox
   ```

2. Build the documentation:

   ```bash
   nox -s docs
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `docs/_build/html`.

To build live documentation that updates when you update local files, run the following command:

```bash
nox -s docs-live
```

#### Manually with `conda`

If you wish to manually build the documentation, you can use `conda` to do so.

1. Create a `conda` environment to build the documentation.

   ```bash
   conda env create -n a11y-team-compass-docs python=3.9
   ```

2. Activate the new environment and install the rest of the dependencies:

   ```bash
   conda activate a11y-team-compass-docs
   conda install -f docs/requirements.txt -c conda-forge
   ```

3. Build the documentation:

   ```bash
   jupyterbook build docs
   ```

This will generate the HTML for the documentation in the `docs/_build/html` folder.
You may preview the documentation by opening any of the `.html` files inside.
