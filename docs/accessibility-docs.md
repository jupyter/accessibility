# Accessibility Docs

If you are looking for accessibility docs for
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

## Quick start for writing project accessibility docs

Accessibility docs should help disabled users decide whether a Jupyter tool can
support their workflow today, and help contributors improve accessibility
without guessing. If a project is not fully accessible yet, say that plainly and
describe the current status, known limitations, workarounds, and where users can
report barriers.

When adding or revising accessibility docs for a Jupyter project, start with
these high-impact practices:

1. **Describe the user task.** State which workflow the page supports, such as
   opening a notebook, editing a cell, navigating the file browser, using
   terminals, or managing a server.
2. **Use predictable structure.** Use clear headings, short paragraphs, ordered
   steps, and descriptive link text. Avoid links such as "click here" because
   they are unclear outside their surrounding sentence.
3. **Document keyboard paths.** Include the keyboard route for important actions
   and note where keyboard focus should move after a command, dialog, or error.
4. **Name assistive technology expectations.** When known, describe whether a
   workflow has been tried with screen readers, magnification, speech input, or
   other assistive technology. If it has not been tested, say so.
5. **Provide alternatives for visual content.** Add useful alt text for images,
   summarize charts and diagrams in text, and avoid relying on color alone to
   communicate state.

### A useful page pattern

For product-specific accessibility docs, a page can usually start with this
structure:

- **Current status:** what is known to work, what is partially supported, and
  what is not yet supported.
- **Supported workflows:** the tasks users can reasonably attempt today.
- **Keyboard navigation:** important shortcuts, focus order notes, and known
  focus traps.
- **Screen reader notes:** tested browser and screen reader combinations, plus
  any mode switching that matters.
- **Known barriers:** open issues, temporary workarounds, and links to relevant
  tracking issues.
- **How to report a barrier:** the issue template, labels, or community forum to
  use, and what information helps maintainers reproduce the problem.
- **Review date:** when the page was last checked, because accessibility status
  changes as the project changes.

### Alt text decision guide

| Content type | Recommended documentation approach |
| --- | --- |
| Informative screenshot | Describe the purpose of the screenshot and the state it shows, not every visual detail. |
| Decorative logo or divider | Use empty alt text or hide it from assistive technology where the publishing system allows it. |
| Chart or graph | Summarize the main takeaway near the chart and link to the underlying data when available. |
| Architecture or workflow diagram | Add a short text explanation of the flow, actors, inputs, and outputs. |
| Icon in an instruction step | Name the action or control, such as "Run" or "Save", instead of describing the icon shape alone. |

The [W3C alt text decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)
and [Write the Docs accessibility guide](https://www.writethedocs.org/guide/writing/docs-accessibility/)
are useful references when deciding how much description is needed.

### Review checklist

Before publishing accessibility docs, check that:

- headings are nested in a logical order;
- link text makes sense out of context;
- images, charts, and diagrams have text alternatives;
- steps do not depend only on mouse, touch, color, or spatial instructions;
- keyboard-only users can follow the documented workflow;
- known limitations are described without overstating support; and
- issue links or reporting instructions are included for unresolved barriers.

Accessibility documentation should not claim conformance unless the project has
evidence to support that claim. It is still valuable to document partial support,
known gaps, and active improvement work.

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
