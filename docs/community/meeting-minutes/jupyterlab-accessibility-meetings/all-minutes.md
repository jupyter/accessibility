# All JupyterLab Accessibility Meeting Minutes

This file collects all the separate note files into one place to make it easier to skim the notes or search for topics. It is organized oldest to newest.

## 09.30.20 Meeting Minutes

### Attendees

- Martha (@marthacryan )
- Max (@telamonian )
- Karla (@karlaspuldaro)
- Alek
- tony (@tonyfast)
- Alex (@ajbozarth)
- Isabela (@isabela-pf)

### Notes

#### Say hello!

Introduce yourself however you like. What do you want to get from
this meeting?

- Our group has limited experience with accessibility work previously.
  We are all learning. Hooray!
- No one here uses a screen reader or other assistive software.
- Should we do outreach to have people involved who use this?
  Probably. Find a way how.

#### Why this meeting? Why now?

- Multiple JupyterLab team meetings where we discuss people's
  interest in making JupyterLab accessible, but those interested
  don't know where to start (both in learning about accessibility
  and wrangling JupyterLab).
- Let's be resources for each other! Share skills, knowledge,
  and morale.
- 3.0 release plans to have a lot of added features, 4.0 might
  be a good time to push for improving what is already there.
  - yes definitely, no way is this getting in 3.0

#### What goals do we have?

- WCAG specifications. Let's review them and figure out how to
  implement them. - https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines - We reviewed this document to start getting on the same page.
- Get different people involved. Get people who actually use
  accessibility features/ screen readers/ assistive software. - Avoid single point of failure problems. Community engagement
  needs to be done together.
- Are consoles a good place to start? Some older consoles are
  established and already have accessible affordances for us to
  start working with.
- - Another resource exploring what a typically inacessible
    experience (web comics) can be like with affordances.https://comica11y.humaan.com/
    (comics use cells too… :eyes:)
- https://design.chicago.gov/accessibility/tools/
- Need a plan to reviewing/getting feedback on JupyterLab as is and
  the changes we make. Can't just rely on accessing disability
  communities because it's our responsibility to fix it.

#### What are people working on?

