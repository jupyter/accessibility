_These notes are from a supplementary meeting to the regular and more general JupyterLab accessibility meetings we've been holding. It was lead by @jasongrout._

# Walkthrough Phosphor Accessibility PRs Meeting Notes - 2020

## Attendees

- Jason Grout @jasongrout
- Martha @marthacryan
- Alex @ajbozarth
- Karla @karlaspuldaro
- Alek @biniona
- Gonzalo @goanpeca
- Isabela @isabela-pf

## Context

This is related to the [Web4All Hackathon](http://www.w4a.info/2019/hackathon/)
on Jupyter from 2019 at the [LightHouse SF](https://lighthouse-sf.org/).

Accessibility standards tend to be written based on HTML forms or
similar standard web use cases. Sometimes it's difficult to figure
out how that impacts JupyterLab since we use lots of things in ways
that weren't intended in the design of such standards.

Some people worked on the "low-hanging fruit" in JupyterLab (like
dialogs) and some people started working on Phosphor since it makes
architectural decisions that interfere accessibility higher up.

- Menus and tabs are the main focuses of the Phosphor work

  - Menus use virtual DOM
  - Menus have been relatively straightforward
  - Tabs have caused some more difficulty

- In menus right now, any menu items can be "checked," but you
  don't have any indication of which menu items can be checked or
  not, it is inferred from the context. Whether or not something can
  have these different states is not accessible information. - This is probably the least controversial change because: - It's backwards compatible - Makes sensible defaults - Small PR - Incremental PR - This might be a good place to start merging. - Should these be the goals we reach for (when relevant) to be
  able to make progress in this area?
  Trying to understand ARIA standards. If/when we talk to experts,
  asking them which tutorials/docs to use (to avoid deprecated ones)
  is a good question.
- There seem to be a few main types of work needed:
  - Additive accessibility work. For example, add ARIA attribute
    and any needed infrastructure to make it possible or consistent
    to call whatever is needed.
  - Reworking existing structure. This tends to be harder and
    create more difficult to resolve discussions.
  - Figuring out what has not been found as an issue yet.
    Exploring other problems.

## WIP Repos

Where a lot of this work lives. Closed issues were pulled upstream.
Open issues hold discussions and work that still needs to be done.

- https://github.com/diagram-codesprint/Web4AllHackathon2019
- https://github.com/diagram-codesprint/jupyterlab
- https://github.com/diagram-codesprint/phosphor

## Relevant PRs and Issues

- https://github.com/phosphorjs/phosphor/pull/404
- https://github.com/phosphorjs/phosphor/pull/405
- https://github.com/phosphorjs/phosphor/pull/406
- https://github.com/jupyter/accessibility/issues/11
- https://inclusive-components.design
- https://github.com/jupyterlab/lumino/issues/81
- https://github.com/phosphorjs/phosphor/pull/406
- https://github.com/jupyterlab/jupyterlab/issues/911#issuecomment-562304755
- https://github.com/jupyter/accessibility
- https://github.com/phosphorjs/phosphor/pull/392

## Miscellaneous Notes

- Lumino needs to be really stable, so will probably need to
  collect changes for a big release to make changes there.
- Things to check:
  - Does this follow Sina's outline of what we need to do?
  - Is this still what we need to do? Has ARIA or other standards
    progressed where we need to reasses?
- When the DOM can reflect what is currently visible on the screen,
  that tends to be a good thing. - If your DOM had an iframe, it used to break enough that it
  made people ask "Maybe we shouldn't be messing with the DOM
  all the time?"" So it was rewrittem the way this works as a
  flat structure. This is terrible for accessibility since there
  is no longer clear indication of what is controlling what. - Semantic versus physical DOM. We're using a semantic DOM to
  address this flat DOM issue.
- Other discussions about tables. DOM as table? Notebooks as
  tables? This would make it easier for screen readers to jump
  around the structure. We don't know where this discussion is
  right now.

## Next steps?

- Split existing PRs between people so that we can make progress
  on problems we already know we have - Get these to be merged or at a state where they could be
  merged and get review from experts/other relevant community
  buy-in
- Get up to speed enough that discussions with experts will not
  waste their time
- Show energy, commitment, and active development on our side so
  that we can gain momentum.
- Collect the lists of issues that have already been found so we
  know what we can d
- Do some reading on relevant standards (ARIA) so we have the
  knoweledge to have meaningful conversations
- Move Phosphor PRs over to Lumino
- Walk through Phosphor https://www.youtube.com/watch?v=GCp4lxOblxg&list=PLFx5GKe0BTjQyCKtiK9TI-ekSuSn_8a3J&index=1
- Is there a way that we can set up a binder image with one of
  these PRs so that it can be easier to help community and/or
  accessibility experts jump in more easily?
- Move all issues we find into the jupyer/accessibility repo so
  that we have an easier list to revisit as we work. https://github.com/jupyter/accessibility/
