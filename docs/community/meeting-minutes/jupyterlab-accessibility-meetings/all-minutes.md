# All JupyterLab Accessibility Meeting Minutes

This file collects all the separate note files into one place to make it easier to skim the notes or search for topics. It is organized oldest to newest.

## 2020

```{include} 2020/2020-09-30.md

```

```{include} 2020/2020-10-21.md

```

```{include} 2020/2020-11-04.md

```

```{include} 2020/2020-11-18.md

```

```{include} 2020/2020-12-02.md

```

```{include} 2020/2020-12-16.md

```

```{include} 2020/2020-12-30.md

```

## 2021

```{include} 2021/2021-01-13.md

```

```{include} 2021/2021-01-27.md

      - seems convoluted, can we just use
        [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label)
        (this is exactly what it's for)? [Opinions seem mixed](https://developer.paciellogroup.com/blog/2017/04/what-is-an-accessible-name/)

```{include} 2021/2021-02-10.md

```

```{include} 2021/2021-02-24.md

```

```{include} 2021/2021-03-10.md

```

```{include} 2021/2021-04-07.md

```

```{include} 2021/2021-04-21.md

```

```{include} 2021/2021-05-05.md

```

```{include} 2021/2021-05-19.md

```

```{include} 2021/2021-06-02.md

```

```{include} 2021/2021-06-16.md

```

```{include} 2021/2021-07-14.md

```

```{include} 2021/2021-07-28.md

```

```{include} 2021/2021-08-11.md

```

```{include} 2021/2021-08-25.md

```

```{include} 2021/2021-09-08.md

```

```{include} 2021/2021-09-22.md

```

```{include} 2021/2021-10-06.md

```

```{include} 2021/2021-10-20.md

```

```{include} 2021/2021-11-03.md

```

```{include} 2021/2021-11-17.md

```

```{include} 2021/2021-12-01.md

```

```{include} 2021/2021-12-15.md

```

## 2022

```{include} 2022/2022-01-12.md

```

````{include} 2022/2022-01-26.md

```{include} 2022/2022-02-09.md

```{include} 2022/2022-02-23.md

```{include} 2022/2022-03-09.md

```{include} 2022/2022-03-23.md
````

```{include} 2022/2022-04-06.md

```

```{include} 2022/2022-04-20.md

```

```{include} 2022/2022-05-04.md

```

```{include} 2022/2022-06-01.md

```

```{include} 2022/2022-06-15.md

```

```{include} 2022/2022-06-29.md

```

```{include} 2022/2022-07-13.md

