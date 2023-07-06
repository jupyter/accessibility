# Notebook 7 Keyboard Navigation Audit

## Background and Overview

Keyboard navigation is a vital aspect of Web accessibility for many disabled users with motor and vision disabilities. The main objective of this functionality is to allow users to use Web interfaces by only using a keyboard.

By default, there should be an alternative from a standard mouse for navigating Websites. WCAG standard states that all the content needs to be navigable without a specific keyboard timing. The recommendations from the W3C include using the `Tab` key for forward navigation and `Shift+Tab` for backward navigation. Other important and most common used keys include `Space`, `Enter` and the arrow keys.

On the eve of the pre-release of Notebook 7 in the Jupyter ecosystem a keyboard navigation audit event was performed. The following document states the methodology, results and recommendations found in the audit.

## Methodology

The notebook interface has a lot of interactions, widgets and functionalities. The main goal for this event was for participants to learn how to perform and describe foundational tests for keyboard navigation. Each participant chose a WCAG criteria to focus the audit.

The UI was divided in 11 areas, menu bar, files panel, new/upload/refresh buttons, search bar, breadcrumbs, columns of the file browser, file browser, running panel, file editor, notebook toolbar and the notebook cells. The participants where surveyed regarding the keyboard navigation in the following categories: `content order`, `areas to navigate`, `keyboard/tab traps`, `skip links`, `focus`, `mixed input` and `keyboard shortcuts`.

Each of the areas was tested by the participants searching for [keyboard tab traps](https://www.w3.org/TR/WCAG22/#no-keyboard-trap) and [skip links](https://www.w3.org/TR/WCAG22/#bypass-blocks). The methodology used was to start from the beginning of the area and start using the `Tab` key until the end of the area. Then, record the behavior and flag any blockers.

## Findings

The major findings are listed below,

### Content order

In the file browser

- The full order of the content isn't clear because of limited visible focus styling.
- There are unknown focus areas where the user needs to use the tab key multiple times in a row to continue to the next section without visual feedback where they are. We're not sure if this will be solved by visible focus styling or if they content order is jumping somewhere we don't expect.
- Files tabs, Running tabs, and File sorting UI (like Name and Last Modified ordering) are skipped over with keyboard navigation.

### Areas to navigate

- Navigating through the menu bar with a keyboard "leaves incorrect lm-mod-active class on last active item"
- Notebook toolbar excess items cannot be navigated to with a keyboard
- Leaving the active file editor with a keyboard must be done with the esc key. This isn't standard keyboard navigation behavior.
- JupyterLab cannot switch between split areas Keyboard shortcuts for navigating panes

### Keyboard/tab traps

- Terminal is a major tab trap. Could only escape by using the command palette shortcut.
- Notebook editor (like other file editors) and consoles must be exited with the esc key. This isn't standard keyboard navigation behavior.
- Could not open new terminal with the Running tab using the keyboard. Only expands and collapses.
- "If I hide the header (command palette, untoggle "Show Header"), I still tab through the hidden element?"
- "Please check focus reset after Command Palette -> Find... -> Escape to exit out. I would expect focus to go back where I was prior to the command palette (e.g. in a specific cell editor)."

### Skip links

- There does not appear to be a skip link in either the file tree page or the notebook page. There should be skip link(s) to skip over menu bar(s), straight to main page content

### Focus

- There is visible focus in some areas, but it is not applied throughout. Some areas have blue outlines.
- Sometimes a user is able to see focus because of an area's hover state, but these areas need a true focus state additionally.
- "The behavior of hovering/colors/interactions is not the same doing it by the keyboard than doing it with the mouse." Meaning different interactive area states are not always triggered by keyboard focus?

### Mixed input

In the file browser,

- "Could not select/unselect file using only keyboard. Multi-select and unselect is also busted"

### Keyboard shortcuts

- Shortcuts cannot be turned off
- Shortcuts cannot be remapped/configured (via the UI)

## Overall recommendations

Each item in the findings can be described as it's own issue. Given that the goal for keyboard navigation is to remove all the keyboard traps and create skip links to ease the amount of keys needed to be pressed to move from one block to another.

## References

If you are interested in reading the full audit and be part of the discussions please refer to the following issues and pull requests,

- [Notebook 7 keyboard navigation review: October 12](https://github.com/isabela-pf/a11y-events/pull/10/files)
- [Notebook 7 prerelease keyboard navigation review](https://github.com/jupyter/notebook/issues/6595)
- [Keyboard navigation workshops](https://github.com/isabela-pf/a11y-events/tree/main/workshop-resources/keyboard-navigation)
