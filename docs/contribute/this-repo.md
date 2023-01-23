# Contributing to `jupyter/accessibility`

This Team Compass is a guide for team members of `jupyter/accessibility` and the broader community to navigate the project
and keep track of the accessibility-related initiatives in the Jupyter ecosystem.

If you see information that is out of date, propose an edit in the [`jupyter/accessibility` repository](https://github.com/jupyter/accessibility).
To propose an edit directly from the documentation, click on the `GitHub icon` on the top of any page {fab}`github`
and then on the {fas}`pencil-alt` `Suggest an edit` menu item.

## Issues and labels

Before you open a new issue, please check if any of our open issues cover your idea already.
If you open a new issue, please follow our basic guidelines laid out in our issue templates.

We have a number of labels in the repository - this helps us orient ourselves around what type of contribution is needed as well as to signal the type of skills this might involve.
You can see the full list of issue labels in our [`jupyter/accessibility` repository](https://github.com/jupyter/accessibility/labels).

## Making a Change with a Pull Request

The following steps are a guide to help you contribute in a way that will be straightforward for everyone to review and move forward.

1. Comment on an [existing issue][accessibility-issues ] or open a new issue referencing your addition

   This allows other members of team to confirm that you aren't overlapping with work that's currently underway
   and that everyone is on the same page with the goal of the work you're going to carry out or proposing.

2. Fork the [`jupyter/accessibility` repository][accessibility-repo]

   This is now your own unique copy of `jupyter/accessibility`.
   Changes here won't affect anyone else's work, so it's a safe space to explore edits to the content!

3. Make the changes you've discussed

   Try to keep the changes focused.
   If you submit a large amount of work all in one go it will be much more work for whoever is reviewing your pull request.

   While making your changes, commit often and write self-explanatory commit messages.
   [This blog by Chris Beams](https://chris.beams.io/posts/git-commit/) explains how to write a good Git commit message and why it matters.
   It is also perfectly fine to have a lot of commits - including ones that break code.

4. Submit a Pull Request (PR)

We encourage you to open a pull request as early in your contributing process as possible.
This allows everyone to see what is currently being worked on.
It also provides you, the contributor, feedback in real-time from both the community and the continuous integration as you make commits (which will help prevent stuff from breaking).

A member of `jupyter/accessibility` team will then review your changes to confirm that they can be merged into the main repository.
A review will probably consist of a few questions to help clarify the work you've done.
Keep an eye on your GitHub notifications and be prepared to join in that conversation 🔔.

## Making Changes to the Team Compass

### Adding Content

The source for the Team Compass content is located in the `docs` directory and is organized under the following chapters:

- Accessibility Efforts - content is located in `docs/resources`
- Community - Community Meetings and Events - located in `docs/community`
- Community - Contribute to Jupyter Accessibility - located in `docs/contribute`
- Accessibility resources - located in `docs/resources`
- Funded Accessibility Work - located in `docs/funding`

Additionally, the landing page is located in `docs/index.md`.

#### Adding a New Chapter

1. Create a new directory under `docs/` and an `index.md` file, which will be the top page of the new section.
2. Add a new `chapter` in the Table of contents `docs/_toc.yml`.
3. As you add more sections in the new chapter, make sure to add the corresponding `file` entries in the Table of contents `docs/_toc.yml`.

#### Adding a New Section to a Chapter

1. Create a new `.md` file in the most suitable directory within `docs/`.
2. Add the file path to the `file` entry in the Table of contents `docs/_toc.yml`.

### Pre-commit Hooks

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

Optional- run the hooks against the files in this repository

```bash
# run the pre-commit hooks
pre-commit run --all-files
```

Once installed, the pre-commit hooks will run automatically when you make a commit in version control.

### Building the Team Compass

The Team Compass is built with [the Jupyter Book documentation engine](https://jupyterbook.org/en/stable/index.html).

Follow the instructions below to build the Team Compass on your local computer.

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

Optional: build live documentation that updates when you update local files, run the following command instead:

```bash
nox -s docs-live
```

#### Manually with `conda`

If you wish to manually build the documentation, you can use `conda` to do so.

1. Create a `conda` environment to build the documentation.

   ```bash
   conda env create -n accessibility-docs python=3.9
   ```

2. Activate the new environment and install the rest of the dependencies:

   ```bash
   conda activate accessibility-docs
   conda install -f docs/requirements.txt -c conda-forge
   ```

3. Build the documentation:

   ```bash
   jupyterbook build docs
   ```

This will generate the HTML for the documentation in the `docs/_build/html` folder.
You may preview the documentation by opening any of the `.html` files inside.

## Reference Links

- [Jupyter Book documentation](https://jupyterbook.org/en/stable)

<!-- links -->

[accessibility-issues]: https://github.com/jupyter/accessibility/issues
[accessibility-repo]: https://github.com/jupyter/accessibility