- Making JupyterLab accessible for a read-only type experience
  - This is the focus of the report on [#9399](https://github.com/jupyterlab/jupyterlab/issues/9399)
- Making JupyterLab accessible for an interacting/coding experience
- Adding JupyterLab docs for accessibility features
  - Sam gave an anecdote about help pages in docs that lists
    help and resources for screen reader users.
- Adding CI or relevant accessibility tests to the JupyterLab
  contributing workflow ensure accessibility remains a priority - Referenced pydata-sphinx-theme [#292](https://github.com/pandas-dev/pydata-sphinx-theme/issues/292)
  - nteract has some kind of accessibility CI they use (probably focused on react)

```{include} 2022/2022-08-10.md

```

```{include} 2022/2022-08-24.md

```

```{include} 2022/2022-09-07.md

```

  - Needs to conform to what user expect for menu bar interactions
    - Examples: alt focuses menu bar, move between top items
      with arrow keys.
  - Elements of the menu bar to be marked up with ARIA so it can
    be communicated via screen reader - This is brought up as a part of [#9399](https://github.com/jupyterlab/jupyterlab/issues/9399)

- Jupyter Notebook is just a little more accessible than Lab. "Like
  you get in a car and everything is backwards."

#### Agenda items not yet covered

- is this closed? can someone audit it? https://github.com/jupyterlab/jupyterlab/issues/6575
  - https://github.com/jupyterlab/jupyterlab/pull/6359
- some old audits
  - https://docs.google.com/document/d/1oSHOqmtua_3vdoJddvo4u3na71cIZlpEgP73w-0uXFU/edit#heading=h.umcyl9debp28
  - https://docs.google.com/spreadsheets/d/1RWEtBtXEF5vQf_vJzqtGWnPbT0VZI_RZ_H7RWHmgyGs/edit#gid=0
- Should these minutes be somewhere besides one long issue? Could
  the jupyter/accessibility repo (or another repo) hold minutes in
  a way that allows for more organization?
- Agenda item from Chris Holdgraf (Did Max mention they had already
  been discussing this?)
  > 1. Don't forget that we have a little bit of funding from
  >    Bloomberg to run some kind of event around accessibility. I'm not
  >    sure how much flexibility we have with it, but perhaps it is worth
  >    discussing if / how this funding could be useful in a future meeting?
- how should we handle touch events re accessibility?
  - PR for manually converting some touch events to mouse events
    - https://github.com/jupyterlab/lumino/pull/123

#### Next Steps

- Continue moving past triage work to the [project](https://github.com/orgs/jupyterlab/projects/1)
  for tracking (Isabela)
- Follow up on necessary ARIA roles JupyterLab needs (a [lumino PR](https://github.com/jupyterlab/lumino/pull/131/files)
  already started labeling) (Martha)
- Make issue about menu bar focus (no assignment?)
- Update [Monaco plugin](https://github.com/jupyterlab/jupyterlab-monaco)
  for 3.0 (Max post-3.0)
- 3.0 Release! (Jason and Max)
- Review Max's PR (Martha)
- Reach out to accessibility experts we've met with before (Isabela)
- Check the status of [#6575](https://github.com/jupyterlab/jupyterlab/issues/6575) (Isabela)

## 12.30.20 Meeting Minutes

### Attendees

- Gonzalo @goanpeca
- Tony @tonyfast
- Thomas @manfromjupyter
- Isabela @isabela-pf

### Notes

- From JupyterLab Team meeting 12.23.20 discussion

  - > Is single-document mode the more accessible UI? [compared
    >
    > > to JupyterLab default]
  - Thomas says Classic is better, but since that's not being
    updated we need to keep it relevant
  - Can't move tabs on a screen reader
  - Focus on navbar and notebook. Will this help make jupyterlab
    and classic accessible together?
  - Having less things on screen could be helpful because it
    means you can focus on having those things being navigable,
    but it also can risk hiding functions and making things less
    usable.
  - jaws, nvda, focus on low vision ambulatory users because at
    the moment things are completely inaccessible to blind users
    and will keep being so until we fix these needs first.
  - project manager to get different places. need a foundation.
  - Can't currently evaluate JLab well because you can't even
    navigate it right now. Keyboard accessibility and tab order
    are key place to start.

- Agenda item from Chris Holdgraf: "Don't forget that we have a
  little bit of funding from Bloomberg to run some kind of event
  around accessibility." - We agreed that we need to follow up on how much money this is
  to know what we want to do with it. - Parts of the work might be good/more contained project that
  we can get funding for. Maybe the accessible editor is an option?
- What's the strategy?

  - Thomas would like to see all [#9399](https://github.com/jupyterlab/jupyterlab/issues/9399)
    and [#9491](https://github.com/jupyterlab/jupyterlab/issues/9491)
    in next six months. These issues make JupyterLab
    navigable/readable so that it can be more finely evaluated and
    so that you can even reach the editor experience.
  - Currently can't create new notebooks, or change kernel with
    keyboard alone?
  - 6 months: everyone but blind users can use jupyter
  - 12 months: everyone can use JupyterLab
  - Can we convince people to act by framing some of these
    things as helping multiple problems (like a better mobile
    experience)?
  - Would not recommend splitting the team up because we don't
    have a lot of people who have an accessibility background, so
    it might be best to keep our knowledge together.

- Goals for next JupyterLab release? What would we want to
  prioritize? - We think we can do it without formally being a part of
  the release schedule. See above for priorities. - Do the work, show it, and it is usually easier to get
  it incorporated.

### Next steps

- Mark which things are we looking to work on first and make
  sure they are ready to be assigned next meeting (Isabela).
- Look into having regular sprints or other group times to
  work so we can help learn from each other.
- Have a happy new year!

## 01.13.21 Meeting Minutes

### Attendees

- Max @telamonian
- Thomas @manfromjupyter
- Martha @marthacryan
- Jason @jasongrout
- Tony @tonyfast
- Isabela @isabela-pf
- Darian @afshin
- Alex @ajbozarth

Happy new year!

Hooray for JupyterLab 3.0! Congrats and kudos who everyone who
worked hard on it.

### What are people working on?

Go around the meeting area and ask.

- Martha

  - [#149](https://github.com/jupyterlab/lumino/pull/149) -
    Realized I needed to add more to lumino and not jupyter lab
    for the toggleable stuff
  - Tota11y toolbar (recommended by Thomas) is a potential tool
    for testing this.
  - https://khan.github.io/tota11y/
  - How does a labeling something as a checkbox with ARIA roles
    differ from using a true HTML checkbox? Using HTML as intended
    usually works better, and screen readers will comment which
    one it is.

- Tony

  - Needs help with setting up linked lumino JLab set up to test
    the work around roles that need to be assigned in lumino.
  - Everytime you make a change in lumino, rebuild lumino before
    JLab.
  - Going through [#9491](https://github.com/jupyterlab/jupyterlab/issues/9491)
  - Interest in creating a binder that also reflects changes in
    Lumino to help each other testing all these things.
  - Other times to pair program on this?

- Max

  - how to work on both lumino and JLab at once: https://github.com/jupyterlab/jupyterlab/blob/master/docs/source/developer/contributing.rst#testing-changes-to-external-packages
  - in progress lumino PR for ARIA roles for tabs: https://github.com/jupyterlab/lumino/pull/132
  - Martha may review?

- Thomas

  - Willing to provide support.
  - Posted https://github.com/jupyterlab/team-compass/issues/98#issuecomment-752748519
    (thank you!)
  - If someone wants something to do that won’t step on other
    people’s toes, lot of elements need either to be hidden or
    revealed. Card: https://github.com/orgs/jupyterlab/projects/1#card-50646346
    as part of #9399. I included a bunch of screenshots if you wanted to started working through it or section by section? https://imgur.com/a/6HvOcYK

- Isabela

  - WIP color contrast at [#8832](https://github.com/jupyterlab/jupyterlab/issues/8832)
    and related PR [#9335](https://github.com/jupyterlab/jupyterlab/pull/9335).
    Will help address sections of [#911](https://github.com/jupyterlab/jupyterlab/issues/911)
    and [#9399](https://github.com/jupyterlab/jupyterlab/issues/9399)
    (since both note color contrast concerns).

- Jason: not actively working on something here specifically, but
  still available for questions and discussion

- Alex and Darian: not actively working on something here, but want
  to keep track and stay part of the discussion.

### What we need to work on

We need to take stock of what's being worked on and split up the
work we know we need to do.

- Here is [the project](https://github.com/orgs/jupyterlab/projects/1)
  for tracking accessibility (should have all issues and PRs we know
  of)(can be reorganized if we have different needs for sorting).
- First priorities include:
- [#9491](https://github.com/jupyterlab/jupyterlab/issues/9491)
  This will make it possible to evaluate JupyterLab with a screenreader
  so we can both be aware of more problems and actually check that
  fixes are working.
- [#9399](https://github.com/jupyterlab/jupyterlab/issues/9399)
  (broken up into steps on the project, click on card to make issue
  when we are ready to work on it). WCAG 2.1 specifications.
- Editor? Is [#4878](https://github.com/jupyterlab/jupyterlab/issues/4878)
  a first priority right now?
- Right to left (RTL) language support?
  - We will likely be working in areas where these changes need
    to be made for labeling reasons, so we may want to see if we
    can include this support at the same time. Especially now that
    we have RTL language transalations for JLab to test it with
    (Gonzalo knows more). More info in issues [#3046](https://github.com/jupyterlab/jupyterlab/issues/3046)
    and [#1163](https://github.com/jupyterlab/jupyterlab/issues/1163).

### Other Notes

- Feedback on accessibility event funding.
  - Update: Probably shouldn't rely on it. It's status isn't
    certain with the pandemic.

## 01.27.21 Meeting Minutes

### Attendees

(oops! No one signed in today so I gave my best guess.)

- Max @telamonian
- Thomas @manfromjupyter
- Martha @marthacryan
- Jason @jasongrout
- Tony @tonyfast
- Alex @ajbozarth
- Karla @karlasupldaro
- Isabela @isabela-pf

### What are people working on?

- How is everyone doing?
  - Come up with different intro questions :upside_down_face:
- Does it make sense to have these meeting notes documented
  outside an issue? I think there's enough content there that
  it's hard to navigate if you aren't just looking for the first
  or last comment. - Yes! Let's propose a place in the Jupyter accessibility repo.
- Can we make an issue about adding accessibility tests to the
  JupyterLab development process? - I was reminded by the discussion started on [JupyterLab
  Classic #80](https://github.com/jtpio/jupyterlab-classic/issues/80). - I've also listed some existing tests. We should review
  these to see if they could work or give us a baseline for
  working with lumino or jupyterlab components. - [squizlabs / HTML_CodeSniffer](https://github.com/squizlabs/HTML_CodeSniffer) - IBM's [accessibility-checker](https://www.npmjs.com/package/accessibility-checker) - [AccessLint / accesslint.js](https://github.com/AccessLint/accesslint.js) - [pa11y / pa11y](https://github.com/pa11y/pa11y-ci) - [dequelabs / axe-core](https://github.com/dequelabs/axe-core)
- Should we also make an issue reminding us to make accessibility
  docs as we make all the WCAG and other changes?
- Check in! In the JLab team meeting, we have accessibility listed
  as an issue people are working on within the JLab 4.0 timeline.
  What scope do we want to report? Are we working on [#9339](https://github.com/jupyterlab/jupyterlab/issues/9399)
  and [#9491](https://github.com/jupyterlab/jupyterlab/issues/9491)
  only right now, or is someone planning to work on the editor? - [#9339](https://github.com/jupyterlab/jupyterlab/issues/9399)
  and [#9491](https://github.com/jupyterlab/jupyterlab/issues/9491)
  for sure. Editor changes are still being researched so mark it
  as possible but uncertain.
- Max started working on [#9491](https://github.com/jupyterlab/jupyterlab/issues/9491)
  - Probably JupyterLab and not lumino level fixes.
- Martha
  - [#9622](https://github.com/jupyterlab/jupyterlab/pull/9622)
    blocked by small translation issue
  - Needs review or advice how to proceed.
  - Otherwise ready to merge (Thomas tested it!)
  - [#149](https://github.com/jupyterlab/lumino/pull/149) Merged!
- Tony
  - [#9648](https://github.com/jupyterlab/jupyterlab/pull/9648)
  - With Max's PR, this should cover #9491!
  - Tony's PR should cover all landmarks.
  - Only thing left is making it so screen readers can access
    those different labels.
  - How does this interact with JLab themes? We need to test
    what this PR means visually.

### Other Notes

- Spatial experience and vision
  - Thomas says you are generally not supposed to label things
    that will be accessed via screen reader with left, right,
    here, so on because it doesn't really mean anything to those
    users.
  - In CSS classes or other areas not accessed by a screen
    reader, this is okay.
- Tab index convention
  - Seems like the main recommendation is to set everything
    to tabindex 0 (because it defaults to the browser).
  - Does this work for JupyterLab?
  - -1 means you aren't going to see it. For example a is a
    tab and buttons are tabbed, so there is possibility for
    things being tabbed twice. So sometimes -1 is to avoid
    redundancy.
  - Tabs are only for people to jump to those regions. They
    do not define the region or header/hierarchy. But tab puts
    you in those places to then announce the region or header.

### Merged PRs (let's celebrate!)

- Martha merged [lumino #149](https://github.com/jupyterlab/lumino/pull/149)! :tada:
- Max merged [lumino #150](https://github.com/jupyterlab/lumino/pull/150)! :confetti_ball:
- Isabela merged [jupyterlab #9335](https://github.com/jupyterlab/jupyterlab/pull/9335)! :sunflower:

### Next steps

- Isabela
  - Propose moving accessibility meeting notes to the
    accessibility repo so they are easier to search.
  - Follow up on test/CI ideas
  - Update accessibility project with merged PRs
  - Start issue for adding accessibility page to docs
  - Add resources to contributing guidelines encouraging people
    to read up on accessibility.
- Thomas
  - Will note the next five steps they recommend focusing on and
    make relevant issues.
- Martha
  - Work on #9622
- Max
  - Review Martha's #149 PR
  - Work on PR for #9491
- Tony
  - Continue on [#9648](https://github.com/jupyterlab/jupyterlab/pull/9648)
    reviewing visual impact and with a JupyterLab-style class name.

## 02.10.21 Meeting minutes

### Attendees

- Max @telamonian
- Tony @tonyfast
- Alex @ajbozarth
- Martha @marthacryan
- Jason @jasongrout
- Isabela @isabela-pf
- Nick @bollwyvl
- Thomas @manfromjupyter

### What are people working on?

- Keyboard shortcuts and default keyboard navigation with assistive
  devices. This Came up with this PR JLab
  [#9031](https://github.com/jupyterlab/jupyterlab/pull/9031) but it
  seems like it could be a bigger discussion for understanding how
  these things interact now and in the future.

  - Thanks to Thomas for replying here!

- Max has been working on a new filebrowser. Trying to bake
  accessibility in on a low level. Issue with notes:

  - https://github.com/jpmorganchase/regular-table/issues/114
  - Using the WAI ARIA spec for grid and table properties. These
    not only need regular labels, but also descriptions for how they
    are nested and a flag for the position.
  - Max would like feedback/for someone to test it with a screenreader.
  - This is a really helpful exploration that should help us with
    other tables used in JupyterLab. Further references with a [treegrid
    example](https://w3c.github.io/aria-practices/examples/treegrid/treegrid-1.html)
    are here.

- Question on Max's [lumino PR](https://github.com/jupyterlab/lumino/pull/132)
  conflicts with https://github.com/jupyterlab/jupyterlab/pull/9622 - Martha reviewed it and is clarifying what labels they are using
  across PRs so that they are consistent.

- Martha's PR at [#9622](https://github.com/jupyterlab/jupyterlab/pull/9622)
  is ready for final review and to be merged after one more commit
  to match labels across PRs.

- Nick
  - For testing: pa11y -s, --standard <name> the accessibility
    standard to use: Section508 (U.S. focused), WCAG2A, WCAG2AA
    (default), WCAG2AAA – only used by htmlcs runner
  - numfocus GSoC team would be a solid team for working on
    accessibility docs

### Other Notes

- Isabela opened
  - [#9742](https://github.com/jupyterlab/jupyterlab/issues/9742)
    because I've had some people asking me about accessibility tests
    elsewhere and I wanted a place to collect the discussion as it
    relates to JLab.
  - an issue on the accessibility repo about best practices for
    [accessibility docs](https://github.com/jupyter/accessibility/issues/15)
- As a last check, remember to ask yourself if things need to be
  translated. - ARIA values usually need it - Table headers might need to be translated? This is worth
  further research. - Data in a table does not need to be.
- Funding discussion
  - Possible Canadian grant: https://accessible.canada.ca/advancing-accessibility-standards-research/funding
  - NSF, NIH, DoE (both of them) NSF future of work https://www.nsf.gov/pubs/2021/nsf21548/nsf21548.htm
  - Does documentation seem like a good project to get outside
    help on?
- Accessibility workshop updates! There isn't something we can
  share now, but people are working on it and there should be
  updates in the next few weeks.

### Merged PRs (let's celebrate!)

- Tony merged [#9648](https://github.com/jupyterlab/jupyterlab/issues/9648)!
  :tada: Thanks to Thomas, Martha, and Max for reviewing it! Congrats, all!

## 02.24.21 Meeting Minutes

### Attendees

- Jason Grout @jasongrout
- Saul Shanabrook @saulshanabrook
- Tony @tonyfast
- Isabela @isabela-pf
- Alex @ajbozarth
- Max @telamonian
- Martha @marthacryan
- Adam @adpatter
- Thomas @manfromjupyter
- And more!

### What are people working on?

- Isabela
  - Should I mention people for feedback on the [meeting minutes PR](https://github.com/jupyter/accessibility/pull/17)? It isn't urgent, but I don't know who would be good to ask.
- Tony
  - codemirror 6 talk about accessebility:  https://ftp.heanet.ie/mirrors/fosdem-video/2021/D.javascript/codemirror.webm 
  - tabindex was not that hard, but the rest is hard.
  - working on https://github.com/jupyterlab/jupyterlab/issues/9686 i am having a hard time understanding what happens to the focus on the sidebar.
    - look at https://github.com/jupyterlab/jupyterlab/pull/9622
  - it is an li with div's inside, replacing with anchors doesnt ever seem to find focus
  - linking setup example https://jupyterlab.readthedocs.io/en/latest/developer/contributing.html#testing-changes-to-external-packages
  - - Probably should add a very concrete example of linking the Lumino packages to develop Lumino and test against JupyterLab
- Saul
  - Learning to code through working on JupyterLab accessability? Good first issues?
    - currently organized issues https://github.com/orgs/jupyterlab/projects/1
    - Thomas's issues are a good (Thanks Thomas!)
    - This is the issue that covers what we need to do to be able to meet WCAG 2.1 standards. We are breaking it up into other issues to work on bit by bit as well (scroll to the bottom of the issue). https://github.com/jupyterlab/jupyterlab/issues/9399
- Max
  - possible scipy 2021 talk
    - talk notes: https://github.com/telamonian/tree-finder/tree/scipy-2021-talk-proposal/docs/scipy_2021
    - collaborators welcome
- Thomas
  - How can we support the work for tablists at [#9622](https://github.com/jupyterlab/jupyterlab/pull/9622)
  - Martha replies that that it needs to be rebased from Max's lumino PR and then it will be ready.
  - For the typescript gods, next priority imo for accessibility are the list items from this comment: https://github.com/jupyterlab/team-compass/issues/98#issuecomment-768800666

### Other notes

- Follow up on accessibility workshop status?
  - Having a meeting later today
- lumino + jlab dev notes: https://jupyterlab.readthedocs.io/en/latest/developer/contributing.html#testing-changes-to-external-packages
  - Saul was working on a binder here that links all lumino packages to juptyerlab: https://github.com/saulshanabrook/binder-jupyterlab-dev/blob/master/binder/postBuild
- setup an intermediate meeting for learning about accessibility and contributing to jupyterlab.

### Next Steps

- Set up binder to show lumino changes instanly for development testing. (Tony, Martha, maybe Max)
- Get merge rights for accessibility repo (Isabela)
- Gather a set of resources/guides to help start up our newcomers.(Isabela)
- Add specific example to lumino development docs that shows how to link it up to JupyterLab (?)
- Rebase #9622 to have it ready for review (Martha)
- Next week meeting to get people up to speed on accessibility efforts (Isabela, Tony, Saul)
- Review #9399 so you get context for what we are doing and we have a good place to start talking (Anyone trying to catch up on our current work)

## 03.10.21 Meeting Minutes

### Attendees

- Gonzalo
- Jason
- Q
- Saul
- Tony
- Nick
- Thomas
- Karla
- Martha
- Isabela

### What are people working on?

- Isabela
  - Looking into writing a CZI grant with the support of Tania and maybe Tony? Just an FYI. I will keep you updated.
  - Trying to write a roadmap of what we are doing that is not just a Github project or made of issues because people keep asking me what we are doing.
- Tony
  - nbconvert
    - nbconvert jinja templates are not accessible, they are just divs. If we made them header elements, then nbviewer will be accessbile
      - Thomas: Could make them accessible just with roles
      - nbiewer: https://nbviewer.jupyter.org/
      - For context nbviewer is a “notebook viewer”.
        - Ex:https://nbviewer.jupyter.org/github/ipython/ipython/blob/6.x/examples/IPython%20Kernel/Index.ipynb
        - It lets you view a jupyter notebook and send that link around
        - Github will also render jupyter notebooks, like it renders markdown. But it does a bad job of it, its very slow
      - Thomas: Why make them look good? Search engine optimization?
      - Nick: There is no SEO, all robots turned off. Its a way public notebooks can be shared
      - This could be a good first issue (because no typescript!)and it still imapcts the comunity.
  - binder for jupyterlab development making changes in lumino [jupyter/accessibility #20](https://github.com/jupyter/accessibility/pull/20).
- Thomas
  - Get all the low vision stuff in one place so people can start jumping into it
  - Ask Gonzalo a question to follow up on internationalization work and overlap with low vision/zoom support. Where are the packages
- Saul

  - A lot of this work seems to be focused on helping folks with vision problems. Have any of them come on this working call? Possibly related to grants, for paying people to help diagnose what the main problems are?
    - At least one person has. Many people don't necessarily disclose why they have the knowlegde they do for us, so I'm unsure.

- Martha
  - Needs to follow up on Max's lumino PR and move forward as much as she can with the related JupyterLab PR. :)

### Other notes

- Follow up on accessibility workshop meeting (two weeks ago)?
  - There should be an email this week following up with people who expressed interest in running workshops to check if they are still interested

### Next Steps

- Review [deathbeds/accessibility #4](https://github.com/deathbeds/accessibility/pull/4). (Isabela)
- Edit/update [jupyter/accessibility readme](https://github.com/jupyter/accessibility/pull/24) to have accurate information about these meetings. (Isabela)
- Get a roadmap draft ready for review (Isabela)
- Review [jupyter/accessibility #20](https://github.com/jupyter/accessibility/pull/20). (Isabela)
- Martha - finish review of Max's lumino PR so that the JL PR can be rebased off of that
  - Actually just took another look and approved
- Start funding/grant discussion for jupyter/accessibility to keep people updated and support other opportunities. (Isabela)
- Publish language packages that have full localization so people can test them (Gonzalo)

## 03.24.21 Meeting Minutes

### Attendees

- MJ
- Tony
- Martha
- Pete Blois
- Jessica Xu
- Saul
- Max
- Nick
- Nina
- Thomas

### What are people working on?

- Isabela

  - Can I add a checklist comment to [#9491](https://github.com/jupyterlab/jupyterlab/issues/9491)? I want to double check that I'm correct about what's been done.
    - There are other blockers still preventing this from getting completed.
    - [#9622](https://github.com/jupyterlab/jupyterlab/pull/9622) merging almost fixes this! Wow!
    - Are there tests? Not yet. We need to be able to verify that this hasn't been overwritten by other work before closing. Aiming for test utils.
  - CZI grant update at [#36](https://github.com/jupyter/accessibility/issues/36).

- Gonzalo

  - Can’t make it to the meeting. Will be releasing the lang packs soon.

- Pete

  - PR [jupyter/accessibility #37](https://github.com/jupyter/accessibility/issues/37)
  - Is this a nbformat fix, or an IPython fix?
    - Probably IPython first will be a big win.
  - Looking into cell outputs having alt text for those by default. This is something we haven't looked into yet.
  - We had a good discussion that clarified some of the nuances to this, so now people need to look into questions and comment on the issue.

- Martha

  - [#9622](https://github.com/jupyterlab/jupyterlab/pull/9622) and [#132](https://github.com/jupyterlab/lumino/pull/132) both merged! Looking for new item to work on
    - Double check 9491 to see if it can be closed.
  - Look into a comment on [jupyterlab/team-compass #98](https://github.com/jupyterlab/team-compass/issues/98#issuecomment-768800666)

- MJ

  - Got some [questions](https://github.com/jupyter/accessibility/discussions/38) when working on the skip link issue [#9688](https://github.com/jupyterlab/jupyterlab/issues/9688)
  - Further discussion about how a `skiplink` should work. Should it just skip to content (notebook), or give options to major regions like the content, top menu bar, left sidebar, right sidebar.
    - Thomas' recommendation is roughly:
      - first tab = main toolbar
      - second tab = left side bar
      - third tab = inside left sidebar section
      - fourth tab = right sidebar
      - fifth tab = inside right sidebar section
  - Tabindex should be 0. Do we need to fix tabindex before skiplink?
    - Shouldn't be a blocker. This will need to be changed, but won't block skiplink as long as you don't hardcode your tabindex values.

- Thomas

  - What is the best resources/instructions for getting a project stood up on my computer for making these accessibility changes.
    - https://jupyterlab.readthedocs.io/en/stable/developer/contributing.html
    - https://jupyterlab.readthedocs.io/en/latest/developer/contributing.html#linking-unlinking-packages-to-jupyterlab
    - [jupyter/accessibility binder PR](https://github.com/jupyter/accessibility/pull/20)?
    - VSCode handles typescript better than some other IDEs. That might help.
  - Added [jupyterlab/jupyterlab #10004](https://github.com/jupyterlab/jupyterlab/issues/10004) and [jupyterlab/jupyterlab #10008](https://github.com/jupyterlab/jupyterlab/issues/10008) issues based on past discussions. These break up certain compliances by disability.

- Nick
  - Pa11y PR in accessibility repo. If this isn't a CI-needing repo maybe we target these tests on another branch so it doesn't slow don't meeting notes and readme PRs. Check [jupyter/accessibility #35](https://github.com/jupyter/accessibility/pull/35)

### Other notes

- Is hackmd a good notetaking platform for people and do you like having a markdown file for the long-term version of the notes? Did you like Tony's issue method better?

### Next steps

- Edit one Phosphor tutorial video to see if it helps with the small screen. (Isabela)
- Turn [#9491](https://github.com/jupyterlab/jupyterlab/issues/9491) to checklist (Martha and Tony) so we can tell its status more clearly. This may be almost closed/resolved.
- Release language packs (Gonzalo)
- Review ideas for Pete's issue and comment on it (Nick and Tony)
- Look into what to work on next starting with [jupyterlab/team-compass #98](https://github.com/jupyterlab/team-compass/issues/98#issuecomment-768800666) comment (Martha)
- Continue with `skiplink` work (MJ) :sunflower:
- Figure out where Pa11y tests fit with jupyter/accessibility.

### Merged PRs (let's celebrate!)

- Martha merged [#9622](https://github.com/jupyterlab/jupyterlab/pull/9622). Hooray! :tada:
- Max merged [#132](https://github.com/jupyterlab/lumino/pull/132). Great work! :confetti_ball:
- Nick and Tony merged [jupyter/accessibility #20](https://github.com/jupyter/accessibility/pull/20). Huzzah! 🥳

## 04.07.21 Meeting Minutes

### Attendees

- Martha
- Max
- Tony
- Jason
- MJ
- Jessica
- Thomas
- Tania
- Isabela

### What are people working on?

- Martha
  - Checking out the focus part of [this issue](https://github.com/jupyterlab/jupyterlab/issues/9491). Not sure if changes are for lumino or JL but I suspect it's lumino
  - There's also no visual indicator of focus which has made this more difficult to test. Browser dev modes should be able to expose this.
- Isabela
  - Coming back to [jupyterlab/jupyterlab #8832](https://github.com/jupyterlab/jupyterlab/issues/8832) with the sidebar and command palette. I'm trying to unpack where all the elements I need to change are in the code.
  - Closing issues in the accessibility repo.
- Thomas
  - Tried to set up local JLab for development. Got blocked but will return.
- Jessica
  - Checking in about whether or not/how arrow keys are reserved for keyboard navigation in order to move forward with an issue.
  - Using just arrow keys is not best practice. It's best they are reserved.
- Tony
  - Has been looking into accessibility testing ecosystem. Lots of JS tools, no Python tools. Some component systems seem to have built in support.
  - How do we move forward with this? Should there be an extension? Can we have this in core JupyterLab?
- Jason
  - Shared [focus-visible](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible) to follow up on focus discussion.

### Other notes

### Next Steps

- Update [jupyterlab/jupyterlab #9742](https://github.com/jupyterlab/jupyterlab/issues/9742) with current testing discussion info (Isabela)
- [jupyterlab/jupyterlab #8832](https://github.com/jupyterlab/jupyterlab/issues/8832) (Isabela)
- Continue working on the focus section of [9491](https://github.com/jupyterlab/jupyterlab/issues/9491) (Martha)
- `skiplink` (MJ)

## 04.21.21 Meeting Minutes

### Attendees

- Max
- Tony
- Isabela
- MJ
- Thomas
- Martha

### What are people working on?

- Martha

  - Found out that JLab has a focus manager that might override native browser focus (which could cause us a lot of accesibility problems potentially). It looks like this might not cause a problem because
  - It is inherrited from [lumino](https://github.com/jupyterlab/lumino/blob/f434ff8bc751b58cc27b9cf0ab7cb31318e8dd15/packages/widgets/src/focustracker.ts)
  - Merged [jupyterlab/lumino #174](https://github.com/jupyterlab/lumino/pull/174) setting `tabindex` to 0 in the menubar. Be on the look out for if this breaks anything unexpectedly.
  - Thomas says the only reason he can think of that you can hard code a tabindex is if you need an area to be focused first, but it's better practice to rearrange the HTML to do what you want.
  - role=menuitem needs a tabindex assigned to make sure this gets the proper treatment.
  - Menu items also need a `disabled` ARIA label.
  - Closed [#9491](https://github.com/jupyterlab/jupyterlab/issues/9491) :tada:

- MJ

  - Draft PR [jupyterlab/jupyterlab #10126](https://github.com/jupyterlab/jupyterlab/pull/10126) for proof of concept making sure the `skiplink` is going in the right place. Looking for feedback on where that component fits in JupyterLab's architecture.
  - Thomas says skiplink always needs to be the first thing on a page, all hacks aside.
  - Max says it might make the most sense to implement it as a widget and add it that way. Put the generalizable part of the code into the widget and the rest elsewhere.
  - Martha and MJ think it might make more sense to add it to an existing widget because it is a small amount of code and should be in all front ends. If that's the case, Martha and Max think `labshell` in [here in `shell.ts`](https://github.com/jupyterlab/jupyterlab/blob/master/packages/application/src/shell.ts#L199) is the best place for it to live not as an extension.

- Tony

  - Integrated Galata and axe-core to get some testing and automated reports started.

- Isabela
  - First round of CZI grant application was accepted so we'll be working on the next step. You can read the full letter of intent at [jupyter/accessibility #44](https://github.com/jupyter/accessibility/pull/44). I think we'll also be looking for community review for this next step?
  - Workshop updates on [jupyter/accessibility #43](https://github.com/jupyter/accessibility/issues/43). I'm trying to follow up with that.
  - My attempts on fixing color contrast in the sidebar and command palette have a very very very draft PR at [jupyterlab/jupyterlab #10101](https://github.com/jupyterlab/jupyterlab/pull/10101). I may not be capable of making all the changes I want myself, but I am trying to do all I can on my own first.

### Next Steps

- Be aware of the focus manager and be on the look out for any problems it might cause (everyone)
- Work on the [skiplink PR](https://github.com/jupyterlab/jupyterlab/pull/10126) based on in-meeting feedback and let us know when it's ready for review! (MJ)
- Get a testing demo running (Tony)
- Fix CZI PDF PR to be in a different directory (Isabela)
- Work on the [sidebar and command palette color contrast PR](https://github.com/jupyterlab/jupyterlab/pull/10101) and let us know when it's ready for review (Isabela)

## 05.05.21 Meeting Minutes

### Attendees

- Max
- Tony
- Isabela
- MJ

### What are people working on?

- MJ
  - Looking for review on [jupyterlab/jupyterlab #10126](https://github.com/jupyterlab/jupyterlab/pull/10126), a pull request to address `skiplink` needs discussed at [#9688](https://github.com/jupyterlab/jupyterlab/issues/9688).
  - Martha and Max followed up, thank you!
  - It seems like a suggestion may have broken the implementation, so we are trying to get it working again.
- Isabela
  - Still focusing mainly on grant writing.
  - Haven't gotten to work on the draft color contrast PR at [jupyterlab/jupyterlab #10146](https://github.com/jupyterlab/jupyterlab/pull/10146).
- Tony
  - How do we keep up community momentum?

### Next Steps

- Changes to get skiplink merged
- Grant writing update and public review

## 05.19.21 Meeting Minutes

### Attendees

- Jason
- Thomas
- Martha
- Tony
- Max
- Sophie
- Max

### What are people working on?

- We did introductions since we had new attendees! Hooray!

- Sophie
  - Interested in getting an overview of what we are doing here and what needs to be done still.
  - May have interest in mentored sprints or other community events to help get a Jupyter interface accessible.
- Martha
  - Looking for guidance on where is the next useful place to contrubute
  - Perhaps [Issue area 1: keyboard navigation of #9399](https://github.com/jupyterlab/jupyterlab/issues/9399)?
  - Checking tab index and skiplink status
- Isabela
  - Workshop funding follow up [jupyter/accessibility #43](https://github.com/jupyter/accessibility/issues/43). Need feedback on "the jupyter/accessibility team have the best visibility onto what would make the most impact. What advise would you have for how to best use these resources?"
  - CZI grant submitted. We won't hear for a few months, so I'll be back to color contrast.x
- Jason reviewed skip links implementation: https://github.com/jupyterlab/jupyterlab/issues/10268
  - Follow up with MJ about availability

### Next Steps

- Follow up on skiplink status (Isabela)
- Next steps for keyboard navigation (check for positive tab index values, potential skiplink next steps) (Martha)
- Workshop follow up (Everyone can post at [#43](https://github.com/jupyter/accessibility/issues/43))
- Color contrast PR [jlab #10146](https://github.com/jupyterlab/jupyterlab/pull/10146)(Isabela)
- Binderhub AWS policy

Priority issues: https://github.com/jupyterlab/jupyterlab/issues/9399

## 06.02.21 Meeting Minutes

### Attendees

- Max
- Thomas
- Tony
- Kevin
- Jason
- Sophie
- Martha

### What are people working on?

- Isabela

  - JupyterLab dev mode not reflecting changes. Help please?
    - Note to self: you can run `jupyter lab --dev-mode --watch` :upside_down_face:
  - Some workshop ideas have been added to [jupyter/accessibility #43](https://github.com/jupyter/accessibility/issues/43).
  - Does anyone know what JupyterHub and/or BinderHub issues, PRs, or other discussions factored in to the blocking of AWS?
    - [jupyterhub/mybinder.org-deploy #1828](https://github.com/jupyterhub/mybinder.org-deploy/issues/)

- Martha

  - [#187](https://github.com/jupyterlab/lumino/pull/187) Needs testing! Also need to fix test failures
    - Jason is reviewing it (thanks)!
  - [#10289](https://github.com/jupyterlab/jupyterlab/pull/10289) Merged! :D :tada:

- Kevin
  - Yjs now supports CodeMirror v6 which has better accessibility support: https://github.com/yjs/y-codemirror.next
  - This should make it pretty easy to switch to CodeMirror 6 at Jupyter
  - jlab 4.0 roadmap (mentions codemirror 6): https://docs.google.com/spreadsheets/d/1r6_ySd18xZwfPexdmlkdFhHUWynaza0zXjrxMMIoLWw/edit

### Next Steps

- Review github project to make sure it's accurate and target next steps for work (Isabela)
- PR with docs for Nick's magic lumino + jlab binder
  - https://github.com/jupyter/accessibility/pull/35
- Follow up on RTC and accessibility. What are next steps for making progress there? (Isabela)
  - https://workspaceupdates.googleblog.com/2019/08/real-time-collab-accessibility.html
  - Thomas: "I think easiest way to do the RTC piece for screenreaders AFTER the product supports reading and editing first, would be to just add screenreader only alerts that simple says 'Tony recently edited the document.' Could say what they added for extra credit. The WCAG requirement now is merey that they are ntofiicated if 'content changed dynamically'”
- Get [#10146](https://github.com/jupyterlab/jupyterlab/pull/10146) for color contrast to a review state (Isabela).
- Follow up about CodeMirror 6 (Isabela and Kevin)
- Follow up about accessibility workshop [jupyter/accessibility #43](https://github.com/jupyter/accessibility/issues/43)

## 06.16.21 Meeting Minutes

### Attendees

- Oops! No one signed in.

### What are people working on?

- Isabela
  - [#10146](https://github.com/jupyterlab/jupyterlab/pull/10146) was merged! This made some color contrast fixes to the filebrowser and command palette.
  - There are still more to-do fixes on the [issue it draws from](https://github.com/jupyterlab/jupyterlab/issues/8832). Has anyone worked on/know where the various search UIs (in the file browser, command palette, and/or extensions) are in the code base?
  - I'm going to the BinderHub team meeting later today to follow up on the AWS blocking and get request a long-term solution.
  - [Accessibility workshop](https://github.com/jupyter/accessibility/issues/43) follow up! We are aiming to have an event by late August/early September.
  - Someone pointed me to W3C's [Authoring Tool Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/atag/). Passing it on.
- Kevin and Cameron
  - Accessibility considerations in RTC commenting?

## 06.30.21 Meeting Minutes

### Attendees

- Mike
- Tony Fast - Quansight
- Isabela
- Adam
- Jason
- Chloe

### What are people working on?

- Adam
  - Does accessibility include accessibility? Answer: yes!
  - Tony shares [The Documentation System](https://documentation.divio.com/) and [Rin Oliver's Writing Documentation with Neurodivergent Open Source Contributors In Mind](https://www.youtube.com/watch?v=TV-bawUDibc)
- Mike
  - What is an accessible code completion experience? There seems to be a gap in documentation here.
- Chloe
  - What are some things to think about with commenting/chat and RTC that aren't just visual?
  - Think about how to make sure content is marked up in a way that it can be accessed. How does all the info on a page
  - Tony shares and https://www.w3.org/WAI/tutorials/page-structure/content/
- Isabela
  - The full multi-skiplink is back on the table if people want to work on that. I went to pick it up and it is beyond my current knowledge level (though I'd love to be a fly on the wall of someone working on this).
    - Needs implementation fix based on [#10268](https://github.com/jupyterlab/jupyterlab/issues/10268)
    - Isabela to follow up with Jason
  - BinderHub meeting update [jupyterhub/binderhub #1309](https://github.com/jupyterhub/binderhub/pull/1309)
  - From the last meetings: [RTC commenting issue](https://github.com/jupyterlab/jupyterlab/issues/10448) and [CodeMirror 6 discussion](https://github.com/jupyterlab/jupyterlab/issues/10370)

### Other ideas

- JupyterLab extension that disables the mouse for manual testing?

### Next Steps

- Update [#8832](https://github.com/jupyterlab/jupyterlab/issues/8832) with info from [#10008](https://github.com/jupyterlab/jupyterlab/issues/10008) and a regression I manually noticed. Turn this checklist into another PR. (Isabela)
- Multiple skiplinks to different regions (Isabela to reach out to Jason)
- Mike is going to look into color stuff? :)

## 07.14.21 Meeting Minutes

### Attendees

- Darian
- Tony
- Martha
- Nick
- Isabela

### What are people working on?

- Isabela and Tony
  - Jupyter Accessibility Workshop
    - We discussed an alternative sprint method for adding alt text to documentation. This does not create regular contributors, but it might solve a big problem and help people learn about accessibility.
    - What could be another goal? Getting a group of people who want to be involved with Jupyter but don't know how a place to start.
- Martha
  - Looking for feedback on [lumino #187](https://github.com/jupyterlab/lumino/pull/187). - Darian says that this should be two PRs. One for focus. One for the expected keyboard bindings.
  - Is this PR still viable? [jupyterlab #6369](https://github.com/jupyterlab/jupyterlab/pull/6369)
    - It is a draft, so we can't do anything to the existing PR. At best we could open a new PR.

### Next steps

- Remove keybindings work on [lumino #187](https://github.com/jupyterlab/lumino/pull/187) and mark it ready for review (Martha)
- Start new lumino PR for keybindings and focus in menus (Martha)
- Test documentation sprint on July 21 (Tony and Isabela) (and anyone else who wants to join!)
- Review [jupyterlab #8832](https://github.com/jupyterlab/jupyterlab/issues/8832) and [jupyterlab #1008](https://github.com/jupyterlab/jupyterlab/issues/1008) for next steps on color contrast (Isabela)

## 07.28.21 Meeting Minutes

### Attendees

- Tony
- Isabela
- Martha
- Carlos
- Jessica

### What are people working on?

- Martha
  - Merged [jupyterlab/lumino #187](https://github.com/jupyterlab/lumino/pull/187) :tada:
  - Looking for next thing to work on!
    - Maybe the next step for skiplink to make there by a list of skiplinks for the different areas. Most recent [skiplink PR](https://github.com/jupyterlab/jupyterlab/pull/10535)
- Carlos
  - Curious about what is happening here!
  - We talked about testing some. Maybe recording and comparing videos might help for tracking interactions and avoiding accessibility regressions.
  - Playwright? [blog post](https://www.yunier.dev/post/2021/accessibility-testing-with-playwright/)
  - How can we support projects
- Isabela
  - and Tony: Jupyter accessibility workshop. You can [track the work here](https://github.com/Quansight-Labs/jupyter-accessibility-workshops).
  - [Notes from the test sprint on July 21](https://hackmd.io/GifZ-RJZR2uXWx5ETcuXEg)
  - Very work-in-progress [alt text guide/review checklist](https://hackmd.io/bkAOZc9wTG6iRMBvaP745Q) based on feedback. Hopefully this can go to many projects once we have a working draft.
  - We are supposed to be hearing back about the CZI grant soon.
  - Binder isn't blocking providers anymore (issue [#1828](https://github.com/jupyterhub/mybinder.org-deploy/issues/1828)). Hooray!
- Jessica
  - Curious about intersection of accssibility & internationalization effort i.e alt text in non-English?

### Next steps

- Review [jupyterlab #8832](https://github.com/jupyterlab/jupyterlab/issues/8832) and [jupyterlab #1008](https://github.com/jupyterlab/jupyterlab/issues/1008) for next steps on color contrast (Isabela)
- Test documentation sprint with NumPy on July 28 (Tony and Isabela) (and anyone else who wants to join!)

## 08.11.21 Meeting Minutes

### Attendees

- Martha
- Isabela
- Jason
- Max
- Nick
- Mike
- Jenn
- Erik

### What are people working on?

- Jenn and Erik
  - Hello from [Space Telescope Science Institute](https://www.stsci.edu/) and [Astropy](https://www.astropy.org/)!
  - Jupyter notebooks aren't accessible and we'd like them to be.
  - We've been working with [GLAS Education](https://www.glaseducation.org/) to test our own work with blind and visually impaired people.
- Nick
  - documentation as an area also lacking accessibility
  - Still trying to get pydata-sphinx-theme PRs merged ([Lighthouse testing](https://github.com/pydata/pydata-sphinx-theme/pull/206) and [pa11y testing](https://github.com/pydata/pydata-sphinx-theme/pull/294))
- Mike
  - question: are outputs returned by kernel, say data frames, accessible/is it being worked on by anyone? I know there is a lot of work on UX, but I wonder how much work will be there in downstream packages which provide outputs
    - [Max] _if you’re talking about the fancy pandas dataframe rendering, the answer is definitely not. There are wcag/aria specs for how to make a grid accessible, tho_
    - [Jason] _That would be awesome if the frontend supported some innate dataframe mimetype which it could render in an accessible way_
  - question: `aria-label` vs `title` (https://github.com/jupyterlab/jupyterlab/pull/10727/files#r685601307)
    - Should this be defined from the toolbar button instead of the tooltip?
    - Isabela will test the binder and see how the current implmentation works.
    - https://github.com/jupyterlab/jupyterlab/pull/10727/files#r685601307
    - https://www.w3.org/TR/wai-aria-practices-1.1/
    - https://www.w3.org/TR/wai-aria-practices-1.1/#wai-aria-roles-states-and-properties-3

### Next steps

## 08.25.21 Meeting Minutes

### Attendees

- Nick
- Martha
- Jason
- Tony
- Isabela
- Max

### What are people working on?

- Max
  - Trying to contribute a Jupyter accessibility design he'd used reccently [as shown here](https://github.com/jupyter/accessibility/issues/54). Needs to follow up with the trademark community.
- Tony
  - Accessible authoring practices for notebooks. How can we support this for authors, not just accessibility in interface.
  - Like what was being discussed at [jupyter/accessibility #37](https://github.com/jupyter/accessibility/issues/37)
  - Isabela: is [Authoring Tools Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/atag/) related?
  - Nick: https://w3c.github.io/annotation-aria/#annotation-model-mappings
  - [chartability](https://chartability.fizz.studio/)
- Nick
  - PyData Sphinx PRs need updating, but that would also be helpful.
  - nbconvert accessible output templates?
- Isabela
  - Workshop! Running several smaller events and want to release the final dates i the next week.
  - [Workshop alt text guide PR](https://github.com/Quansight-Labs/jupyter-accessibility-workshops/pull/1)
  - Nick says Something like [pytest-check-links](https://pypi.org/project/pytest-check-links/) but for alt text?
  - Ideas for other events
    - Take accessibility PRs that have been made and dissect them to get more understanding from Jupyter experts in the community.

### Next steps

- Follow up with the trademark committee (Max)
- Update PyData sphinx theme PRs for [Lighthouse](https://github.com/pydata/pydata-sphinx-theme/pull/206) and [pa11y testing](https://github.com/pydata/pydata-sphinx-theme/pull/294). (Nick)
- Ask Martha about explaining how accessibility needs to fit in to Jupyter (Isabela)
- Follow up/finish alt text guide for workshop (Isabela)

## 09.08.21 Meeting Minutes

### Attendees

- Jason
- Isabela
- Max

### What are people working on?

- [PyData Sphinx theme's pa11y testing PR](https://github.com/pydata/pydata-sphinx-theme/pull/294) has been merged! :tada: Thanks to Nick!
- Jupyter accessibility workshop efforts can be tracked on the [workshop repo](https://github.com/Quansight-Labs/jupyter-accessibility-workshops) and the first two events are scheduled for October 2 and October 9.
  - More announcements to come soon!
  - If you are interested in helping moderate this event, we'd love to hear from you.`
- The [CZI grant for Jupyter accessibility efforts](https://chanzuckerberg.com/eoss/proposals/inclusive-and-accessible-scientific-computing-in-the-jupyter-ecosystem/) did get funded!
  - Our official start is at the beginning of October, so more info to come.
  - The a [PDF of full application is public](https://github.com/jupyter/accessibility/blob/81361c61fd1090fb1dd928d0914f0940192c58e3/grant-applications/Inclusive_and_Accessible_Scientific_Computing_in_Jupyter_Ecosystem_SUBMITTED_PROPOSAL.pdf) and includes a timeline and work we are commited to.
- Outside of Jupyter-specific work, there is also multi-project interest in developing [SPEC(s)](https://scientific-python.org/specs/purpose-and-process/) for accessibility practices in open source. You can [join the discussion here](https://discuss.scientific-python.org/t/discussion-accessible-open-source-projects/63).

### Next steps

- Formal announcement of accessibility workshops (Isabela and Tony)
- Connect with other community workshop people (Isabela)

## 09.22.21 Meeting Minutes

### Attendees

- Martha
- Mike
- Tony
- Isabela
- Kevin
- Jessica

### What are people working on?

- Tony
  - We've been focusing on proposals and planning, but less on JupyterLab specific.
  - Where does RetroLab fit with [#9399](https://github.com/jupyterlab/jupyterlab/issues/9399)
- Mike
  - Navigating cells in notebook with a keyboard is difficult. Mike has been working on something locally to resolve this, but it likely won't be in PR form any time soon because of other projects.
  - If anyone is working on this area of code or the interface, please let him know.
  - Mention him if you are looking for review on PRs.
- CodeMirror 6
  - Still in the air because it will break things so we need someone willing to stand behind breaking things.
  - Kevin has some knowledge about CodeMirror 6 and may be a good point of contact for this.
  - How does rich text fit in with this? Does it make sense to have rich text cells? (ProseMirror or https://www.tiptap.dev/?)

### Next Steps

- Talk about CodeMirror 6 again at the beginning of October

## 10.6.21 Meeting Minutes

### Attendees

- Jason
- Tony
- Adam
- Martha
- Isabela
- Ely
- Thomas

### What are people working on?

- Adam
  - Lumino documentation is lacking and it can interfere with this work.
  - Who would document, give a tutorial, talk, anything?
- Isabela
  - Grant process has begun! Myself and people in charge of me are working on bringing in new people to spend dedeicated development time on this.
  - I'm watching [this ipython/ipython PR](https://github.com/pydata/pydata-sphinx-theme/pull/294) and hoping to see it merged.
- Tony
  - Where does [RetroLab](https://github.com/jupyterlab/retrolab) fit?
  - It isn't core JupyterLab (currently) ([this comment describes how it could be in core in the future](https://github.com/jupyterlab/jupyterlab/issues/9869#issuecomment-936714230)) but has a more streamlined interface that might influence the experience.
- CodeMirror 6
  - Estimated to take at least one month for a single full-time developer
  - 5 and 6 don't have full parity, so that path isn't perfectly clear. You need to account time for that.
  - Kevin is interested in this and would like to work with others.
  - Martha may also be able to help!

## 10.20.21 Meeting Minutes

### Attendees

- Tony
- Jessica
- Nick
- Mike
- Karolina
- Martha
- Jenn
- Ely
- Isabela

### What are people working on?

- Isabela

  - Jupyter accessibility workshops are going through budget approvals now. That's where I'll be halfway through our meeting today.
  - October 25 I will have someone starting with development time devoted to JupyterLab accessibility. Yay! You'll get to meet them soon. (This is made possible by the [CZI EOSS grant](https://blog.jupyter.org/czi-awards-three-eoss-grants-to-jupyter-community-members-6aef43bd9468))
  - This also means I'll have devoted time for accessibility again, so this will help me go back to making contributions.

- Jenn

  - funding question
  - needs to be scoped
  - can have external partners
  - needs follow up

- Mike: just highlighting file system review in https://github.com/jupyterlab/design
  - Extensions and accessibility assessment. Are extensions in the JupyterLab organization the next step?
  - is there an accessibility repo?
    - there is https://github.com/orgs/jupyterlab/projects/1
    - but no repo as for today
    - might be worth to have a repo with acessibility team-compas and to upload artifacts (slides/notes/recommendations) and link to these notes

### Next Steps

- Follow up with Jenn about funding (Isabela+)

## 11.03.21 Meeting Minutes

### Attendees

- Jason
- Martha
- Nick
- Tony
- Frederic
- Mike
- Adam
- Isabela
- Jenn
- Gabriel
- Jessica
- Tania
- Karolina

### What are people working on?

- Jason has been working on formatting keyboard shortcuts, adhering to OS conventions:
  - https://github.com/jupyterlab/lumino/pull/258 (with some exploratory work in https://github.com/jupyterlab/lumino/pull/257). Most of the work affects how keyboard shortcuts are displayed on Mac especially, and I tried to check how things are presented in VoiceOver. I would love if someone would double-check my work when it gets released to make sure it works well with screen readers.
    - Mike: some older articles (2014) highlighted issues with other screen readers: https://www.deque.com/blog/dont-screen-readers-read-whats-screen-part-1-punctuation-typographic-symbols/
  - Mike: tracking `aria-keyshortcuts` in https://github.com/jupyterlab/lumino/issues/261 (help wanted!)
- Jason also is working on switching to using the system font on all platforms: https://github.com/jupyterlab/jupyterlab/pull/11388. The end result of this is that Linux moves from Arial to the system font, which seems to be more readable and wider spacing. You can see examples of the difference by looking at the differences in the screenshots that are updated by the PR.

- Nick says [JupyterLab-fonts](https://github.com/deathbeds/jupyterlab-fonts) (could) add [`opendyslexic`](https://opendyslexic.org/) from [fontsource](https://github.com/fontsource/fontsource/blob/main/FONTLIST.json#L978)

  - https://github.com/deathbeds/jupyterlab-fonts
  - Mike: [JupyterLab Desktop ships a custom set of fonts](https://github.com/jupyterlab/jupyterlab-desktop/pull/59) (we may need to account for that)
  - Should this be a pattern for a theme builder because variables allow for better manipulation and adjustment of things like button sizes or input box sizes.
  - Would there be use in a DOM specification similar to nbformat?

- Tania, Gabriel, Tony, Isabela

  - You can keep up with grant efforts at [Quansight-Labs/jupyter-a11y-mgmt](https://github.com/Quansight-Labs/jupyter-a11y-mgmt) and this will be reported again at meetings in the future.

- Gabriel
  - Thanks to Jason (and whoever else) for contributing docs. I was able to get JupyterLab dev environment up really quickly (less than 1 hour)
  - Mentioned https://www.w3.org/TR/using-aria/#firstrule
- Martha

  - Just wanted to let Gabriel know - you can reach out to me anytime with questions through gitter!

- Isabela
  - Is anyone in contact/know status of Johan's work on the [CodeMirror6 migration](https://github.com/jupyterlab/jupyterlab/issues/10370#issuecomment-942048940)?
    - Work is in progress ([there](https://github.com/jupyterlab/jupyterlab/pull/11638)). CodeMirror6 introduces a completly new API that brings some challenge. So Johan is focusing on having a first draft PR without carry too much about styles/modes and extensions. So people can start to test it and we will be able to evaluate what work is remaining (in particular if some CodeMirror extensions needs to be ported from 5 to 6).
- Frederic
  - I will test [Fast Design components](https://www.fast.design/) from Microsoft and report here.

### Next steps

- Address request for feedback on Jason and Mike's work listed above
- Mike https://github.com/jupyterlab/lumino/issues/261 (help wanted!)
- Frederic will check in with Johan about CodeMirror 6
- Isabela will update the [JupyterLab accessibility project](https://github.com/orgs/jupyterlab/projects/1) to make sure it's ready for people to pick work off again.

## 11.17.21 Meeting Minutes

### Attendees

- Martha
- Ely
- Jason Grout
- Jason Weill
- Tony
- Mike
- Frederic
- Gabriel (Quansight, @gabalafou)
- Nick
- Adam
- Karolina
- Isabela

### What are people working on?

- Shared with us: [Accessibility notebook experiment exploring sound interactions](https://colab.research.google.com/github/hassaku/colab-a11y-utils/blob/master/colab_a11y_util_example.ipynb#scrollTo=021Jdm2npMLf)
- Jason Grout mentioned [colab-a11y-utils](https://pypi.org/project/colab-a11y-utils/). It may be good to explore this package.
- Frederic
  - working on a windowed notebook - this will certainly raise accessibility issue
    - Headers may already not be working well. [jupyterlab/jupyterlab #11374 Anchors are not working properly](https://github.com/jupyterlab/jupyterlab/issues/11374)
    - Virtual rendering in other contexts: [Google Docs](https://workspaceupdates.googleblog.com/2021/05/Google-Docs-Canvas-Based-Rendering-Update.html), [genome browsers](http://2020.ensembl.org/genome-browser/homo_sapiens_GCA_000001405_28?focus=gene:ENSG00000141510&location=17:7544013-7862190)
  - Testing basic components against accessiblity: sharing an example from VS Code (didnot look at the techno used):
    - https://microsoft.github.io/vscode-webview-ui-toolkit/ - This is a storybook website that got a Accessibility tests report  
      ![Webview UI Toolkit's interface showing a list of accessibility test results for a component](https://i.imgur.com/aKRjl2E.png)
    - GitHub repo: https://github.com/microsoft/vscode-webview-ui-toolkit
- Tony
  - Notebook 7 efforts are meant to include accessibility efforts [more info on the plan for Notebook 7](https://github.com/jupyter/notebook/issues/6210#issuecomment-957169113)
  - Nick mentions wanting resources that help accessibility be a part of development as a focus of the repo. Should we be testing things like [Lorenz notebook](https://github.com/jupyterlab/jupyterlab-demo/blob/master/notebooks/Lorenz.ipynb) in accessibility tests?
- Jason W
  - Resources for working on jupyterlab, retrolab, other packages simultaneously?
    - [doit automation file](https://pydoit.org/task_args.html) https://github.com/jupyter/accessibility/blob/main/pa11y-jupyter/dodo.py
    - [Linking/Unlinking Packages to JupyterLab documentation](https://jupyterlab.readthedocs.io/en/stable/developer/contributing.html#linking-unlinking-packages-to-jupyterlab)
    - [An example of testing such things in jupyter/accessibility](https://github.com/jupyter/accessibility/pull/35)
    - [Verdaccio](https://verdaccio.org/)
- Gabriel
  - Poking around the JupyterLab code base, running Galata tests
- Isabela
  - With the CZI EOSS grant, we will be updating our progress via a roadmap.
  - Let's talk about the current [draft roadmap PR](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/pull/60).
  - What information would you all want on this roadmap?
    - Linking to issues might be nice. Which issues make sense (we have duplicate issues across some repositories)?
    - Add another page "changelog" that lists what we have completed when things get moved off the roadmap.
    - Are there repository labels/tags that make sense to link to?

## 12.01.21 Meeting Minutes

### Attendees

| Name                  | Organization                  | GitHub Handle    |
| --------------------- | ----------------------------- | ---------------- |
| tony fast             | quansight                     | @tonyfast        |
| R Ely                 | Bloomberg                     | @ohrely          |
| Chadi Abi Fadel       | American University of Beirut | @real-slim-chadi |
| Isabela Presedo-Floyd | Quansight Labs                | @isabela-pf      |
| Frederic Collonval    | QuantStack                    | @fcollonval      |
| Gabriel Fouasnon      | Quansight Labs                | @gabalafou       |

### What are people working on?

- Chadi
  - [W3C's Web Accessibility Initiative](https://www.w3.org/WAI/)
  - [Australian National University's Different types of disabilities](https://services.anu.edu.au/human-resources/respect-inclusion/different-types-of-disabilities)
- Ely and Tony
  - Can we get review on the [draft workshop agenda](https://hackmd.io/@p5jde6ivTRa6LnqFD8l8wQ/Hk42FoH_Y)
- Frederic
  - PoC [WebComponents for Jupyter](https://github.com/jupyterlab-contrib/jupyter-ui-toolkit) with low level accessibility rules
  - Discussed more in depth in the prior JupyterLab meeting
- Gabriel (Quansight Labs)
  - Automated accessibility testing
  - Quansight Labs [tracks my work on Jupyter](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/issues/assigned/gabalafou) in a public GitHub repo
  - Feel free to reach out to me on [Gitter](https://app.gitter.im/) at @gabalafou or email me gfouasnon@quansight.com
- Isabela

  - I'm back working on [#8832](https://github.com/jupyterlab/jupyterlab/issues/8832) as promised. I have some questions on search/filter boxes this week.

- Pre-meeting chat
  - Ely: High contrast colors that help with low vision may aggravate migranes or other disabilities. Customization seems key.
  - Nick: we could add a PR check to ensure that style values aren't being hard-coded
  - Shared links:
    - [Bay area (currently remote) a11y meetup](https://www.meetup.com/a11ybay/)
    - [sytlelint-scss/stylelint-scss Rule idea: color-no-non-variables #4 ](https://github.com/stylelint-scss/stylelint-scss/issues/4)
    - [stylelint documentation's list of rules for color](https://stylelint.io/user-guide/rules/list/#color-1)

## 12.15.21 Meeting Minutes

### Attendees

- Ely
- Tony
- Gabriel
- Mike
- Isabela
- Saeeda
- Chadi
- Martha
- Carlos
- Jenn

### What are people working on?

- Ely
  - Accessibility workshop is tomorrow!
    - [Here is the workshop agenda](https://hackmd.io/JmEN6JIMTn6f9IKuLCoo0Q)
    - Anyone can join in from the community calendar
- Chadi
  - Getting involved/onboarding needs to support accessibility
  - Sharing work around summarizing accessibility needs
- Carlos
  - RTC user identification uses colors. How to use distinct and accessible color palettes is being discussed on [jupyterlab/jupyterlab issue #11641](https://github.com/jupyterlab/jupyterlab/issues/11641).
    - This issue is based on [a thread on jupyterlab/jupyterlab PR #114430](https://github.com/jupyterlab/jupyterlab/pull/11443#discussion_r761473200)
  - Ely: seems like it needs to be a set of variables defined by the theme since themes can vary so much
  - Tony shares [WCAG 3 will use a new color contrast method called APCA (Advanced Perceptual Contrast Algorithm)](https://twitter.com/DanHollick/status/1468958644364402702)
- Isabela
  - Jupyter accessibility events updates! More updates to come, and you can always reference [the quansight-labs/jupyter-accessbility-workshops repo](https://github.com/Quansight-Labs/jupyter-accessibility-workshops)
  - [jupyterlab/jupyterlab PR #11658](https://github.com/jupyterlab/jupyterlab/pull/11658) is work on color contrast. I've gotten some review but there's lots to discuss.
  - Roadmap updates (for CZI grant reporting and community communication) based on all your feedback. You can review the PR [Quansight-Labs/jupyter-a11y-mgmt #60](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/pull/60). When we get it cleaned up, it will go to jupyter/accessibility so it's more findable by the community.

## 1.12.22 Meeting Minutes

### Attendees

- tony
- Ely
- Mike
- Frederic
- Gabriel
- Martha
- Jason
- Nick
- Matthew
- Chadi

### What are people working on?

- Isabela
  - Jupyter accessibility workshops are upcoming on January 15, January 22, and two events in March.
  - Find all up-to-date links on the [Jupyter blog announcement post](https://blog.jupyter.org/join-us-for-the-jupyter-accessibility-workshops-part-1-133e0e522d1b)
- Gabriel
  - Mapping out and comparing frontend of JupyterLab and RetroLab
- Chadi
  - How to get involved with Jupyter accessibility work
    - Review tasks on the [JupyterLab accessibility project board](https://github.com/orgs/jupyterlab/projects/1)
    - Focus on documentation fixes. Some could be adding alt text, making sure things are up to date.
    - Make changes to documentation theming that supports accessibility across projects (find test background on https://github.com/jupyterlab/jupyterlab/pull/11803 and https://github.com/pydata/pydata-sphinx-theme/pull/548)
    - Open issues based on what isn't working for you! We're relying heavily on standards, but user feedback would be even better.
- Nick
  - exploring [robotframework-axelibrary](https://github.com/adiralashiva8/robotframework-axelibrary) as a thing to add to [JupyterLibrary](https://github.com/robots-from-jupyter/robotframework-jupyterlibrary)
    - should be possible to e.g. configure `Test Teardown` to `Collect Accessibility Violations`
      - ...and when error conditions arise
    - tag with violations which would bubble up to
  - potentially blocked by limited maintainer effort on upstreams
  - also have some data analysis tools for long-term ingest of many robot reports
  - both could be injected into e.g. [robotkernel](https://github.com/robots-from-jupyter/robotkernel/issues/72)

Some links in chat:

- https://github.com/jupyterhub/jupyter-server-proxy/tree/main/tests/acceptance
- https://github.com/robots-from-jupyter/robotlab/
- https://github.com/locustio/locust
- https://github.com/jupyter-server/jupyter_server/blob/main/jupyter_server/services/api/api.yaml
- https://hypothesis.works/
- https://github.com/Zac-HD/hypothesis-jsonschema
- https://testguild.com/python-automation-testing/

## 1.26.22 Meeting Minutes

### Attendees

- Isabela
- Frederic
- Ely
- Jason
- Darian
- Gabriel
- Nick
- Patrick
- Tony

### What are people working on?

- Tony https://github.com/jupyter/accessibility/issues/67
  - What jupyter/accessibility has been so far: kind of a cross-project team compass
  - This PR discusses ways to make it a more resource-focused and active repo. Also to help people actually start using Jupyter tools (that's been a popular ask)
- Patrick
  - Could anyone give an update on how things are currently working, perhaps both high level and in the code?
  - People are interested! We need to follow up and connect these communities
  - Are these communities also willing to giving feedback on how to make better experiences (not just be WCAG compliant) based on how they use these tools?
- Isabela
  - Jupyter accessibility workshop summary/things to do
  - Alt text PRS from the workshop (still in progress until the end of this week)
    - https://github.com/isabela-pf/jupyter/pull/1
    - https://github.com/isabela-pf/jupyter.github.io/pull/1
- Gabriel
  - Does the [JupyterLab settings UI PR](https://github.com/jupyterlab/jupyterlab/pull/11079) add accessibility features/is that a place they could go in the future?
  - Right now? That's not the focus. It could be added in the future.

### Next steps

- Discuss [jupyter/accessibility reorganization](https://github.com/jupyter/accessibility/issues/67) (open for commenting to everyone!)
- Follow up on cross-community collaboration (Isabela, Jenn, Tony, Patrick)
- Remove hardcoded css colors to improve the extensibility of the these (maybe Nick?)

## 2.09.22 Meeting Minutes

### Attendees

- Nick
- Tony
- Martha
- Ely
- Frederic
- Thomas
- Chadi
- Isabela

### What are people working on

- Chadi

  - Interest in being assigned from existing issues
  - nick: ipywidgets needs love. probably no existing issues, needs the audit and issue authoring. "there are definitely some ambulatory items on some of the custom controls"

- Thomas

  - "When is Jupyter Classic going away?"
    - Tony replies with the related Juypyter Enhancement Proposal
    - https://jupyter.org/enhancement-proposals/79-notebook-v7/notebook-v7.html
  - Who's working on the grant now
    - Gabriel (not in meeting today) is the person you want to meet. He's been working on testing at [jupyter/accessibility](https://github.com/jupyter/accessibility/)
  - What's been happening?
    - [stylelint PR may be a start to getting this testable](https://github.com/jupyterlab/jupyterlab/pull/11993)

- Frederic

  - [jupyter-ui-toolkit](https://jupyterlab-contrib.github.io/jupyter-ui-toolkit) update
  - Intent of making all components in JupyterLab more accessible from their foundation rather than only remediation of existing.
  - This has ties to [[WIP] JEP for React.js at Jupyter datalayer/jupyter-react#9](https://github.com/datalayer/jupyter-react/issues/9).

- Tony

  - We need to have some testing notebooks for manual testing. Any thoughts on things/content types we need to make sure to include?
    - Ely: Errors!
    - Nick: the smallest elements, input/output (not even cells). something like [the work at jtpio/replite](https://github.com/jtpio/replite)
    - Nick: run-only experience

- Isabela: Jupyter accessibility workshops in January (summary)
  - Sprint had two alt text PRs come out of it. [Jupyter.org alt text was merged](https://github.com/jupyter/jupyter.github.io/pull/680). [Project Jupyter documentation PR could use review](https://github.com/jupyter/jupyter/pull/607)
- Isabela: Jupyter accessibility workshops in March!
  - Draft sprint topic is on auditing. Is there anything specific you'd all like to have covered? Are there any projects you'd like to propose we use for the sprint?

## 2.23.22 Meeting Minutes

### Attendees

- Tony
- Ely
- Gabriel
- Martha
- Nick
- Jason

### notes

- pdf accessibility https://www.section508.gov/create/pdfs/
- stylelint-a11y https://github.com/YozhikM/stylelint-a11y
- https://bareynol.github.io/mui-theme-creator/ theme editor
- Thoughts from Ely on custom themes
  - should we talk to people who are used to customizing colors?
  - an export button would be really good for someone who has spent a lot of time working on their own theme locally

### What are people working on

- @tonyfast
  - reusable tasks for building jupyterlab, retrolab, lumino combinations.
  - turning [`jupyter/accessibility`](https://github.com/jupyter/accessibility) into a js/py packages

## 3.9.22 Meeting Minutes

### Attendees

- Martha
- Tony
- Jason W
- Jenn
- Isabela
- Gabriel

### Agenda

- Gabriel
  - What do developers want/what would you all find helpful in the [jupyter/accessibility repo](https://github.com/jupyter/accessibility)
    - - People can give feedback and ideas later via issues (or PRs if you have something you want to contribute) on jupyter/accessibility.
  - What I'm working on, just FYI:
    - [Adding checkboxes to JupyterLab file browser](https://github.com/jupyterlab/retrolab/issues/260#issuecomment-1035610998)
    - [Adding infrastructure to run automated accessibility tests](https://github.com/gabalafou/accessibility/tree/axe/tests/retrolab)
- Jason W
  - [JupyterLab cell toolbar PR 12028](https://github.com/jupyterlab/jupyterlab/pull/12028) — Feedback sought on usability, accessibility, etc.
    - Tab behavior is consistent throughout JupyterLab (which is good), but it's JupyterLab's tab behavior that doesn't make sense. This may need to be a separate issue.
      - Tabbing through regions is discussed in https://github.com/jupyterlab/jupyterlab/issues/9688
    - Focus is working throughout, so there is nothing that relies solely on a hover state (good!)
    - How this interacts with a cell's command versus edit state is interesting. Navigating the toolbar happens in command mode, but tabbing fully through the toolbar transitions to edit mode with no immediate way back (instead users must return to the start of command mode outside the cell). This is to preserve the use of tab for code completion in a cell, something we do need to preserve.
- Jenn
  - Grant!
- Tony
  - brings up discussion at [matplotlib/matplotlib #15971 Improve the accessibility of figures shown with `_repr_html_`](https://github.com/matplotlib/matplotlib/issues/15971#issuecomment-1062772917) around deprecation of `longdesc` and if there are ways this can be solved in a better experience and not only one-off tags.

## 3.23.22 Meeting Minutes

### Attendees

- Mike
- Ely
- Martha
- Jenn
- Gabriel
- Tania
- Isabela

### Agenda

Jupyter accessibility workshop resources! (First two events are up, but the last ones are pending. They will all link here.) [Jupyter accessibility workshops repo](https://github.com/Quansight-Labs/jupyter-accessibility-workshops/tree/main/events)

Mike:

- progressbar aria https://github.com/jupyterlab/jupyterlab/pull/12238
  - An addition based on review on a prior pull request.
  - This is something worth testing! Open invite for people to give it a try.
  - Prompted a discussion around what/how can we test these things going forward. Do we have several accessibility fixes we'd like tested where it's worth actively reaching out to people?
  - Similar, but separate from discussion around regular user feedback surveys timed with JupyterLab releases.

Tania:
Jupyter governance and jupyter/accessibility. A discussion around what's happening and where the community thinks we belong!

- The initial proposal:[jupyter/governance #121 Standing Committees and Working Groups PR](https://github.com/jupyter/governance/pull/121)
- Further discussion: [jupyter/governance #124 [Proposal] - add jupyter/accessibility as a software sub-project](https://github.com/jupyter/governance/issues/124)
- :pencil: [Future governance Software Steering Council](https://jupyter.org/governance/software_steering_council.html) roles and responsibilities
- Questions to pass over to the governance body:
  - What are the criteria under which the WG's might or not get voting rights?
  - Same but for continued vote/existence?
- Pros and cons of each level. Summary is that it seems like there's more pros and no real cons on being a software project (long term).

### Next steps

- **TODO**: open an issue on jupyter/accessibility and use it as a RFD (request for discussion)/lazy voting and revisit in 2-4 weeks?
- Isabela to follow up with Mike on asking the community for feedback on existing accessibility fixes.

## 4.6.22 Meeting Minutes

### Attendees

- Frederic
- Nick
- Jason
- Darian
- Martha
- Ely
- Gabriel
- Mike
- Preston
- Tom
- Rohit
- Pooja
- Isabela

### What are people working on?

- Preston

  - Contributing guide questions https://github.com/jupyter/accessibility/issues/47
  - Should this be specific to the repo (not general jupyter contrib)
  - CI. what's the status (based on jupyterlab benchmarks repo)
  - things that don't exist (another issue or what's happening?)
  - Follow up on issue with some of these specifics.

- Tom

  - Has there been a date announced for when support for classic Notebook (as it is now) ends? This has to do with Notebook 7 release work.
  - goal is to only support two versions simultaneously
  - nbclassic package (notebook 6 ui written as jupyter server extension)
  - https://github.com/jupyter/notebook-team-compass/issues/5#issuecomment-1085254000
  - support for extension updates is a priority

- Gabriel

  - :tada: Not much to discuss, but I put up my first JupyterLab PR: [Add checkboxes to file browser #12299](https://github.com/jupyterlab/jupyterlab/pull/12299).
    - Small accessibility win; hopefully will lead to more

- Darian

  - Governance question re: [Working Group and Subproject brought up by Tania](https://github.com/jupyter/governance/issues/124)

- Isabela
  - Open question from me, what do you all want me to work on next?
    - From notebook call: nbgrader importance; could use my attention
    - "It just can't be worse than the existing nbgrader" :laughing:
  - If nothing else, can we go through the [JupyterLab accessibility project board?](https://github.com/orgs/jupyterlab/projects/1)
  - tag people not necessarily accessibility involved if they know what's up
  - ask it in jupyterlab

### Next steps

- Follow up on accessibility fixes survey/feedback request (Isabela to Mike)
- Follow up with Tania about last meeting's governance discussion (Isabela to Tania)
- Three options for governance next steps and have people involved come to consensus (Isabela to create and tag people)

## 4.20.22 Meeting Minutes

### Attendees

- Gabriel F.
- Nick
- Isabela

### What are people working on?

- Please vote on [jupyter/accessibility's status in the new Jupyter governance](https://github.com/jupyter/accessibility/issues/81) by midnight wherever you are today!

- Meeting this Friday, April 22: FAST-based JupyterLab UI toolkit. This is a discussion around [the proposal for a new JupyterLab UI toolkit](https://github.com/jupyterlab/team-compass/issues/143), which we've seen demo'ed for accessibility considerations. Show up or comment on the issue if you'd like to weigh in!

- Isabela

  - [isabela-pf/a11y-events Brainstorm list of event ideas](https://github.com/isabela-pf/a11y-events/issues/4)
  - [Scoping automated testing steps](https://docs.google.com/spreadsheets/d/1mUmZevaEI1HwZQ0uF5Rjhb9mGEJ71RAkjj-Lxr3sLZw/edit?usp=sharing)

- Gabriel

  - A [plan for the next six weeks](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/issues/97) that Quansight Labs is considering
    - A number of learnings about **automated accessibility tests** has been rolled into that doc
  - We are looking for pathways to contributions from other people - especially in this group

- Nick

  - [Model-based testing](https://en.wikipedia.org/wiki/Model-based_testing). Build a user model of somebody using the Jupyter test. A model is more interesting that a particular case because you get to weird error messages and corner cases that we need to test for.
  - [A close example with stateful, property-based testing in Hypothesis](https://hypothesis.readthedocs.io/en/latest/stateful.html)
  - Workflow is not to do this all thinking about it as a test, but more as a state and task combo (ie. I'm looking at a notebook and I want to )

- on the subject of building up a language to create test plans (Isabela metaphor: magnetic fridge poetry)

  - https://github.com/deathbeds/jupyterlab-outsource
  - https://pypi.org/project/jupyterlite-robotkernel
  - goal, action, goal, action, goal action (that's a human-readable way we can work with)
  - https://github.com/robots-from-jupyter/robotframework-jupyterlibrary
  - https://pypi.org/project/robot-axelibrary/
  - https://github.com/ipython/traitlets/pull/705#issuecomment-1103958033

- opt-in a11y checks - label on PR that goes into changelog

- https://github.com/jupyterlab/maintainer-tools
- https://github.com/jupyter-server/jupyter_releaser
- https://pv.github.io/numpy-bench/

## 5.04.22 Meeting Minutes

### Attendees

- Martha
- Isabela
- Gabriel

### What are people working on?

- Isabela
  - Governance follow up. We voted at [jupyter/accessibility #81](https://github.com/jupyter/accessibility/issues/81). Isabela needs to know how to move this forward.
  - Testing updates! We're at the foundation level now, but thoughts on prioirities are welcome.
    - Feedback: documentation is the most valuable thing!
    - Mentioned links: [Quansight-Labs/jupyter-a11y-mgmt #95 Scoping automated testing comment](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/issues/95#issuecomment-1112427588) and [jupyter/accessibility #74 past draft PR for axe-core testing](https://github.com/jupyter/accessibility/pull/74).

### Next steps

- The dream: updated galata documentation.😊
- Follow up about governance status (Isabela)

## 5.18.22 Meeting Minutes

### Attendees

- Isabela
- Martha

### What are people working on?

- jupyter/accessibility is on its way to Subproject status! 🎉 PR is being voted on on [jupyter/governance #129](https://github.com/jupyter/governance/pull/129)
- jupyter/accessibility automated testing has been updated! Changes are still being made, but there's a lot to show.
  - [jupyter/accessibility #83 Axe Gitpod JupyterLab](https://github.com/jupyter/accessibility/pull/83)
  - [jupyter/accessibility #84 Developer tooling for building/testing jupyter artifacts](https://github.com/jupyter/accessibility/pull/84)
  - Isabela: Draft testing scripts (for new, task-style tests) on [a comment on quansight-labs/jupyter-a11y-mgmt #95](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/issues/95#issuecomment-1118978913)
  - [More info on axe-core tests](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md#wcag-21-level-a--aa-rules)
- Isabela
  - Learning and contributing event ideas to keep the community energy going. Rough draft agendas on [a series of comments on isabela-pf/a11y-events #4](https://github.com/isabela-pf/a11y-events/issues/4#issuecomment-1124536984)

## 6.1.22 Meeting Minutes

### Attendees

- Tony
- Mike
- Ely
- Gabriela
- Isabela
- Nikhil

### What are people working on?

- Intros for newcomers!
- Tony
    - [jupyter/accessibility #90](https://github.com/jupyter/accessibility/pull/90) automated accessibility testing efforts
        - [axe-core](https://github.com/dequelabs/axe-core/) test suite
        - Run axe-core tests against JupyterLab in GitHub Actions
        - Will help support user stories for testing in [quansight-Labs/jupyter-a11y-mgmt/discussions/122](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/discussions/122)
    - Automated testing is known to catch only a percentage of known accessibility problems (usually WCAG, which is the minimum itself). How/are there plans to include disabled user testing?
        - Because of open source we need solutions that aren't only tied to people (espcially individuals). But we also agree we need this input. It's been a combo of getting funding (to pay people for their expertise) and some parts of JupyterLab are so inaccessible that we need to fix areas before we can get good feedback.
        - How does this fit with the extension-cookiecutter?
- Voice navigation in JupyterLab?
    - Where to start? Has there been existing work? Not as far as anyone here knows.
    - Having semantic HTML is probably the start, though, because it would allow other tools to hook into JupyterLab well.
    - Some resources on how this work might need to behave: [Browsing with assistive tech - Tetralogical](https://tetralogical.com/blog/2021/12/24/browsing-with-assistive-technology-videos)
- Workshops mentioned in Lab call?
    - There's no current plan from anyone here to submit for the next Community Workshop proposal cycle.

### Next steps

## 6.15.22 Meeting Minutes

### Attendees

- Tony
- Gabriel
- Mike
- Adam
- Martha
- Isabela

### What are people working on

- Tony
    - Help using the extension cookiecutter
- Isabela
    - [Jupyter accessibility's governance status has changed](https://github.com/jupyter/governance/pull/129). Hooray and thanks for y'all's help! We're a subproject!
    - Testing updates. I want to share the [manual testing script work and template for feedback](https://github.com/jupyter/accessibility/pull/95).
    - [JupyterLab accessibility statement](https://github.com/Quansight-Labs/accessibility/pull/3). I'd like to go over and request feedback on this proposal statement. It'd also be good to think about how we propose this to JupyterLab.

### Next steps

- Follow up on subproject set up (Isabela)

## 6.29.22 Meeting Minutes

### Attendees

- Gabriel
- Tony
- Darian
- Sylvain
- Martha
- Nikhil
- Mike
- Tania

### What are people working on?

- Sylvain
    - [Codemirror 6 migration](https://github.com/jupyterlab/jupyterlab/pull/11638) is ready for testing, accessibility perspective and otherwise.
    - Please test it with the binder link in the PR! Feedback is extremely welcome! Please note CM6's accessibility doesn't seem to be clearly documented.
    - Known issues we will not be addressing: LaTeX syntax highlighting does not yet exist

- Isabela
    - JupyterLab accessibility statement approach
    - I'm going to be working on theming soon. What are your dream themes? (ie. ideal accessible themes)
    - :bulb: colour-blind friendly - as many as possible?!, selective contrast, address [Irlen syndrome needs](https://www.autism.org.uk/advice-and-guidance/professional-practice/irlen-syndrome), monochrome

- Gabriel
    - I haven't been doing much Jupyter-related accessibility work lately, but I have been trying to implement accessibility-related CI/CD for the upcoming new Quansight website (quansight.com and labs.quansight.org), and I have been a bit surprised (but not surprised) that some of this stuff isn't more plug-and-play. 
    - Quansight's new website is statically generated with Vercel. You might think that there would be some ready drop-in solution to run [pa11y-ci](https://github.com/pa11y/pa11y-ci) or [axe-core](https://github.com/dequelabs/axe-core) against the pages in your site, but so far I haven't found it.

- Nikhil
    - Haven't been working on Jupyter-specific accessibility tickets (although I would like to dive in), but have been working on data viz accessibility! Continuing some prior research I worked on during school (w/ Doug Schepers, Frank Elavsky) on auto-generating summaries using NLPfor complex/reactive charts/graphs and also diving more into sonification ([Highcharts](https://www.highcharts.com/docs/accessibility/accessibility-module)).
    - One of our research benchmarks: [Chart2Text: Generating Natural Language Explanations for Charts by Adapting the Transformer Model](https://github.com/JasonObeid/Chart2Text)
    - From @gabalafou: here's a [Colab using some sonification](https://colab.research.google.com/github/hassaku/colab-a11y-utils/blob/master/colab_a11y_util_example.ipynb)
     - https://allosphere.ucsb.edu/
     - https://astronify.readthedocs.io/en/latest/

- Mike
   - https://github.com/krassowski/jupyterlab-voice-control is now a thing, was demoed on previous JupyterLab meeting

### Next steps

- Collect requests for notebook and visualization standards in JupyterLab to figure out where that info may be best stored (Isabela)
- Create a list for requested JupyterLab accessible themes with status (Isabela)
- Update on static website testing set up (Gabriel)
- Watch the jupyter-lab-voice demo when it's on YouTube!

## 7.13.22 Meeting Minutes

### Attendees

- Tony - QLabs
- Balaji - Berkeley
- Ryan - Berkeley
- Allison - Berkeley
- Paul - Berkeley
- Sean - Berkeley
- Tania - QLabs
- Gabriel - QLabs
- Richard - Berkeley
- Isabela - QLabs

### What are people working on?

- Quick updates
    - Circle back on next steps for our subproject status: probably a council
    - Theming status - JLab 3.4.3 under review based on [this draft criteria](https://github.com/Quansight-Labs/accessibility/pull/9/files#diff-ae9e4a46a307e3234480f0684742137952fb1d181184643f8c52753f5f8579e1)
- Questions about JupyterLab accessibility status for use at UC Berkeley.
    - JupyterLab as a part of DataHub, needs to be accessible.
    - Interest in WCAG 2.0 AA alignment and figuring out how to collaborate.
    - If we do an audit now, can we show by [timeline is unclear]
    - Short term: classes deploying this before the end of the year
    - Long term: how do we sustain this work and these changes to avoid regression and ensure a solid experience.
    - [New campus committee will focus on digital accessibility - Berkeley News](https://news.berkeley.edu/2022/07/11/new-campus-committee-will-focus-on-digital-accessibility/)
    - [About Accessibility in Learning Tools - Berkeley Research, Teaching, and Learning](https://rtl.berkeley.edu)
    - [ARC Toolkit - TPGi](https://www.tpgi.com/arc-platform/arc-toolkit/)
    - [Tenon](https://tenon.io/)
    - [berkeley-dsep-infra/datahub image requirements](https://github.com/berkeley-dsep-infra/datahub/blob/staging/deployments/datahub/images/default/requirements.txt)

### Next steps

- Update meeting notes in jupyter/accessibility (Isabela)
- Bring up statement work with main JupyterLab team (Isabela)
- Follow up on subproject next steps (Isabela)
  - (+1 Nikhil - would love to learn more!)

  ## 8.10.22 Meeting Minutes

### Attendees

- Gabriel F. - Quansight Labs
- Ely - Bloomberg
- Ryan
- Martha
- Balaji - UC Berkeley
- Mike
- Richard
- Isabela
- Darian

### Agenda

- [Identify accessibility targets for Lumino 2 #341](https://github.com/jupyterlab/lumino/issues/341)
   - Mike: `silentNotifications` support - there is a stale PR which has an accessibility related utility function for announcing changes, maybe worth pulling into in lumino https://github.com/jupyterlab/jupyterlab/pull/9031 it looks like a similar effort was attempted years ago for: https://github.com/jupyterlab/jupyterlab/pull/6583
   - Changing divs to buttons? (+1 from Isabela on this)
   - Isabela: Does the labelling issue in [jupyterlab/jupyterlab #6581 Input fields in dialogs need to be labeled](https://github.com/jupyterlab/jupyterlab/issues/6581) have roots in Lumino?
   - [name=gabriel] is DataGrid used in JupyterLab? Darian: CSV viewer, variables viewer(?), pandas dataframes - basically anywhere you see the "spreadsheet" component
   - question from Ely about accessibility of canvas (because datagrid uses canvas)
       - Isabela mentions/asks about Google Docs and Canvas. Link from Mike: https://workspaceupdates.googleblog.com/2021/05/Google-Docs-Canvas-Based-Rendering-Update.html
   - [name=gabriel] what counts as API change beyond method names/signatures? 
       - response from Darian: for example, CSS is considered API because we don't make it private
- Circle back on next steps for our subproject status: probably a council
- Theming status - [JLab 3.2.0 partial (non-color) draft review](https://github.com/Quansight-Labs/accessibility/pull/9#issuecomment-1184017454). There's also been more indepth review on zoom behavior at [quansight-labs/jupyterlab-accessible-themes](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues).
- Convention to support alt text in notebooks - [github issue](https://github.com/jupyter/accessibility/issues/98)
    - Mike would like the ways that metadata gets used by tools like nbconvert for things like alt text to be standardized
    - Realted issue at [jupyter/accessibility #37](https://github.com/jupyter/accessibility/issues/37)
    - Some questions. Should this be a change done on a tool by tool level, or overall? If it is overall, what is the path?
        - Possibly a [Jupyter Enhancement Proposal](https://jupyter.org/enhancement-proposals/) to bring this into nbformat. Possibly the Jupyter Standards group. These will both be slower. There may be faster and just as good changes in nbconvert level.
        - What happens when you work on the individual output level versus the cell level (which may have multiple outputs).
        - Mike: IPython mimebundle adds `alt` to output metadata: https://github.com/ipython/ipython/blob/9ed8ecd64be967335ce7f098f67aa602a3f3383b/IPython/core/display.py#L1015-L1050
        - Mike: R  IRKernel does not add alt to image output metadata: https://github.com/IRkernel/IRdisplay/blob/master/R/display_images.r
        - Mike: width and height metadata are "codified": https://nbformat.readthedocs.io/en/latest/format_description.html#display-data
          - Darian: but not formally in https://github.com/jupyter/nbformat/blob/main/nbformat/v4/nbformat.v4.schema.json (which does not prevent the use of `width`, `height` nor `alt`)

### Next steps
- Circle back on next steps for our subproject status: start a council (Isabela)
- from Ryan "should there be a github issue in lab to measure/describe a11y issues with it’s current use of canvas?" Yes! (Isabela)
- Review DataGrid specifically to understand the work that would be needed to make it more accessible (start with a complicated component)

## 8.24.22 Meeting Minutes

### Attendees

- Darian
- Tony
- Gabriel
- Ryan
- Martha
- Isabela
- Allison

### Agenda

- Rendered notebook user testing has started! You can track that work-in-progress on the [iota-school/notebooks-for-all repo](https://github.com/Iota-School/notebooks-for-all)
- Lumino 2.0 accessibility 
    - Relevant links [lumino #341](https://github.com/jupyterlab/lumino/issues/341) and [jupyterlab #12992](https://github.com/jupyterlab/jupyterlab/pull/12992) and [lumino examples](https://lumino.readthedocs.io/en/latest/examples.html) and [Section 508](https://www.section508.gov/)
    - This is in alpha release at this point.
    - Lumino provides the top level menus, the command palette and search, the keyboard shortcut system, the dock panel (sidebars), and Widgets (a lot like react components but with different life cycle; more like building UI in Qt).
    - Some changes are low-level changes, like making sure that keyboard navigation is not inhibited. Lumino doesn't have a concept of the content in these widgets, so some changes that are content-specific do not belong there.
    - What's the status of where we are in evaluating any API-breaking changes or other issues?
        - DataGrids still seems the most potentially suspect. It does impact certain cell outputs, too, so this could be critical.
            - Probably the most sure-fire choice would be to provide an option to turn this off and render as a table. 
            - Maybe it's easier to review on Notebook and then we find those issues and then can evaluate wheter or not they are Lumino.
        - Where do ARIA labels or similar tags align with this work?
- Gabriel
    - A win! [lumino #373](https://github.com/jupyterlab/lumino/pull/373)

### Next steps

- Review Notebook 7 for accessibility as means of identifying Lumino changes and more. (Isabela + anyone interested) ([most recent review is](https://github.com/jupyter/accessibility/issues/7))

## 9.07.22 Meeting Minutes

### Attendees

- Darian
- Ryan
- Gabriel
- Martha
- Isabela
- Ely

### Agenda

- How do we want to set up the council? Background: the [governance bootstrapping docs](https://jupyter.org/governance/decision_making.html) don't account for the fact that we became a software project later and did not have existing steering council members to start our council process. We also need to have a council soon to nominate our representative to the new SSC soon.
    - Some options to create the starter group:
        - Add who has already voted in our most recent votes as the starter group.
        - Add whoever is in the GitHub organization as the starter group.
        - Add meeting attendees over a certain list of recent months as the starter group.
            - Maybe a number of regular attendance? But this shouldn't be the only thing because there are many valuable asynch contributions.
        - Darian: "has attended x number of times out of y number last meetings OR has voted in https://github.com/jupyter/accessibility/issues/81"
    - More setting up council to dos:
        - Council team compass
        - Github team
        - Mailing list (if wanted)
        - SSC representative
        - two-factor authentication
- Isabela
    - Reflow and Lumino?

### Next steps
- Isabela to set up starter group list for the council. Reach out to list of individuals.
- Isabela to post an issue about how we determine this starter group for transparency.
- Add PR to jupyter/accessibility when this starter group is formed. Then we can have the discussion about where things go without blocking this process.

## 9.21.22

### Attendees

- Darian
- Tania
- Gabriel
- Ryan
- Ely

### Agenda

- Discussing depth-levels in JupyterLab/lumino codebases
    - Example that sparked this conversation https://github.com/jupyterlab/jupyterlab/pull/13109
- Most recent Zoom audit in JupyterLab and findings https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/34
- Examples of manual-testing scripts we are working on https://github.com/Quansight-Labs/jupyter-a11y-testing/tree/main/testing/scripts
- Darian: is happy to offer office hours to help folks orient around the codebase
    - Ely: had plenty support from Jason when walking this path 
    - Ely: some helpful information was around panel, CSS, historical context (from Jason), panels needed for a particular situation
    - Provide examples of extensions with the panels/layout explanations (maybe in the readme in Lumino)
    - Tania: could we look at codetours for example? https://github.com/microsoft/codetour
- Adjacent: Tania proposed this docs reorg (JupyterLab) https://github.com/jupyterlab/jupyterlab/issues/7387
- Darian: proposal -> use some of these calls to do "BBQ bonanza/triage" -> find where the issue resides to help fixing this

## October 5 2022

### Attendees

- Jeremy (might not be able to attend)
- Frederic
- Mike
- Gabriel
- Isabela
- Allison
- Darian
- Frederic
- Martha
- Detroit
- Balaji
- Ryan

### Agenda

- Mike:
    - Shadow DOM
- Jeremy:
    - A new pre-release of Notebook 7 is available: https://github.com/jupyter/notebook/releases/tag/v7.0.0a6
    - Discourse topic: https://discourse.jupyter.org/t/notebook-7-pre-releases-are-available/16063
    - It includes the switch to **CodeMirror 6** that landed in JupyterLab: https://github.com/jupyterlab/jupyterlab/pull/11638
    - Closed the old issue on the RetroLab repo that was about doing an accessibility audit on the RetroLab UI: https://github.com/jupyterlab/retrolab/issues/80. Now that the CodeMirror 6 update is available in a Notebook 7 pre-release it should be possible to make this audit with a document-oriented notebook UI.
    - There is no development happening in `jupyterlab/retrolab` anymore, improvements and fixes should be done in JupyterLab and Notebook 7.
    - Happy to help in the `jupyter/notebook` or `jupyter/accessibility`. Please report any issue if you find any, thanks!
    - Try it on Binder with this gist: https://gist.github.com/jtpio/d368ab89cee5123ecee60683115e15f3

- Frederic
    - [Improvements of tab panel labelledby](https://github.com/jupyterlab/lumino/pull/407) - will be part of 3.5.0
    - Some related work with consistency of CSS variables between background color and text color:
        - [Link background colors and ui font colors in the style](https://github.com/jupyterlab/jupyterlab/pull/13173)  
        This was seen when working on a [JupyterLab theme editor](https://github.com/HaudinFlorence/jupyterlab-theme-editor)

- Mike v2:
  - low hanging fruit good first issue for new contributors https://github.com/jupyterlab/jupyterlab/issues/13045

- Isabela
    - Office hours follow up (from last meeting)?
    - Council updates?
    - [Browser zoom support](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html)— [(early) ideas for JupyterLab?](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/34#issuecomment-1228911639)

- Gabriel
    - If we have time for office hours, can we chat about tab focus indicators and/or tab traps in code cells?

### Next steps
- Shadow DOM needs more research and/or a binder to test it in
- Explore [Notebook 7](https://gist.github.com/jtpio/d368ab89cee5123ecee60683115e15f3). [Report Notebook 7 issues](https://github.com/jupyter/notebook/issues).
- Add "office hours" help for under agenda and make a queue of issues to pull from

## October 19 2022

### Attendees

- Mike
- Isabela
- Gabriel
- Stephannie
- Martha
- Gérard
- Tania
- Ryan
- Balaji
- Kseniya
- Israel

### Agenda

- Isabela 
    - Discussion on directions for high browser zoom and JupyterLab at [jupyterlab/jupyterlab #10004](https://github.com/jupyterlab/jupyterlab/issues/10004#issuecomment-1276957564). Please weigh in! 
        - Mike: Another approach would be to have UI and document zoom approached separately since it is possible they are different use cases.
        - Mike: "A datapoint for previous discussion: in VScode the default is to zoom everything and user needs to enable document zooming manually though they divide ctrl + scroll as it seems."
    - For anyone curious, here is what we did [on the collaborative keyboard navigation review for the Notebook 7 prerelease](https://github.com/isabela-pf/a11y-events/pull/10). It will become an issue elsewhere.

- Gabriel
    - Sneak peek on some of the work I'm doing. tl;dr-- Run accessibility regression tests via GitHub Actions against a JupyterLab PR, showing if it breaks (or fixes) any regression tests.

- Copy this to next meeting's agenda: For the remainining meeting time, can we open up and dig into CodeMirror? -Gabriel
[name=Tania] I am interested in this, mostly how can we "test" for the newly introduced accessibility features 

## November 2 2022

### Attendees

- Darian
- Gabriel
- Stephannie
- Isabela
- Martha
- Ely
- Ryan
- Mike
- Kseniya
- Balaji
- Tania

### Agenda
- Isabela
    - Update on Space Telescope user testing results. This [resources PR](https://github.com/Iota-School/notebooks-for-all/pull/26) provides all info used to plan the tests so far and script, notebook used, and takeaways from the first round of tests.
- Mike
   - nbdime? Keep an eye out for any PRs here because this could relate to the inaccessibility of the space. We should review any PRs with this in mind.
- Darian
    - Rick mentioned someone from UC Berkeley might contact us re: accessibility for Jupyter tools deployed there
    - Jupyter Executive Council election
- For the remainining meeting time, can we open up and dig into CodeMirror? -Gabriel
[name=Tania] I am interested in this, mostly how can we "test" for the newly introduced accessibility features 
    - https://github.com/berkeley-dsep-infra/datahub/issues/3885
    https://playwright.dev/docs/accessibility-testing

## November 16 2022
    
### Attendees

- Darian
- Gabriel
- Stephannie
- Isabela
- Tania
- Mark
- Detroit
- Ryan
- tf
- Sylvain
- Ely

### Agenda

- Special guest appearance: Katie
[name=Tania]- Since Darian mentioned an audit (potential) it would be definitely good to keep in sync and find a way to standardise our auditing processes in Jupyter-world

- Isabela
    - Update on Space Telescope [user testing results](https://github.com/Iota-School/notebooks-for-all/blob/main/user-tests/1-navigation/results.md). We have more complete takeaways from the first round of tests. If there's any interest in me sharing the results or answering questions, let me know!
    - For desired reflow in JupyterLab, please feel free to weigh in on [jupyterlab/jupyterlab #10004](https://github.com/jupyterlab/jupyterlab/issues/10004#issuecomment-1276957564). I'm trying to keep this moving forward and would like if we can get to a decided direction.
    - Regarding reflow Darian/Sylvain does any of you have ideas/suggestions on moving this forward and help land on a decision/path forward
        - [name=Gabriel] In response to this question, there was discussion and questions around Notebook 7 vs JupyterLab
- Sylvain
    - Notebook v7 audit by Balaji at UC Berkeley

## November 30 2022

### Attendees

- Mark
- Martha
- Gabriel
- JooYoung
- Tony
- Stephannie
- Mike
- Tania

### Agenda

- Gabriel
    - Discuss: "Jupyter Accessibility": 
        1. Group exercise: open your favorite search engine, type "Jupyter Accessibility"... where does it take you? what is the first thing you see? 
        2. Are we happy with this?
        3. If not, what do we need to do?
[name=Tania] - we need docs like https://code.visualstudio.com/docs/editor/accessibility for Lab and friends
[name=Mike] - Collect a list of extensions and themes for accessibility features see https://jupyter-accessibility.readthedocs.io/en/latest/#using-jupyter-software-with-assistive-technology
Comments included that we don't have user-focused documentation to point to. Even if they live on a per project basis, it makes sense to also have them here.
    - Some take-aways:
        1. Keep jupyter/accessibility as one repo. Don’t split into two repos (one for user-facing docs, one for team compass)
        2. Put sign posts for end users in jupyter/accessibility repo and website.
        3. Try to add accessibility docs to jupyter.org and/or JupyterLab ReadTheDocs
        4. Push forward the work done on the Accessibility statement, with an eye to providing useful info for disabled users.
        5. Think about restructuring current docs so that they address different users: contributors, end users, maintainers, and such.
        6. Repos that use the keyword accessibility but are incomplete or works in progress sohuld probably have some kind of WIP label and preamble.
    - Links:
        - [name=Mike] I opened a [PR to add link to accessibility docs on docs.jupyter.org](https://github.com/jupyter/jupyter/pull/665)
        - [name=Tania] [Point accessibility.jupyter.org to these docs?](https://github.com/jupyter/accessibility/discussions/109)

- Isabela
    - Summary of  Space Telescope user testing results for test 1: navigation. [Results slides](https://docs.google.com/presentation/d/1rSrPlK-dW49h0LorSTMEMpLRfOkR2aUak4HAHKAPjK8/edit?usp=sharing). [Full results](https://github.com/Iota-School/notebooks-for-all/blob/main/user-tests/1-navigation/results.md).
    - Want to fix the broken link to our old meeting notes? Help with [jupyter/accessibility #113](https://github.com/jupyter/accessibility/issues/113) is welcome!
    - I want to review and (if needed) update the [accessibility project board](https://github.com/orgs/jupyterlab/projects/1) soon. Is anyone interested in giving this a review as well? We can split issues up to save time.

## December 14 2022

### Attendees

- Min
- Darian
- Ryan
- tonyfast
- Blessing Ogoh
- Gabriel
- Isabela

## Agenda 

- Isabela
    - Calendar check. Is this our last meeting of the year?
        - [name=Gabriel] FYI, the JupyterLab team meeting on Dec 28 that precedes this one was cancelled.
    - Want to fix the broken link to our old meeting notes? Help with [jupyter/accessibility #113](https://github.com/jupyter/accessibility/issues/113) is welcome!
        - [name=Min] my first accessibility PR! https://github.com/jupyter/accessibility/pull/115
    - I want to review and (if needed) update the [accessibility project board](https://github.com/orgs/jupyterlab/projects/1) soon. Is anyone interested in giving this a review as well? We can split issues up to save time.

- Gabriel
    - In the meeting before this one, Florence from QuantStack demo'd a JupyterLab extension to edit the look and feel of JupyterLab.
    - [name=Ryan] Sounds like it could lead to accessible themes or maybe more accessible defaults
    - [name=Gabriel] Yes! but for me the key thing that interests me here in terms of accessibility for end users is empowering end users to customize the UI to their particular accessibility needs (high contrast, color blindness, large font, etc.)

- Min
    - Connecting Blessing, Outreachy intern working on accessibility in JupyterHub
    - Authentication, Spawning, Admin pages
    - Wave exposing existing color/contrast issues
        - How to make intentional design decisions 

- Darian
    - Wanted to open a PR against @steff456's [Lumino PR for collapsing menus](https://github.com/jupyterlab/lumino/pull/489)

- tony
    - Progress on navigating static notebooks after a recent round of tests.

## January 11, 2023

### Attendees

- Tony
- Gabriel
- Darian
- Isabela
- Mike
- Ryan
- Ely

## Agenda 

- Accessible tables with pandas output https://tonyfast.github.io/tonyfast/xxiii/2023-01-02-accessible-dataframes-basic-indexes.html

- Darian: I am reviewing [Stephannie's menubar collapsing PR](https://github.com/jupyterlab/lumino/pull/489)
    - darian is review this week.
    - it is hard to know the size of something before it is rendered
    - completer that measure width https://github.com/jupyterlab/jupyterlab/pull/13663  
- Mike:
  - should we try to turn on `screenReaderMode` in terminal (xterm.js) or is it fine to keep it off by default
  - does anyone has time to provide a review for https://github.com/jupyterlab/lumino/pull/477?
- [jupyterlab # 13704 cell role](https://github.com/jupyterlab/jupyterlab/issues/13704)
    - related reading: [aria-label is a code smell](https://ericwbailey.website/published/aria-label-is-a-code-smell/)

## Non-agenda
- What Gabriel is currently working on
    - JupyterLab PR: [Make file browser respond to focused elements #13577](https://github.com/jupyterlab/jupyterlab/pull/13577)
    - [Tab trap in JupyterLab notebook code cell](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/issues/168)
 - post meeting: I believe Darian asked during the meeting if someone had done some a11y testing of Google Colab. I found out later that Balaji Alwar did this, using a public notebook. Result is at https://user-images.githubusercontent.com/2306166/197913587-bbae1601-d0f4-436b-bd83-6d2ea8892753.png.

## January 25, 2023

### Attendees

| Name | Affiliation | GitHub | Favorite html tag |
| ------------------ | ----------- | ------------- | ------------------------------ |
| tony fast |  | @tonyfast | details |
| Tania Allard | Quansight Labs | @trallard | `<abbr>`|
| Stephannie Jimenez Gacha | Quansight Labs | @steff456 | |
| Martha Cryan | IBM | @marthacryan | |
| Gabriel Fouasnon | Quansight Labs | @gabalafou | `<script>` but doing this exercise, I learned about the `<progress>` tag |
| Michal Krassowski | Quansight | @krassowski | |
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf | `<p>` |
| | | | |

## Agenda 

* progress on testing static notebooks. [notebooks for all testing content](https://iota-school.github.io/notebooks-for-all/)
    * how we parameterize notebooks with the jupyter configs. 
* [rendering dataframes for screen readers with pandas](https://tonyfast.github.io/tonyfast/xxiii/2023-01-02-accessible-dataframes-basic-indexes.html)
    * https://adrianroselli.com/2017/11/a-responsive-accessible-table.html

## February 8, 2023

### Attendees

| Name | Affiliation | GitHub | Favorite aria role |
| ------------------ | ----------- | ------------- | ------------------------------ |
| tony fast |  | @tonyfast | [feed](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/feed_role) |
|william stein | SageMath, Inc | @williamstein | |
| a. t. darian | `quantstack` | @afshin | `complementary` |
| Gabriel Fouasnon | Quansight Labs | @gabalafou |  |
| Stephannie Jimenez Gacha | Quansight labs | @steff456 | |
| R Ely | Bloomberg | @ohrely | Olympia (Les Contes d'Hoffmann) |

## Agenda 

* [name=Gabriel] Possible office hours question: keyboard shortcuts registered via the JupyterLab command registry are handled on the capture phase, but I have always worked in apps that use bubbling. 
    * Why are keyboard shortcuts implemented how they are?
        * chord shortcuts were applied. it is a emacs feature. helps entice emacs users in jupyter.
        * support chords
        * css specificity
        * people implement their own keyboard action when it is not a command. 
            * use case: a mini list to make up down l r work.
    * How are keyboard shortcuts handled?
        * keyboard shortcuts are composed and executed by the command registry.
        * this happens at the lumino application layer.
        * [specificity versus matchability](https://github.com/jupyterlab/jupyterlab/blob/b7c241483ec8562eb2a836ebc86086d04597aa4a/packages/shortcuts-extension/src/index.ts#L51-L79)
* [name=william] A little motivated by Darian's comment last hour: I'm curious about the accessibility implications of being able to move buttons around in toolbars, reorder menus, etc.   It can be confusing because customization has a scope with web apps that is a lot different than say "photoshop".
* [name=tonyfast] semantic tags for notebooks and cells
    * Could a [rendered notebook (static HTML page) be described by aria role=feed](https://iota-school.github.io/notebooks-for-all/exports/Imaging_Sky_Background_Estimation-form-based.html)?

## February 22, 2023

### Attendees

| Name | Affiliation | GitHub | Favorite css property |
| ------------------ | ----------- | ------------- | ------------------------------ |
| tony fast |  | @tonyfast | font-size |
| Ryan Lovett | UC Berkeley | @ryanlovett | color |
| Sylvain Corlay | QuantStack | @SylvainCorlay| border-radius |
| Isabela Presedo-Floyd | | | |
| Martha Cryan | | | |
| William Stein | SageMath, Inc| @williamstein| box-shadow d|
| Kseniya Usovich | | | 
| R Ely | Bloomberg | @ohrely | all |
| Stephannie Jimenez Gacha | Quansight labs | @steff456 | |

### Agenda

- Isabela
    - Update on Space Telescope [user testing](https://github.com/Iota-School/notebooks-for-all/tree/main/user-tests#test-2-content-types). Results for test 2 are a work in progress.
    - I am also in the process of lining up JupyterLab-specific user testing. Stay tuned for that!
- Sylvain
    - Axe audit announcement & post.
    - Draft blog post: https://docs.google.com/document/d/1XpRuWqZVlPRHQzNzfP5K8G2fp6QQS288jP4vjSoWnOU/edit?usp=sharing
- Tony
    - UI conventions for error vs warning, etc.
    - What if a single Jupyter notebook cell were a form?  Motivation: there's a LOT of thought about accessibility of forms...

## March 8, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
| tony fast |  | @tonyfast |
| Isabela Presedo-Floyd | | |
| William Stein | SageMath | @williamstein |
| Stephannie Jimenez Gacha| Quansight Labs | @steff456 |
| Gabriel Fouasnon | Quansight Labs | @gabalafou |
| R Ely | Bloomberg | @ohrely |
| Blessing Ogoh| |@bl-aire |
| Mike | | @krassowski |

### Agenda

- William: I'm curious if you have any thoughts about what happens when the cursor is at the top (or bottom) of a markdown cell and you hit the up (or down) arrow.  It goes to the previous cell instead of "staying in that form element".  Is this bad from an accessibility point of view?  A user complained today about this behavior to me, prompting [this issue](https://github.com/sagemathinc/cocalc/issues/6526).   Same question makes sense for code cells.    (Context: could there be a general "accessibility mode" for Jupyter notebook where the entire approach to navigation is much more standard and accessible, but maybe more awkward for experts?)
   - User: "I expect arrow keys to only move the cursor in the current form that is being edited."
    - [codepen](https://codepen.io/tonyfast/pen/NWLpdrB)
    - [WAI](https://www.w3.org/WAI/ARIA/apg/patterns/)
    - Where to put accessibility configuration:
      - https://github.com/mozilla/readability
- Ely (if time): takeaways from Jupyter for Education Workshop
    * what format do professors provide students?
    * teaching and sharing formats are often not the same
    * export to html is common practice
    extensions help and cause problems
    * can fix things, but provide more code to be vulnerable to accessibility failings
    "slides in latex easier to read"
    * used to students saying "give me the source"
    * the need for alt text is there, but writing it is hard.
    * jupyter is the medium for teaching
- Isabela: Updates on JupyterLab accessibility user research. I'm still in the scheduling phase.

## March 22, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
| tony fast |  | @tonyfast |
| Ryan Lovett | UC Berkeley | @ryanlovett |
| William Stein | SageMath | @williamstein |
| Stephannie Jimenez| Quansight Labs | @steff456 |
| Gabriel Fouasnon | Quansight Labs | @gabalafou |
| Martha Cryan | IBM | @marthacryan |
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf |
| Michal Krassowski | | @krassowski |
| Sylvain Corlay | QuantStack | @SylvainCorlay |
| Afshin T. Darian | QuantStack | @afshin |
| Balaji Alwar | UC Berkeley | @balajialg |

### Agenda

- Isabela: Updates!
    -  JupyterLab accessibility user research. I'm still in the scheduling phase.
    -  Notebook authoring recommendations.
    -  STScI test two: content write up is on the horizon.
- Gabriel updates
    - [Adding automated Axe-core + Playwright testing to PyData Sphinx Theme](https://github.com/pydata/pydata-sphinx-theme/pull/1260)
    - The other big thing I'm working on is trying to find UX bugs in a somewhat high-risk PR I made against JupyterLab to [remove tab traps from the Notebook area](https://github.com/jupyterlab/jupyterlab/pull/14115).
        - One big functional change is that browser focus goes on cell wrappers rather than the notebook node itself. This functional change is reflected in a visual change: there is now a bold outline around the notebook cells as you move focus from cell to cell.
- [name=Tony Fast]
    - crash course of links of i presented at pycascades https://tonyfast.github.io/tonyfast/xxiii/2023-03-18-pycascades-ally-talk.html
    - axecon last week:
        - ibm equal access checker ci and extension https://github.com/IBMa/equal-access
            - combines multiple web and national standards
        - https://www.deque.com/axe-con/sessions/the-accessibility-to-burnout-pipeline/
- thoughts about jupyter accessibility
    - cells as forms in lumino
- Sylvain
    - More contributions upcoming
    - What is a good way to collect the work that's been previously done to stop it from getting lost and to help prioritize?
        - Having all the things that have been done collected is too large for the scope of the work coming up.
        - Just being responsive should be enough. (Isabela worries about sustaining this but okay.)
- Mike
   - [GitHub Copilot X](https://github.blog/2023-03-22-github-copilot-x-the-ai-powered-developer-experience/) (just dropped) got voice control; should I move [jupyterlab-voice-control](https://github.com/krassowski/jupyterlab-voice-control) to jupyterlab-contrib? enabling control via via more modalities would be neat

## April 5, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
| A. T. Darian | QuantStack | @afshin |
| Ryan Lovett| UC Berkeley | @ryanlovett |
| Gabriel | Quansight | @gabalafou |
| Ely | Bloomberg | @ohrely |
| Stephannie Jimenez | Quansight | @steff456 |
| Tania | Quansight Labs | @trallard |
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf |

### Agenda

- Tony: https://github.com/Iota-School/notebooks-for-all/pull/49 shows progress on a semantic html5 structure for notebook webpages. in this approach, we treat the rendered version of the notebook as an entire interactive web page.
    - please leave feedback on comments in the pull request
    - in this structure
        - the notebook occupies the `main` tag
            - the each cell is a row in a `table`
                - the cell is represented by form components
    -  this approach surfaces interactive elements like links, forms, and overflowing elements to drive focus. it gives a more meaningful navigation experience of rendered notebooks zoomed in, on a screen, and navigated with tabs.
    -  this representation could serve as a starting point for the proper roles and aria for interactive implementations to improve their accessible experience. 
- Isabela
    - Recruiting usability study pariticpants. More information and sign ups at [the Jupyter Discourse topic](https://discourse.jupyter.org/t/participate-in-a-jupyterlab-accessibility-study/18786). Please feel free to share it around.
    - [Space Telescope Day of Accessibility registration here](https://iota-school.github.io/day_accessibility/). This is a mostly in-person event with some virtual options.
- Gabriel's updates
    - [pydata-sphinx-theme #1260](https://github.com/pydata/pydata-sphinx-theme/pull/1260) - my PR to test PST with Playwright and Axe-core is in final rounds of review, should be close to merging. 
        - Next steps: expand tests to touch more parts of the theme, fix issues found, integrate with CI 
    - Hope to close my JupyterLab PRs before next accessibility meeting:
        - [jupyterlab #13577](https://github.com/jupyterlab/jupyterlab/pull/13577)
        - [jupyterlab #14115](https://github.com/jupyterlab/jupyterlab/pull/14115)
- P
    - [GCHQ in UK](https://www.gchq.gov.uk/). Working on accessibility here now! Wahoo! (Isabela wrote the Wahoo!)
    - Check out the PR at [jupyterlab/jupyterlab #14320](https://github.com/jupyterlab/jupyterlab/pull/14320).
    - ARIA work upcoming
- nick
    - [Encouraging Research on Open Knowledge Networks - NSF](https://beta.nsf.gov/funding/opportunities/encouraging-research-open-knowledge-networks)

## April 19, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
| A. T. Darian | QuantStack | @afshin |
| Ely R | Bloomberg | @ohrely |
| Stephannie Jimenez Gacha| Quansight Labs | @steff456 |
| Michal Krassowski | | @krassowski |
| Tania | Quansight Labs | @trallard |
| Ryan Lovett | UC Berkeley | @ryanlovett |
| tonyfast |  | @tonyfast |
| G. Vidal | ENS de Lyon| @g-vidal|
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf | 
| Balaji Alwar | UC Berkeley | @balajialg |

### Agenda

* turns out there are more guidelines beyond WCAG for authoring tools. <a href="https://www.w3.org/WAI/standards-guidelines/atag/"><abbr title="Authoring Tool Accessibility Guidelines">ATAG</abbr></a> are guidelines specific for accessible authoring experiences. ATAG is part of series of guidelines including WCAG and <a href="https://www.w3.org/WAI/standards-guidelines/uaag/"><abbr title="User Agent Accessibility Guidelines">UAAG</abbr></a>.
    * [We haven't talked about these since 2021!](https://github.com/jupyter/accessibility/blob/main/docs/community/meeting-minutes/jupyterlab-accessibility-meetings/all-minutes.md#061621-meeting-minutes)
* Chartability for ensuring that data visualizations, systems, and interfaces are accessible.  https://github.com/Chartability/POUR-CAF
* [Do No Harm Guide: Applying Equity Awareness in Data Visualization](https://www.urban.org/research/publication/do-no-harm-guide-applying-equity-awareness-data-visualization)
* Request for a place where we can track/compare different recommendations. Venn diagram-style?
* Interest in having a list of the status of different guidelines. ie. number out of total number guideline compliance per set.
* Isabela was working on a JupyterLab accessibility statement - think keeping that updated to report on effort would be a good step
* Isabela
    * Still recruiting usability study participants. More information and sign ups at [the Jupyter Discourse topic](https://discourse.jupyter.org/t/participate-in-a-jupyterlab-accessibility-study/18786). Please feel free to share it around.
    * [Draft: notebook authoring checklist](https://github.com/Iota-School/notebooks-for-all/blob/main/resources/event-hackathon/notebook-authoring-checklist.md). This will eventually be submitted to be linked in Jupyter repos as well.
* Gabriel
    * Merged :tada: [jupyterlab PR Make file browser respond to focussed elements #13577](https://github.com/jupyterlab/jupyterlab/pull/13577)
    * Merged :tada: [pydata-sphinx-theme PR Accessibility test Kitchen Sink with Playwright #1260](https://github.com/pydata/pydata-sphinx-theme/pull/1260)
        * follow ups: fixes, expand tests, better reporting
    * Not merged but working on today and getting close to taking out of draft mode: [jupyterlab PR Fix tab trap notebook cells #14115](https://github.com/jupyterlab/jupyterlab/pull/14115)
    * Preparing for [talk at JupyterCon about automated accessibility testing](https://cfp.jupytercon.com/2023/speaker/YW7ZDA/)
* Stephannie
    * Organizing [accessibility docs plan](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/issues/196) - happy to hear thoughts about them
    * [Jupyter accessible themes](https://github.com/Quansight-Labs/jupyterlab-accessible-themes)
* Mike
  * Long-term planning: idea for [Accessible (and higher-performance) icons #14402](https://github.com/jupyterlab/jupyterlab/issues/14402)
  * Good-first issue: [Styled input checkbox focus state is not visible on Ubuntu/Firefox #14354](https://github.com/jupyterlab/jupyterlab/issues/14354)
* Nick
    * [NVDA (screen reader) uses robot testing](https://github.com/nvaccess/nvda/blob/master/tests/system/robot/chromeTests.robot). We might benefit from following their lead.

## May 3, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
|  tonyfast |  |  @tonyfast |
|  Ryan Lovett | UC Berkeley | @ryanlovett |
| Ely | Bloomberg  | @ohrely |
| Gabriel | Quansight | @gabalafou |
| Stephannie Jimenez Gacha |  Quansight Labs | @steff456 |
| Gérard Vidal |  ENS de Lyon| @g-vidal |

### Agenda

* SSC + EC update contents (Ely)
    * Quanstack worked toward accessibility testing compliance https://blog.jupyter.org/improving-the-accessibility-of-jupyter-6c695db518d3
    * Quansight developed a theming extension with varying accessible themes  https://github.com/Quansight-Labs/jupyterlab-accessible-themes - Defines a set of JupyterLab themes compliant to WCAG color standards. Currently we have color blindness friendly themes!
    * 400% Zoom audit - some fixes had already been included in both JupyterLab and Lumino 
    * Notebook 7 audit 
    * Notebooks for all is a collaboration with the Space Telescope Science Institute that  in including disabled people in the testing of Jupyter notebooks and improvements in notebooks accessibility. https://github.com/Iota-School/notebooks-for-all
    * [Gabriel] At Quansight Labs, we had an intern working on JupyterLab and accessibility and she wrote a [blog post about her internship](https://labs.quansight.org/blog/zoom-a11y-jupyterlab)
    * [Gabriel] Added some accessibility regression tests (tab traps, focus visible), working on making easy-to-use GitHub actions to run accessibility tests,  incubating at [Quansight-Labs/jupyter-a11y-testing](https://github.com/Quansight-Labs/jupyter-a11y-testing)
    * What is our group's purpose?
        * Consistency, fostering advocacy
    * What we want to say
        * Put accessibility concerns earlier (a11y in the planning phase)
            * and consider at every phase of development
        * We recognize that this is not simple to scope, but neither is security
        * Funding for events to teach developers about accessibility 
        * What happens if Jupyter fails to close accessibility gaps and ed institutions are forced to not use it?
* Gabriel's update:
    * Took a PR out of draft mode that [removes tab traps from the Notebook widget](https://github.com/jupyterlab/jupyterlab/pull/14115)
        * On the PR there is a [discussion about how to style focus indicators on the code cell](https://github.com/jupyterlab/jupyterlab/pull/14115#pullrequestreview-1409130132)
        * [Tony] https://www.sarasoueidan.com/blog/focus-indicators/
## May 17, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
|  tonyfast |  |  @tonyfast |
| stephannie Jimenez Gacha | Quansight | @steff456 |
|  nick bollweg |  Georgia Tech |  @bollwyvl |
| Afshin T. Darian | QuantStack | @afshin |
| Ryan Lovett | UC Berkeley | @ryanlovett |
| T | GCHQ | @t03857785 |
| Michal Krassowski | Quansight | @krassowski |

### Agenda

add any agenda items or topics in the list below.

* Jupytercon executive council meeting
  * a cool experience. 6 executive members and software steering council members in a hot room.
  * 4 minute update about the project progress we collectively discussed last meeting.
  * darian: There is a positive feeling on this subproject and the things we want to deliver
  * meaningful amount of funding
    
    put your ideas in the list below. use the community workshop submission structure.
    
    * Review of accessibility issues reported and if they are still live how to replicate
    * Pay for topics or audits for specific components
    * Use money to solve problems start to finish
    * Community building workshops
    * Fix some 400% zoom issues! We already have an audit with some tasks that can be done.
    * Documentation on accessible features in both the user and developer side.
* Stephannie
    * Notebook authoring guide docs - https://github.com/jupyter/accessibility/pull/127
    * WCAG & ARIA intro - https://github.com/jupyter/accessibility/pull/126
* t03857785
    * Added PR 14560 to add HTML dialog and 14561 to improve text spacing on home page
       * [summary of the discussion on `dialog` tag and targetting the PR](https://github.com/jupyterlab/jupyterlab/pull/14560/files#r1196880141)
    * Not able to work on the [notebooks for all project](https://github.com/Iota-School/notebooks-for-all) but will work on supporting elements if possible
    * https://github.com/jupyterlab/jupyterlab/pull/14560
      * has long term impact because of the base class it effects.
      * PR can be modified to remove the dialog base class for the moment if useful
    * https://github.com/jupyterlab/jupyterlab/pull/14561
    * Next issues on list are 400% zoom and keyboard navigation of menus with good aria prompts
* nick
  * informing the jupyterlab5/notebook8 roadmap
  * POUR CAF https://github.com/Chartability/POUR-CAF

tf: What does accessibility mean to you all?
  * Use of Microsoft Narrator. Close eyes and follow along and see if it makes sense.
  * tf: would be good to know what screen reader / assistive device is being used. tag in issues?

tf:
  - https://www.asha.org/public/speech/disorders/aac/

## May 31, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
|  tonyfast |  |  @tonyfast |
| T & P | GCHQ | @t03857785 |
| Isabela | Quansight Labs | @isabela-pf |
| Gabriel | Quansight Labs | @gabalafou |
| Ryan | UC Berkeley | @ryanlovett |
| Blessing | | @bl-aire|
| Mike | Quansight | @krassowski |
| Tania | Quansight | @trallard |
| Andrii | AWS | @andrii-i |

### Agenda

* t03857785
    * We are continuing to work on full keyboard access and 400% zoom then will move onto aria labelling and contrast to support additional requirements
    * Tania: dropping the link to the Zoom audit findings and suggested fixes from a few months back https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/34
    * Fix skiplink and add placeholder for additional skiplinks https://github.com/jupyterlab/jupyterlab/pull/14597
    * elements respond to enter or spacebar https://github.com/jupyterlab/lumino/pull/590/
    * Added "tabindex=0" for sidebar accessibility https://github.com/jupyterlab/lumino/pull/583
    * changing focus is needed for skip links 
      * how do i focus the left/right panel? Make something active (or choose active element) then focus
      * setting active is seperate from focus and current, active does not update focus. Changing focus is a two step process.
* Isabela
    * [JupyterLab accessibility study](https://discourse.jupyter.org/t/participate-in-a-jupyterlab-accessibility-study/18786) has been run. I'm handling logistics and working on a wrap up.
    * Space Telescope and rendered notebooks accessibility [most recent study results are up as a PR](https://github.com/Iota-School/notebooks-for-all/pull/56).
* Gabriel
    * Updates since last meeting I attended:
        * Gave a [talk at JupyterCon about accessibility testing](https://cfp.jupytercon.com/2023/talk/8N3PZX/)
        * Created new [JupyterLab test for focus visible](https://github.com/Quansight-Labs/jupyter-a11y-testing/pull/33)
        * As part of getting test in #33 (above) to pass, I've been working on some focus issues with the Lumino MenuBar.
    * I have found a document titled [Developing a Keyboard Interface
](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/) from the ARIA Authoring Pratices Guide (APG) to be useful.
* cell semantics - https://github.com/Iota-School/notebooks-for-all/pull/63
* Link from Nick: [1EdTech Guidelines for Developing Accessible Learning Applications](https://www.imsglobal.org/accessibility/accessiblevers/sec3.html)
* Andrii
    * Notebook 7 is close to release, there are still 14 open accessibility problems in issue #6800 (https://github.com/jupyter/notebook/issues/6800). We need to identify which one of them (if any) should be release blockers. During the notebook call we defined release blockers as problems that prevent people from using major features of the Notebook. 

Links to open accessibility PRs that we discussed during call (overtime):
* https://github.com/jupyterlab/jupyterlab/pull/14597
* https://github.com/jupyterlab/jupyterlab/pull/14400
* https://github.com/jupyterlab/jupyterlab/pull/14561
* https://github.com/jupyterlab/lumino/pull/590
* https://github.com/jupyterlab/lumino/pull/477

Note (Gabriel): I think we will want to stick as close to the UI/UX patterns defined in the [ARIA Authoring Practices Guide (APG) Patterns](https://www.w3.org/WAI/ARIA/apg/patterns/) when making changes to Lumino or JupyterLab

## June 14, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
|  tonyfast |  |  @tonyfast |
| T & P | GCHQ | @t03857785 |
| Gabriel | Quansight Labs | @gabalafou |
| Ely | Bloomberg | @ohrely |
| Andrii | AWS | @andrii-i |
| Afshin T. Darian | QuantStack | @afshin |
| Stephannie Jimenez Gacha | Quansight | @steff456
| Mike | Quansight | @krassowski | |
| Tania Allard | Quansight Labs | @trallard | 
| Balaji| UC Berkeley | @balajialg |

### Agenda

* Andrii
    * Thank you everyone for the feedback on https://github.com/jupyter/notebook/issues/6800, really appreciated, helps us prioritize work
        * Next step would be splitting 6800 into separate issues. If someone has bandwidth, help would be much appreciated
        * (Gab) I pretty much volunteered myself to do this in yesterday's triage meeting
* t03857785
    * Thanks for feedback on PRs @fcollonval really helpful, looking at moving [skiplinks](https://github.com/jupyterlab/jupyterlab/pull/14597) to a dialog so it takes it out of widget layout any tips concerns would be useful
    * We are going to review and resubmit a couple of our outstanding PRs following some lessons learnt any idea when 4.0.x will be released as we want to do a pass of everything together to find the gaps
    * Initial [400% zoom changes](https://github.com/jupyterlab/jupyterlab/pull/14626) are in PR any feedback welcome
      * Tania - we should be able to share some findings on keyboard navigation from some paid user testing sessions Isabela led (with disabled folks) in the upcoming couple of months. Repo with our user-testing env https://github.com/Quansight-Labs/JupyterLab-user-testing

* Gabriel's updates since May 31
    * Reviewed many (but not all) open PRs tagged with accessibility
    * Watched a bunch of [videos to better understand Lumino architecture](https://youtu.be/GCp4lxOblxg)
    * Engaged in discussion with Tony and Darian yesterday during the Rethinking Notebook Cells meeting about making the HTML output of the JupyterLab notebook widget (also used by Notebook 7) more semantic and accessible

Discussion: how do we make a better experience for newcomers?

* (Ely suggestion) A scripted intro to the meeting
  * More structure to the meetings
* (t03857785 feedback) Spending more time creating accessibility issues and marking them as "good first issues"
* (t03857785 feedback) It would be helpful to know how to navigating the code base and knowing what a good change looks like
* add links to beginner resources (and issues) at top of HackMD
  * Link to issues filtered by "accessibility" and "good first issue", rather than maintaining a list
* Exemplary issues - 
  * dialog issue is a good example
* (Tania elaboration) responding to G&T's feeback about navigating the codebase. This has been the hardest and longest part of onboarding developers. Not sure 
* (Ely) drawing attention to comment left by Mike in chat: "Good first issues in lab usually have a link to codebase e.g. https://github.com/jupyterlab/jupyterlab/issues/14354"
  * Something for us to keep in mind: maybe we don't need to solve the a11y issue in front of us, but to give enough context for somebody else to solve it, and then we move on to work on other, harder issues
  * On context and issues (Mike): this is >relatively< easy to fix for new "good first issues" by modifying triage docs saying that triage team should add the links and context before labelling as "good first issue"
* Discussion around having quarterly workshops
  * Ely suggests making the logistics as automateable as possible, so for example have it be the first Wednesday of each quarter, so that sending out announcements and the like can be automated
  * (Gab) Keep in mind the difference between "recruiting" versus "onboarding" (workshops may address issue of recruiting more than onboarding)
* (Tania) raises point that HackMD is bad for screen reader users. (P&T) echoes point. 
  * Sounds like Google Docs may be better alternative?
  * Tania - I hear Etherpad is a good alternative 
* Meet next week to begin a community proposal for accessibility. 
  * Add an event to the calendar 
  * Announce in the lab meeting
* https://github.com/jupyterlab/team-compass/issues/199

## June 21, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
|  tonyfast |  |  @tonyfast |
| Blessing Ogoh | | @bl-aire |

### Agenda

* https://github.com/jupyter/notebook/issues/6800
* screen reader workshop https://www.youtube.com/watch?v=F189lurxSbs&list=PLCPZgcYzVpj_WHHCTUpec8THYEMzXZnR1&index=6
* Sylvain 
  * funding for keyboard navigation
  * keyboard navigation issues below
    * https://github.com/jupyter/notebook/issues/6935
    * https://github.com/jupyter/notebook/issues/6931
    * https://github.com/jupyter/notebook/issues/6928
    * https://github.com/jupyter/notebook/issues/6925
* a goal is to figure out community events
  * GCHQ - accessibility means different things to different people
    * concern is that things can go backwards.
      * https://jupyter-accessibility.readthedocs.io/en/latest/
      * https://www.w3.org/WAI/people-use-web/user-stories/
  * bug bash would be supported
  * like a security policy, what is the accessibility 
  * [What does accessibility mean in jupyter?](https://docs.google.com/document/d/1m5-fiqWVdlqOuKjp4auakG0MMaTii7JdCVyjwKU7uQU/edit#heading=h.w3dl0bbc0ba5)
  * [Day of Accessibility Proposal] w iota school

## June 28, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
|  tonyfast |  |  @tonyfast |
| Gabriel | Quansight | @gabalafou |
| Stephannie Jimenez Gacha | Quansight | @steff456 |
| T & P | GCHQ | @t03857785 |
| Ryan Lovett | UC Berkeley | @ryanlovett |
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf |
| A. T. Darian | QuantStack | @afshin |
|Tania Allard | Quansight Labs | @trallard |

### Agenda

* tony 
  * proto issue for notebook v7 remediations to improve the quality of the annotation object model https://tonyfast.github.io/tonyfast/xxiii/2023-06-21-v7-aom.html
* jupyterlite will be helpful in testing the screen reader experience.
  * maybe a prerelease before notebook release
  * this is not a blocker, but a really nice to have.
* Gabriel's updates
    * I have had discussions on how to move forward my [PR #14115 to fix tab traps in the notebook widget](https://github.com/jupyterlab/jupyterlab/pull/14115)
    * I have been in [conversations with Tony and Darian on how to instrument research findings](https://github.com/jupyterlab/team-compass/issues/182) from Notebooks for All to JupyterLab and Notebook 7.
      * An issue to [optionally build Jupyter Notebook off of JupyterLab PRs](https://github.com/jupyterlab/jupyterlab/issues/14767)
    * Result of those discussions: @afshin and @gabalafou (me) will be working on [Implement ARIA recommendations from Notebooks for All #14765](https://github.com/jupyterlab/jupyterlab/issues/14765)
    * Question: where should the branch/PR for the above issue live? I started a [tiny bit of notebook ARIA code](https://github.com/jupyterlab/jupyterlab/compare/main...gabalafou:jupyterlab:notebook-aria?expand=1)
        * Answer: [Improve Notebook ARIA #14768](https://github.com/jupyterlab/jupyterlab/pull/14768) based off my 
    * Opened a [PR to apply @fcollonval's suggestions](https://github.com/t03857785/jupyterlab/pull/1) to fix @t03857785's JupyterLab PR #14597: [Fix skiplink and add placeholder for additional skiplinks ](https://github.com/jupyterlab/jupyterlab/pull/14597)
    * Spent a lot of time thinking about and wrote up my thoughts about [the past, present, and future of the skiplink in JupyterLab](https://github.com/jupyterlab/jupyterlab/pull/14597#pullrequestreview-1490421505) 
 * t0385778
     * Thanks to @gabalafou for the PR approved and merged
     * Need consideration on how to move skiplinks forward command palatte seems a good approach to build on
     * 400% zoom https://github.com/jupyterlab/jupyterlab/pull/14766 created as https://github.com/jupyterlab/jupyterlab/pull/14626 broke when syncing should be ready for merging once approved
     * Keyboard navigation https://github.com/jupyterlab/lumino/pull/590 is complete apart from running "yarn run api" 
 * open an issue about building notebook v7 on jupyterlab prs
   * this will help testing changes in notebook through lab
   * Tania volunteered to help with this -> Darian will tag Tony and Tania on the issue

## July 12, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
| T & P | GCHQ | @t03857785 |
| Afshin T. Darian | QuantStack | @afshin |
| Stephannie Jimenez Gacha | Quansight | @steff456 |
| R Ely | Bloomberg | @ohrely |

### Agenda

* t0385778
    * Following PRs are open it would be great to get these merged as well as tht latest version of lumino into Jupyterlab asin combination they cover a significant amount of keyboard and zoom accessibility
        * [400% Zoom screen usability enhancements - Updated](https://github.com/jupyterlab/jupyterlab/pull/14766/)
        * [Keyboard navigation right sidebar shortcut command](https://github.com/jupyterlab/jupyterlab/pull/14799)
        * [elements respond to enter or spacebar](https://github.com/jupyterlab/lumino/pull/590)
        * [Fix skiplink and add placeholder for additional skiplinks](https://github.com/jupyterlab/jupyterlab/pull/14597)
        * [Alt text and marking elements decorative](https://github.com/jupyterlab/jupyterlab/pull/14819)
    * We are working on 
        * Status bar keyboard accessibility and usability at high zoom
        * Screen reader compatibility with keyboard navigation 
        * Aria announcements for command palette executions
* [Community events](https://docs.google.com/document/d/1m5-fiqWVdlqOuKjp4auakG0MMaTii7JdCVyjwKU7uQU/edit?usp=sharing)
* What Gabriel has been up to:
    * [Improving focus handling in Lumino menu bar](https://github.com/jupyterlab/lumino/pull/607)
    * [Fixing tab traps](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/issues/134)
    * Reviewing [JupyterLab accessible themes](https://github.com/Quansight-Labs/jupyterlab-accessible-themes) by Stephannie
    * Reviewing [JupyterLab user testing results](https://github.com/Quansight-Labs/JupyterLab-user-testing/pull/10) by Isabela
* Action item: [Notebook v7 announcement](https://github.com/jupyter/notebook-team-compass/issues/24) - everyone please take a look at it for messaging around accessibility and weigh in if you have thoughts

## July 26, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
| Gabriel | Quansight Labs | @gabalafou |
| T & P | GCHQ | @t03857785 |
| tonyfast | | @tonyfast |
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf |
| A. T. Darian | QuantStack | @afshin |
| R Ely | Bloomberg | @ohrely |

### Agenda

* Gabriel's update: finishing up deliverables for [CZI JupyterLab accessibility grant](https://jupyter-accessibility.readthedocs.io/en/latest/funding/czi-grant-roadmap.html), which is coming to an end. This includes pushing forward on [fixing tab traps](https://github.com/Quansight-Labs/jupyter-a11y-mgmt/issues/134), [fixing focus management](https://github.com/jupyterlab/lumino/pull/607) in the Lumino menubar, finishing up a [focus visible regression test](https://github.com/Quansight-Labs/jupyter-a11y-testing/pull/33), and [creating accessibility docs](https://github.com/jupyterlab/jupyterlab/pull/14426).
* Isabela
    * [JupyterLab user testing results are up for review.](https://github.com/Quansight-Labs/JupyterLab-user-testing/pull/10). Once merged I'll pass a PR over to [jupyter/surveys](https://github.com/jupyter/surveys) as well for continuity.
    * [Notebooks for all (STScI) user testing results have a PR to add to jupyter/surveys](https://github.com/jupyter/surveys/pull/26). 
    * I'm working on getting the Notebooks for all (STScI) proposal document into jupyter/accessibility's proposal directory so we keep building references for funding accessibility work in Jupyter.
    * I spoke about accessibile notebook authoring recommendations at SciPy (conference). The recording is supposed to be up shortly. You can have [the slides](https://docs.google.com/presentation/d/1LBcEOGhZfLXCaGAWUaGl4c6O5AXBBXzfoA9dV0W-5Pc/edit?usp=sharing).
    * [JupyterLab accessibility statement PR](https://github.com/jupyterlab/jupyterlab/pull/14856)
* T & P and Tony
    * Community event updates
    * Looking for review on [What does accessibility mean for Jupyter?
A Jupyter Community Event proposal
](https://docs.google.com/document/d/1m5-fiqWVdlqOuKjp4auakG0MMaTii7JdCVyjwKU7uQU/edit#heading=h.ksli8dqlx0ec)
* T & P
    * Following PRs are open it would be great to get these merged as well as tht latest version of lumino into Jupyterlab asin combination they cover a significant amount of keyboard and zoom accessibility
        * [400% Zoom screen usability enhancements - Updated](https://github.com/jupyterlab/jupyterlab/pull/14766/)
        * [Keyboard navigation right sidebar shortcut command](https://github.com/jupyterlab/jupyterlab/pull/14799)
        * [Fix skiplink and add placeholder for additional skiplinks](https://github.com/jupyterlab/jupyterlab/pull/14597)
        * [Alt text and marking elements decorative](https://github.com/jupyterlab/jupyterlab/pull/14819)
		* [Made Status bar accessible at 400% zoom](https://github.com/jupyterlab/jupyterlab/pull/14854)
    * We are working on 
        * Screen reader compatibility with keyboard navigation 
        * Aria announcements for command palette executions
    * Note
        * [CSS Style Validator](https://github.com/jupyterlab/jupyterlab/pull/14795) may cause some issues with complex CSS for accessibility notes in ticket on a workaround
* Ely
    * (Special?) meeting time that works for Gabriela
        * Perhaps we can move this meeting to 9am Pacific on Thursdays every other week (and alternating with Jupyter Server contributing hour), Darian will raise this issue at tomorrow's Jupyter Server and Kernels call
* blog post
  * testing is ill defined. we need to work on our definitions
  * [Gab] trying to integrate feedback from Isabela, I'm guessing that probably the blog post needs messaging around the idea that, okay, here we are down the line, we've closed a bunch of accessibility-labeled PRs in a Notebook 7 milestone that came out of auditing the software, but that does not ladder up to certainty that the software is for sure more accessible (without user feedback and user testing)

## August 10, 2023

### Attendees

| Name | Affiliation | GitHub |
| ---- | ----------- | ------ |
| Afshin T. Darian | QuantStack | @afshin |
| Blessing || @bl-aire |
| Mike | Quansight | @krassowski | |
|Stephannie Jimenez| Quansight |@steff456|
| R Ely | Bloomberg | @ohrely |
| T & P | GCHQ | @t03857785 |
|Johnson|Qaunsight|@dannyjohnson2050|
| Gabriel | Quansight Labs | @gabalafou |
| Isabela Presedo-Floyd | Quansight Labs | @isabela-pf |

### Agenda

* Ely
    * Open Studio Day!
        * https://go.bloomberg.com/attend/invite/jupyter-open-studio-day-august2023/
* Isabela
    * If we have time, I'd like to ask for a little more info on the motivation behind [the draft event proposal](https://docs.google.com/document/d/1m5-fiqWVdlqOuKjp4auakG0MMaTii7JdCVyjwKU7uQU/edit?usp=sharing).
        * Tania (not attending, this time is challenging for me): I reviewed this. First thank you for working on this. I'd also appreciate knowing more about the motivation as I do not have clarity and that reflects on the comments.
    * [JupyterLab user testing results are up for review in jupyter/surveys.](https://github.com/jupyter/surveys/pull/27) Looking for review and merge.
    * 🎉[Notebooks for all (STScI) user testing results have been merged to jupyter/surveys](https://github.com/jupyter/surveys/pull/26). 
    * 🎉The [Notebooks for all (STScI) proposal document is public](https://github.com/Iota-School/notebooks-for-all/blob/main/resources/proposal-astronomy-notebooks-for-all.md). I have a [PR open to add it to jupyter/accessibility's proposal directory](https://github.com/jupyter/accessibility/pull/136). Looking for review and merge.
    * 🎉[JupyterLab accessibility statement has been merged](https://github.com/jupyterlab/jupyterlab/pull/14856).
* Gabriel
    * I've cleared my plate of required deliverables from my job, so I should have a little more self-directed time over the next few weeks.
    * JupyterLab keyboard brainstorming 
        * Seeking input on organizing a group video chat
    * Some stuff I've been working on:
        * Adding a [dev-focussed accessibility page to the JupyterLab docs](https://github.com/jupyterlab/jupyterlab/pull/14426)
        * Moving along [Lumino menu bar focus/hover PR](https://github.com/jupyterlab/lumino/pull/607)
        * Testing above PR against a focus visible test so took the [focus-visible test PR](https://github.com/Quansight-Labs/jupyter-a11y-testing/pull/33) out of draft mode
* [notably inaccessible](https://arxiv.org/abs/2308.03241)
* **T & P**
    * PRs remain open be great to get some more merged
    * Looking at adding tests for
        * 400% zoom
        * keyboard navigation
        * high contrast visibility 
* **Johnson** 
    * I wanted to make mention on the work I've done on the ["accessibility section in the user JupyterLab documentation"](https://github.com/jupyterlab/jupyterlab/issues/14396) and the progress myself and Stephannie are making on the project.
* Mike
    * Should JupyterLab have "accessibility" settings plugin for things we do not want as default?
