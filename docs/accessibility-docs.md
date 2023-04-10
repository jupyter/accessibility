# Accessibility Docs

If you are looking for accessibility docs[^1] for
[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), [Jupyter
Notebook](https://jupyter-notebook.readthedocs.io/en/stable/), or
[JupyterHub](https://jupyterhub.readthedocs.io/en/stable/), they don't exist
yet. (If you're not sure what accessibility docs are, we mean documentation
written specifically for disabled users. It should cover what features exist
in the software to help make it more accessible. Example: the [accessibility
docs for Visual Studio
Code](https://code.visualstudio.com/docs/editor/accessibility).)

Frankly, the accessibility of these products is not great. For example, as of
April 2023, none of them comply with the [Web Content Accessibility
Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines).
But we want and hope to change that.

## JupyterLab accessibility docs

There are no JupyterLab accessibility docs yet. In the meantime, if you're
trying to get a sense of whether or not you will be able to use JupyterLab, you
may find the [JupyterLab Accessibility
Statement](./resources/JupyterLab-a11y-statement.md) helpful in making an
evaluation.

Side note: adding accessibility docs to JupyterLab is on the
[roadmap](https://jupyter-accessibility.readthedocs.io/en/latest/funding/czi-grant-roadmap.html),
and the [task is tracked on
GitHub](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/issues/173).

## Using Jupyter tools with assistive technology

If you are trying to use Jupyter tools with assistive technology now, you may be
able to get basic support with the following:

- [Jupyter Notebook a11y
  toolbar](https://github.com/uclixnjupyternbaccessibility/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/accessibility_toolbar)
  (from Microsoft research - ⚠️ note this has not been maintained since 2019)
- Make cells editable with a screen reader using the [NVDA Browser Nav
  add-on](https://addons.nvda-project.org/addons/browsernav.en.html#:~:text=BrowserNav%20addon%20for%20NVDA,comments%20or%20malformed%20HTML%20tables.”)