- Max

  - accesible slider Widget
    - PR: https://github.com/jupyterlab/jupyterlab/pull/9104
    - probably a one-off, not really reusable in current form
  - `LabButton`

    - fully accesible replacement for current blueprint-based
      `Button` in @jupyterlab/ui-components
    - working on PR, hopefully have an initial stab done by the
      meeting
    - based on
      - https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/button_role
      - https://www.w3.org/TR/wai-aria-practices-1.1/examples/button/button.html
      - https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button#Accessibility_concerns
    - tricky part: the button text

      - the reccommendation: always use an HTML button element,
        always label like <button>text</button>
      - for icon buttons (eg all of our toolbar buttons), the
        suggestion is to hide the text using CSS
      - [example CSS](https://css-tricks.com/places-its-tempting-to-use-display-none-but-dont/)

        ```css
        .hide {
          position: absolute !important;
          top: -9999px !important;
          left: -9999px !important;
        }
        ```

        or

        ```css
        .visuallyhidden {
          position: absolute;
          overflow: hidden;
          clip: rect(0 0 0 0);
          height: 1px;
          width: 1px;
          margin: -1px;
          padding: 0;
          border: 0;
        }
        ```

      - seems convoluted, can we just use
        [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques/Using_the_aria-label_attribute)
        (this is exactly what it's for)? [Opinions seem mixed](https://developer.paciellogroup.com/blog/2017/04/what-is-an-accessible-name/)

  - I need resources to finish hashing out the styling system for the
    `LabFoo` components
  - bigger picture: as concrete problems arise (like the text vs
    aria-label thing for LabButton), we should use them as a jumping
    off point to seek outside expert opinion/help

- Isabela (and tony, Gonzalo, Eric)
  - Color contrast https://github.com/jupyterlab/jupyterlab/issues/8832

#### Next steps

- Do we want to share these notes somewhere (team-compass)?
- Martha and Max working on UI components (LabButton?)
  - Alek might help too!
- Spend an hour introducing everyone to JupyterLab UI so we
  understand what we are working with and start identifying places
  to work with it. (Do this later when people have done some
  exploration first)
- Removing UI components based on blueprint
- Reach out to Chris Holgraf, Tania Allard, and Jason Grout about
  contacts we've made in this area already (tony)
- Find and share resources (everyone)
- Settings UI (Alex). Will start after JupyterCon. Needs
  accessibility reveiw for the design.
- Meet every other week (twice a month).

## 10.21.20 Meeting Minutes

### Attendees

- Max @telamonian
- Isabela @isabela-pf
- Martha @marthacryan
- Alex @ajbozarth
- Jason Grout @jasongrout

### Notes

#### Logistic check in

- Does this time seem like it will keep working? Yes.
- If so I’d rather schedule it further out and add it somewhere
  more public so people can drop in. I can bring this up in JLab
  team meeting too, if so.

#### Proposed Goals

We'd like to propose concrete accessibility goals would be so that
we can organize it into JupyterLab's release cycle and encourage
people to focus on them. These are some ideas of where to start.

- Max brought up screen readers. Find most common and start from
  that paradigm.
  - discussion on github: https://github.com/jupyter/accessibility/issues/14
- Keyboard accessibility.
- Closing accessibility issues that already exist. There's already
  been work pointing out some of the issues (like here
  https://github.com/jupyterlab/jupyterlab/issues?q=is%3Aissue+is%3Aopen+web4all)
- Can we produce guidelines/docs/resources (or something similar)?
  This might help other people get involved and make the effort more
  sustainable.
- Creating an actionable plan and possibly getting some grant
  money/full time help

#### What are people working on?

Isabela

- Reached out to Tania Allard and Chris Holdgraf. They made point
  to keep all discussions online, so there shouldn’t be anything we
  are missing. Haven’t heard from Tania. This just means I’m trying
  to collect and understand what has already happened so we don’t
  redo or overlook existing work.
- Here’s some common places these discussions live (in Jupyter):
  - Jupyter Discourse accessibility Category https://discourse.jupyter.org/c/special-topics/accessibility/29
  - Jupyter accessibility repo https://github.com/jupyter/accessibility
  - JupyterLab accessibility issue label https://github.com/jupyterlab/jupyterlab/issues?q=is%3Aopen+is%3Aissue+label%3Atag%3AAccessibility
  - Jupyter Notebook accessibility issue label https://github.com/jupyter/notebook/labels/tag%3AAccessibility
  - JupyterHub accessibility issue label https://github.com/jupyterhub/jupyterhub/labels/accessibility
- Accessibility resource doc. WIP. Please feel free to add so we can
  help each other learn. Don’t let it get in the way of doing other
  work, but add as you find useful things. https://docs.google.com/document/d/12cusZV0j91yZTty_BQndorwTIgRloKR7WEWP2aGNp5A/edit?usp=sharing

#### Next steps

- Install NVDA or JAWS and gain familiarity with screen readers
  in general as well as JupyterLab
- Isabela needs to triage existing JupyterLab issues so we can
  assign/move forward with them
- Try and reconvene hackathon group to make sure we are understanding
  the same issues and have proper context to move forward and not
  repeat work that's already been started.
- Explore Phosphor and Lumino accessibility issues and PRs. This
  might be the metaphorical root of a lot of our problems. - Big PRs in the DOM and menu system that started but did not
  get finished
- Look for grants for funding a full-time accessibility dev
- Schedule meeting with Jason catching us up on work that's been
  done in Phosphor
- Explore Firefox accessibility tools. They've been recommended
  as a good starting point.

## 11.04.20 Meeting Minutes

### Attendees

- Martha @marthacryan
- Max @telamonian
- Alex @ajbozarth
- Jason @jasongrout
- Isabela @isabela-pf

### Notes

If needed, recap/point to the notes and resources for our Phosphor
PR meeting last Monday for people who weren't able to make it.

- Covered what decisions were made and our current goals (transfer
  the problems we already know about in Phosphor to Lumino and finish
  off what was originally Hack4All work).

Are these meetings something we'd want to have on the Jupyter
community calendar?

- Yes! It will be brought up in next week's JupyterLab team meeting
  for approval/necessary steps.

- Need to see if we can find or get data on what developers who use
  screen readers use in terms of OS

#### What are people working on?

- Martha: [#129](https://github.com/jupyterlab/lumino/pull/129) -
  Moved PR from phosphor to lumino, reviewers?
- Gonzalo: Following up on Phosphor tutorial videos. Confirmed we
  can repost them, but need to get license. - Also need a PR for Lumino docs once the videos get set up.

#### Next Steps

- Alex: Review [#129](https://github.com/jupyterlab/lumino/pull/129)
  Add isToggleable command state.
- Gonzalo: Get final info about reposting Phosphot tutorial videos
  for Lumino docs
- Isabela: Move Phosphor issues to Lumino. Also consolidate issues
  from other repos where relevant so we don't have to look for issues
  across as many repos anymore.
- Goal
  - Once those three Phosphor PRs are fully up and ready to be
    reviewed/merged, then we can reach out to experts to talk more.
  - Potentially asking for a meeting where we watch experts
    test PRs so we can learn how to better test too (and not just
    rely on them).

## 11.18.20 Meeting Minutes

### Attendees

- Martha @marthacryan
- Karla @karlaspuldaro
- Alex @ajbozarth
- Max @telamonian
- Jason @jasongrout
- Thomas @manfromjupyter
- Isabela @isabela-pf

### Notes

- Welcome Thomas!

#### What are people working on?

- Martha

  - PRs [jupyterlab/lumino#129](https://github.com/jupyterlab/lumino/pull/129)
    and [jupyterlab/lumino#131](https://github.com/jupyterlab/lumino/pull/131) merged!
    -Hooray for Martha! Great job getting that done!

- Max

  - Requesting review on [jupyterlab/lumino#132](https://github.com/jupyterlab/lumino/pull/132)
    rebasing for lumino.

- Isabela
  - PR for JupyterLab color contrast updates at
    [#9335](https://github.com/jupyterlab/jupyterlab/pull/9335).
    This means it has a binder to test. Original issue is
    [#8832](https://github.com/jupyterlab/jupyterlab/issues/8832)
  - Started sorting through the web of repos where accessibility
    work was started as issues (based on Phosphor Walkthrough
    meeting notes). Nothing to show yet.

#### Next Steps

- Martha will test her PRs with NVDA.
- Martha will make an issue for isToggleable additions to
  [#9365](https://github.com/jupyterlab/jupyterlab/issues/9365).
  Will also start working on it.
- Max will update [jupyterlab/lumino#132](https://github.com/jupyterlab/lumino/pull/132)
  with the items on the checklist. - Also create a binder.
- Thomas will review JupyterLab and perform an audit of all/most of
  the accessibility issues needing to be addressed to ensure an
  optimal user experience for all users with visual, auditory,
  ambulatory, or cognitive handicaps. Goal will be to uncover all
  that is needed to become fully WCAG 2.1 compliant. Will be using
  JAWS for the screenreader when a screenreader is necessary, but
  reported issues will be for all of them, not screenreader specific. - Setup following https://jupyterlab.readthedocs.io/en/latest/developer/contributing.html - maybe `pip install —pre jupyterlab` - Post issues to [jupyterlab repo](https://github.com/jupyterlab/jupyterlab)
  with [accessibility label](https://github.com/jupyterlab/jupyterlab/issues?q=is%3Aissue+is%3Aopen+label%3Atag%3AAccessibility).
- Isabela will consolidate the accessibility issues across repos
  where appropriate (probably [jupyterlab](https://github.com/jupyterlab/jupyterlab)
  or [lumino](https://github.com/jupyterlab/lumino)). Will bring the
  new issues for the next meeting so we can keep moving forward with
  the problems we already know about.

## 12.02.20 Meeting Minutes

### Attendees

- Tony @tonyfast
- Max @telamonian
- Jason @jasongrout
- Alex @ajbozarth
- Karla @karlaspuldaro
- Gonzalo @goanpeca
- Martha @marthacryan
- Thomas @manfromjupyter
- Darian @afshin
- Isabela @isabela-pf

### Notes

- There are overlap in infrastructure needs for an accessible
  JupyterLab and mobile/tablet support for JupyterLab. Maybe this
  is an opportunity to get more people involved in this work since
  there have been a lot of requests for mobile/tablet support.

Triage of existing accessibility issues
**This will be cross-referenced, updated with #9399, and stored
in this [project](https://github.com/orgs/jupyterlab/projects/1)
from here on out.**

- Reviewed from [diagram-codesprint/phosphor](https://github.com/diagram-codesprint/phosphor),
  [diagram-codesprint/jupyterlab](https://github.com/diagram-codesprint/jupyterlab),
  [phosphorjs/phosphor](https://github.com/phosphorjs/phosphor/),
  [jupyterlab/lumino](https://github.com/jupyterlab/lumino/), and
  [jupyterlab/jupyterlab](https://github.com/jupyterlab/jupyterlab/labels/tag%3AAccessibility)
  ([jupyter/accessibility](https://github.com/jupyter/accessibility/issues) has been more organizing focused).
- Isabela proposes continuing to focus on what was found in Hack4All first.
  - [#6577](https://github.com/jupyterlab/jupyterlab/issues/6577)
  - [#6578](https://github.com/jupyterlab/jupyterlab/issues/6578)
  - [#6579](https://github.com/jupyterlab/jupyterlab/issues/6579)
  - [#6580](https://github.com/jupyterlab/jupyterlab/issues/6580)
  - [#6581](https://github.com/jupyterlab/jupyterlab/issues/6581)
  - [#6582](https://github.com/jupyterlab/jupyterlab/issues/6582)
  - [#9365](https://github.com/jupyterlab/jupyterlab/issues/9365) Follow up for jupyterlab/lumino #129 that applies isToggleable to JLab now that it is possible with Lumino (Martha started this!)
- Issues Isabela wants to look into more

  - JLab [#6575](https://github.com/jupyterlab/jupyterlab/issues/6575)
    (update of diagram-codesprint/jupyterlab #8) Has merged PR #6359, but
    didn’t close the issue.
  - JLab [#6576](https://github.com/jupyterlab/jupyterlab/issues/6576)
    (update of diagram-codesprint/jupyterlab #9) and [#6404](https://github.com/jupyterlab/jupyterlab/issues/6404) Looks like a reference for UX of these accessibility changes and proposed solutions.
  - JLab [#1095](https://github.com/jupyterlab/jupyterlab/issues/1095)
    Visual/additional/any cues for running commands (this was to be put
    to phosphor, review if it was already done or not)
  - JLab [#911](https://github.com/jupyterlab/jupyterlab/issues/911)
    An audit issue about what seems to be the first JLab
    accessibility review. I need to check if they are or need to be
    represented in other issues.
  - diagram-codesprint/phosphor [#2](https://github.com/diagram-codesprint/phosphor/pull/2)
    and [#3](https://github.com/diagram-codesprint/phosphor/pull/3)
    status. Did they get merged into Phosphor ever?
  - diagram-codesprint/jupyterlab [#4](https://github.com/diagram-codesprint/jupyterlab/pull/4)
    and [#11](https://github.com/diagram-codesprint/jupyterlab/pull/11) status.
    Did they ever get merged into JupyterLab?

- Other issues
  - [#6573](https://github.com/jupyterlab/jupyterlab/issues/6573)
    NVDA tests on JLab. (Not explicitly tied to Hack4All, but seems
    like it was part of it.)
  - [#4878](https://github.com/jupyterlab/jupyterlab/issues/4878)
    Older screen reader evaluation with good discussion. Has been
    mentioned in a few issues and PRs so it would probably be good
    to brush up on.

#### What are people working on?

- Max and Jason
  - [jupyterlab/lumino#132](https://github.com/jupyterlab/lumino/pull/132)
    still needs review.
- Thomas
  - Opened [#9399](https://github.com/jupyterlab/jupyterlab/issues/9399)
  - This is a full review of JupyterLab accessibility, can be
    broken up into other issues as we go.
  - Evaluation is on JLab v.2.26 This should catch a lot of
    what holds over to 3.0, but we will be facing new problems
    with virtual notebook.
  - We started discussing how we pull this apart to tackle it
    - Tabs/tab order are the blockers that prevent further
      evaluation, so they should be high up on our list
    - Order top to bottom should work in order of what are
      most critical and/or rely on one another
  - This is a great review! Thank you so much!
- Isabela
  - Collecting and triaging existing issues as listed above.

#### Next Steps

- Max created a project to track JupyterLab accessibility work
  https://github.com/orgs/jupyterlab/projects/1. This will be how
  we organize and keep track of work in the future.
- Isabela and Tony will compare and consolidate #9399 with
  pre-existing issues. - Isabela also needs to check for duplicate issues and
  close/update as needed. - Triage marking by WCAG standard and maybe level of complexity?
- Martha #9365 applying isToggleable to JLab now that it is
  possible in Lumino is still happening. This will be her next step.
- Time to reach out to experts and say we want to meet in the
  future (also gives us a deadline for some of the commitments)

## 12.16.20 Meeting Minutes

### Attendees

- Tony Fast @tonyfast
- Jason Grout @jasongrout
- Gonzalo Peña-Castellanos @goanpeca
- Martha Cryan @marthacryan
- Sam Kacer @SamKacer
- Thomas @manfromjupyter
- Alex @ajbozarth
- Max @telamonian
- Isabela @isabela-pf

### Notes

- This is the [project for tracking accessibility
  work](https://github.com/orgs/jupyterlab/projects/1). We are still
  figuring out permissions, and this is a work in progress pulling
  over the past triaging work. When 3.0 is out, we want to convert
  the cards into a concrete road map.
- Recommended resource [WAI ARIA authoring practices](https://www.w3.org/TR/wai-aria-practices-1.1/)
- Thomas thinks there are a magic few lines of code that would be
  easy to get in JupyterLab before 3.0 and could make a big difference.
  Posted (and linked above) at [#9491](https://github.com/jupyterlab/jupyterlab/issues/9491)
  (formerly team-compass #114).

These discussions have identified four main accessibility needs
for JupyterLab (can probably be extended to other Jupyter projects
too)

- Making JupyterLab accessible for a read-only type experience
  - This is the focus of the report on [#9399](https://github.com/jupyterlab/jupyterlab/issues/9399)
- Making JupyterLab accessible for an interacting/coding experience
- Adding JupyterLab docs for accessibility features
  - Sam gave an anecdote about help pages in docs that lists
    help and resources for screen reader users.
- Adding CI or relevant accessibility tests to the JupyterLab
  contributing workflow ensure accessibility remains a priority - Referenced pydata-sphinx-theme [#292](https://github.com/pandas-dev/pydata-sphinx-theme/issues/292)
  and https://github.com/pandas-dev/pydata-sphinx-theme/runs/1507397117?check_suite_focus=true - nteract has some kind of accessibility CI they use
  (probably focused on react)

#### JupyterLab Code Editor

Our main focus today is the accessibility of JupyterLab's code
editor as discussed in [#4878](https://github.com/jupyterlab/jupyterlab/issues/4878)
and the comments of [#9399](https://github.com/jupyterlab/jupyterlab/issues/9399).

- What steps do we want to take?

  - We will be shipping jupyterlab 3 before the end of the year.
    Changing the default editor would be difficult before 4.0
    because of the number of things that have started to rely on
    CodeMirror.
  - Start with an extension based approach. To take action now
    and eventually fit it in to the release cycle as a part of core.
  - What editor should we start working with?
    - Sam confirms codemirror 6 is working better so far,
      especially better than we have now.
    - Based on the [JupyterLab Monaco Plugin](https://github.com/jupyterlab/jupyterlab-monaco),
      is it possible/relatively simple thing to bring that up to
      date and test how it would work with the editor now.
    - Sam still prefers monaco based on current usage.

- Where does this fit on our priority list/who can work on this?
  One potential path: 1. Get monaco editor extension up to date. 2. Review how that works with screen readers in JLab now. 3. Set up a way to quickly and easily install the extension
  (link for screen readers at top of JupyterLab?) and immediately
  use it to test screen reader accessibility in JupyterLab. 4. Prepare the extension to be a part of core JupyterLab for
  the next release.

- Sam's next priority (after editor) would be the toolbar

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
  - codemirror 6 talk about accessebility: http://bofh.nikhef.nl/events/FOSDEM/2021/D.javascript/codemirror.webm
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
  - Tony shares https://technica11y.org/designing-and-coding-for-low-vision and https://www.w3.org/WAI/tutorials/page-structure/content/
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
  - Playwright? [blog post](https://www.yunier.dev/2021-03-13-accessibility-testing-with-playwright/)
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
    - Work is in progress ([there](https://github.com/JohanMabille/jupyterlab/tree/codemirror)). CodeMirror6 introduces a completly new API that brings some challenge. So Johan is focusing on having a first draft PR without carry too much about styles/modes and extensions. So people can start to test it and we will be able to evaluate what work is remaining (in particular if some CodeMirror extensions needs to be ported from 5 to 6).
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
    - [doit automation file](https://pydoit.org/task_args.html) https://github.com/jupyter/accessibility/blob/master/dodo.py
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
  - Feel free to reach out to me on [gitter](https://gitter.im/gabalafou) or email me gfouasnon@quansight.com
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

- How do we want to set up the council? Background: the [governance bootstrapping docs](https://jupyter.org/governance/bootstrapping_decision_making.html) don't account for the fact that we became a software project later and did not have existing steering council members to start our council process. We also need to have a council soon to nominate our representative to the new SSC soon.
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