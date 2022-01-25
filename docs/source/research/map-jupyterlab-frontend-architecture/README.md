# Mapping JupyterLab's user interface to source code

Author: Gabriel Fouasnon

Date: January 18, 2022

## Introduction

The purpose of this document is to help orient frontend developers to the
JupyterLab codebase.

Required reading for this document is the sequence of pages in the JupyterLab docs
beginning with [General Codebase
Orientation](https://jupyterlab.readthedocs.io/en/latest/developer/repo.html).


### Source code versions

This document contains a large number of links to specific lines of code.
Because JupyterLab is constantly evolving and changing, it's important to peg
the links to specific code versions.

For JupyterLab code links, we use
[v4.0.0a18](https://github.com/jupyterlab/jupyterlab/tree/v4.0.0a18) for this
document.

For links to Lumino source, we use
[v2021.12.13](https://github.com/jupyterlab/lumino/releases/tag/v2021.12.13).


### Scope

JupyterLab loads a large number of front-end components into its default user
interface. This document does not attempt to exhaustively map all parts of the
interface to the source code. Rather it focuses on a subset of the UI.

### Approach

This document is organized by actual DOM nodes in the browser that JupyterLab
creates. Each section below covers a single node. In general, as you go from
beginning to end, the nodes become more and more deeply nested.

### Lumino and JupyterLab

JupyterLab is built on top of Lumino. In other words, Lumino is a dependency of
JupyterLab but JupyterLab is not a dependency of Lumino. Lumino provides a set
of classes for creating common UI elements, such as tab bars, menus, panels, and
more. Lumino also provides an architecture for plugins.

Every UI element in JupyterLab ultimately inherits from the Lumino Widget class.
A widget in Lumino is essentially what is sometimes called a frontend component
in other libraries. It's a class that wraps a DOM node, providing a piece of the
UI.

### Point of entry

It's hard to say where exactly the point of entry is for an application as big
and complex as JupyterLab, but for our purposes, it's `new JupyterLab().start()`
in [lines 177-191 of
jupyterlab/staging/index.js](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/jupyterlab/staging/index.js#L177).

The [JupyterLab
class](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/lab.ts#L17)
inherits from [JupyterFrontEnd
class](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/frontend.ts#L40),
which in turn inherits from [Lumino
Application](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/application/src/index.ts#L112).

The JupyterLab class constructor [creates a LabShell
instance](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/lab.ts#L24)
if one is not passed in. [LabShell is defined in
packages/application/src/shell.ts](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L255),
which is a key file to understanding how the JupyterLab UI is laid out. The base
Lumino Application class [points `this.shell` to the LabShell
instance](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/application/src/index.ts#L129),
so `lab.shell` is the root Lumino widget in the hierarchy of Lumino widgets.
Within the JupyterLab source code, you will often see it referred to as
`app.shell`.

The [start method is defined in the Application
class](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/application/src/index.ts#L383).
For each plugin that has been registered, it [calls activate on that
plugin](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/application/src/index.ts#L267),
passing in the plugin's declared requirements to the activate function. In
JupyterLab, plugins are defined in packages that have -extension at the end of
the name. For example, mainmenu-extension [defines a plugin that adds the main
menu
bar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu-extension/src/index.ts#L133)
to the JupyterLab interface.

## DOM Nodes

The rest of the document maps DOM nodes in the JupyterLab UI to related points
of interest in the source code. Each section represents a single DOM node.


### Application shell


The application shell is the entire user interface of the application. It
includes the top, bottom, and side bars, as well as the main content area (and
other areas not covered by this document).

![Screenshot of the JupyterLab UI in which the entire UI is outlined because the
shell node spans the entire visible UI](annotated-ui-screenshots/shell.png)

Node-to-node CSS selector path for this node:

    html > body > div#main

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [main](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L262) |
| CSS class | [jp-LabShell](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L261) |
| Controlling class | [LabShell](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L255) extends [Widget](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/widget.ts#L38) |

Steps to mount:

1. [Create new app
   shell](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/lab.ts#L24)
2. [Start
   app](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/jupyterlab/staging/index.js#L191)
3. Within the start method, [invoke the attach shell
   method](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/application/src/index.ts#L408)
4. [Attach shell to
   DOM](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/application/src/index.ts#L452).
   In a default JupyterLab instance, the shell node will be appended to the end
   of the document body.


### Top container


The top area includes the Jupyter logo and the main menu bar (File, Edit, View,
etc).

![Screenshot on which the top container of the JupyterLab UI is
outlined](annotated-ui-screenshots/top.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-top-panel

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-top-panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L303) |
| HTML role | [banner](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L283) |
| Controlling class | [PanelHandler](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1577), a private class that wraps [Lumino Panel](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/panel.ts#L24) |
| Shell area | [top](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L770) |


Steps to mount:

1. [Create handler for top
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L282).
   When the handler is created, a [new Lumino Panel is
   created](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1636).
2. [Create layout for app shell
   widget](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L299)
3. [Add top panel to
   layout](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L388)
4. [Assign layout to shell
   widget](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L397).
   This invokes [the Lumino Widget layout
   setter](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/widget.ts#L265),
   which in turn invokes [the parent setter for
   BoxLayout](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/layout.ts#L87)
   which it inherits from Layout. This in turn calls the [initialization method
   of the
   BoxLayout](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/panellayout.ts#L182),
   which it inherits from PanelLayout. The init method attaches the widget.
5. Assigning the layout [attaches the top panel to the
   DOM](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/boxlayout.ts#L165)


### Middle container


The middle node contains everything (nearly) between the top and the bottom
areas: the left sidebar, the main document area, and the right sidebar. (Not
covered in this document: it also contains the Log Console when it's displayed.)

![Screenshot on which the middle container of the JupyterLab UI is
outlined](annotated-ui-screenshots/middle.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel


Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-main-content-panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L305) |
| Controlling class | [Lumino BoxPanel](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/boxpanel.ts#L22) |


Steps to mount:

1. [Create new box
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L286)
2. [Add middle box panel to shell
   layout](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L389)

The rest of the steps for mounting the middle container are like the steps in
mounting the top container.


### Bottom container


The bottom area contains the status bar.

![Screenshot on which the bottom container of the JupyterLab UI is
outlined](annotated-ui-screenshots/bottom.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-bottom-panel

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-bottom-panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L304) |
| HTML role | none |
| Controlling class | [Lumino BoxPanel](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/boxpanel.ts#L22) |
| Shell area | [bottom](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L756) |


Steps to mount:

1. [Create new box
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L284)
2. [Add bottom panel to shell
   layout](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L390)

The rest of the steps for mounting the bottom container are like the steps in
mounting the top and middle containers.


### Logo


The Jupyter logo appears in the top area.

![Screenshot on which the logo is outlined](annotated-ui-screenshots/logo.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-top-panel > div#jp-MainLogo

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-MainLogo](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application-extension/src/index.tsx#L1044) |
| Controlling class | [Lumino Widget](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/widget.ts#L38) |


Steps to mount:

1. [Ask shell to add logo to top
   area](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application-extension/src/index.tsx#L1045)
2. The shell [passes the logo to its top
   handler](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1271)
3. The top handler [passes the logo to its Lumino
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1594)
4. The panel [passes the logo to its
   layout](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/panel.ts#L68)
5. The panel layout [mounts the logo to the
   DOM](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/panellayout.ts#L87)


### Top menu bar container


The menu area contains the main menu bar (File, Edit, View, etc).

![Screenshot on which the top menu bar container is
outlined](annotated-ui-screenshots/top-menu-bar-container.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-top-panel > div#jp-menu-panel

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-menu-panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L302) |
| HTML role | [navigation](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L280) |
| aria-label | [main](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L281) |
| Controlling class | [PanelHandler](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1577), a private class that wraps [Lumino Panel](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/panel.ts#L24) |
| Shell area | [menu](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L766) |

Steps to mount:

1. [Create new handler for menu
   area](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L279)
2. [Add menu area handler to top
   handler](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L429).
   Note: this applies only in multiple document mode, which is the default; we
   do not cover single document mode in this doc.

The menu area handler is then mounted with the top handler (see steps for
mounting top container, above).


### Left sidebar

![Screenshot on which the left sidebar is
outlined](annotated-ui-screenshots/left-sidebar.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div[aria-label="main sidebar"]

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | none |
| CSS classes | [jp-mod-left](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L312) |
| HTML role | [complementary](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L321) |
| aria-label | [main sidebar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L313) |
| Controlling class | [Lumino TabBar](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/tabbar.ts#L43) |


Steps to mount:

1. [Create handler for left side
   bar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L297).
   The [left handler creates a new Lumino
   TabBar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1647).
2. [Add the tab bar to the middle
   container](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L368)

This node gets attached to the DOM with the middle container (see steps to mount
the middle container, above).


### Main vertical split panel


This node allows the area inside of the UI that is surrounded by top, bottom,
and side bars to be divided into two top and bottom parts. This appears to be
primarily for providing a place to display the Log Console, which this document
does not go into.

![Screenshot on which the main vertical split panel is
outtlined](annotated-ui-screenshots/main-vsplit-panel.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel > div#jp-main-vsplit-panel

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-main-vsplit-panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L306) |
| Controlling class | [RestorableSplitPanel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L2061) extends [Lumino SplitPanel](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/splitpanel.ts#L30) |


Steps to mount:

1. [Create vertically split
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L287).
2. [Add the v. split panel to the middle
   container](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L369)

This node gets attached to the DOM with the middle container (see steps to mount
the middle container, above).


### Right sidebar

![Screenshot on which the right sidebar is
outlined](annotated-ui-screenshots/right-sidebar.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div[aria-label="alternate sidebar"]

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | none |
| CSS class | [jp-mod-right](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L325) |
| HTML role | [complementary](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L334) |
| aria-label | [alternate sidebar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L326) |
| Controlling class | [Lumino TabBar](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/tabbar.ts#L43) |


Steps to mount:

1. [Create handler for right
   sidebar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L298).
   The [right handler creates a new Lumino
   TabBar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1647).
2. [Add the right sidebar to the middle
   container](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L370)

This node gets attached to the DOM with the middle container (see steps to mount
the middle container, above).


### Status bar

![Screenshot on which the status bar is
outlined](annotated-ui-screenshots/status-bar.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-bottom-panel > div#jp-main-statusbar

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-main-statusbar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/statusbar-extension/src/index.ts#L64) |
| Controlling class | [StatusBar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/statusbar/src/statusbar.ts#L24) extends Lumino Widget |


Steps to mount:

1. [Create new status
   bar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/statusbar-extension/src/index.ts#L63)
2. [Ask shell to add status bar to bottom
   area](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/statusbar-extension/src/index.ts#L65)
3. The shell [passes the status bar to its bottom
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1338)

This node then gets attached to the DOM with the bottom container (see steps to
mount the bottom container, above).


### Main menu bar


The main menu bar appears at the top and contains the menu items: File, Edit,
View, etc.

![Screenshot on which the main menu bar is
outlined](annotated-ui-screenshots/main-menu-bar.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-top-panel > div#jp-menu-panel > div#jp-MainMenu

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-MainMenu](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu-extension/src/index.ts#L150) |
| Controlling class | [MainMenu](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu/src/mainmenu.ts#L22) extends [Lumino MenuBar](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/menubar.ts#L35) |


Steps to mount:

(Note: this set of steps is nearly identical to the set of steps to mount the
Jupyter logo.)

1. [Create new menu
   bar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu-extension/src/index.ts#L149)
2. [Ask shell to add menu bar to menu
   area](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu-extension/src/index.ts#L250)
3. The shell [passes the menu bar to its menu
   handler](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1294)
4. The menu handler [passes the menu bar to its Lumino
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1594)
5. The panel [passes the menu bar to its
   layout](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/panel.ts#L68)
6. The panel layout [mounts the menu bar to the
   DOM](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/panellayout.ts#L87)


### Main horizontal split panel


The horizontal split panel contains the left area panel, the main area panel,
and the right area panel.

![Screenshot on which the main split panel is
outlined](annotated-ui-screenshots/main-split-panel.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div#jp-main-vsplit-panel > div#jp-main-split-panel

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-main-split-panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L308) |
| Controlling class | [RestorableSplitPanel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L2061) extends [Lumino SplitPanel](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/splitpanel.ts#L30) |


Steps to mount:

1. [Create split
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L293).
2. [Add the h. split panel to the v. split
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L365)

This node gets attached to the DOM with the vertical split panel (see steps to
mount the vertical split container, above).


### Status bar left panel


The status bar has three sections: left, middle, and right. Here we cover the
left section.

![Screenshot on which the status bar left panel is
outlined](annotated-ui-screenshots/status-bar-left-panel.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-bottom-panel > div#jp-main-statusbar >
    div:first-child

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div  |
| HTML id   | none |
| Controlling class | [Lumino Panel](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/panel.ts#L24) |


Steps to mount:

1. [Create the status bar left
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/statusbar/src/statusbar.ts#L31).
2. [Add the panel to the status bar's
   layout](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/statusbar/src/statusbar.ts#L43)

This node will then get attached to the DOM when the status bar gets attached.


### Main menu bar item: "File"


A menu item is a clickable area labeled with text. It belongs to either a menu
or a menu bar. For example, the word "File" in menu bar is a menu item, and
within the file menu, the word "New Launcher" is a menu item. Clicking a menu
item either opens a sub-menu or executes a command.

![Screenshot on which "File" menu item of the main menu bar is
outlined](annotated-ui-screenshots/file-menu-item.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-top-panel > div#jp-menu-panel >
    div#jp-MainMenu > ul[role="menubar"] > li[role="menuitem"]

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | li   |
| HTML id   | none |
| tabindex | [0](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/menubar.ts#L785) |
| HTML role | [menuitem](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/menubar.ts#L875) |
| aria-haspopup | [true](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/menubar.ts#L875) |
| Controlling class | [VirtualElement](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/virtualdom/src/index.ts#L756) |


Steps to mount:

To make this concrete, we will follow the steps to mount the "File" menu item.

1. [Provide the "File" menu item
   label](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu-extension/schema/plugin.json#L8)
2. Apply the label to the file menu. This involves a lot of steps, some of which
   we are going to skip here. First, [load the menu
   JSON](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu-extension/src/index.ts#L865).
   Then [pass the menu JSON along with a factory
   function](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu-extension/src/index.ts#L871)
   to MenuFactory.createMenus() method, which transforms the JSON data and
   [passes it to the factory
   function](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/menufactory.ts#L60),
   which [passes to the class method
   MainMenu.generateMenu](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu-extension/src/index.ts#L160).
   The important line in that function is [where it sets the menu
   title](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu/src/mainmenu.ts#L312)
   to the label we provided.
3. [Add the file menu to the main
   menu](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu-extension/src/index.ts#L158).
   Internally, this [calls the Lumino TabBar insertMenu()
   method](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/mainmenu/src/mainmenu.ts#L170),
   which in turn [calls its update()
   method](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/menubar.ts#L232),
   which in turn causes [the onUpdateRequest
   handler](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/menubar.ts#L400)
   to get called.
4. [Render the menu
   item](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/menubar.ts#L408).
   This [creates an li
   tag](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/menubar.ts#L784).
5. [Add the li to the menu bar
   ul](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/menubar.ts#L416)

When the menu bar gets attached to the DOM, the menu item will also get attached
to the DOM.


### A tab in the left sidebar: file browser


These are clickable icons in the sidebar that open a panel in the left area when
clicked. By default these include: file browser, running terminal and kernels,
table of contents, and extension manager.

![Screenshot on which the file browser tab in the left sidebar is
outlined](annotated-ui-screenshots/file-browser-tab.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div[aria-label="main sidebar"] >
    ul[aria-label="main sidebar"] >
    li[role="tab"]

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | li   |
| HTML id   | [tab-key-0](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/tabbar.ts#L1646) (for example) |
| HTML title | [File Browser (⇧ ⌘ F)](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser-extension/src/index.ts#L184) (for example) |
| tabindex | none |
| HTML role | [tab](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/tabbar.ts#L1712) |
| aria-selected | [true/false](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/tabbar.ts#L1712) |
| Controlling class | [VirtualElement](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/virtualdom/src/index.ts#L756) |


Steps to mount:

Note that the steps to mount a tab in left sidebar are similar to the steps to
mount a menu item in the main menu bar. We will use the file browser as a
concrete example.

1. [Create the file browser
   widget](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser-extension/src/index.ts#L301)
2. [Attach the folder icon to the widget
   title](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser-extension/src/index.ts#L393)
3. Ask the shell to [add the file browser widget to the left
   area](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser-extension/src/index.ts#L395).
   The shell [passes the widget to its left
   handler](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1168).
   The left handler [passes the widget's title to its Lumino TabBar
   instance](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1747).
4. [Insert tab object into tab
   bar](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/tabbar.ts#L411).
   This calls update(), which in turn triggers onUpdateRequest().
5. [Render tab element from tab
   object](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/tabbar.ts#L645).
   This [creates an
   li](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/tabbar.ts#L1565).
6. [Add the li to the tab bar
   ul](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/tabbar.ts#L647)

When the tab bar gets attached to the dom with shell's left handler, this tab
will also get mounted.


### Left tab panel container


This is the point of attachment for tab panels that are opened and closed by the
left sidebar.

![Screenshot on which the left tab panel container is
outlined](annotated-ui-screenshots/left-tab-panel-container.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div#jp-main-vsplit-panel >
    div#jp-main-split-panel >
    div#jp-left-stack

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-left-stack](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L322) |
| Controlling class | [Lumino StackedPanel](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/stackedpanel.ts#L24) |
| Shell area | [left](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L762) |


Steps to mount:

1. [Create stacked
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1653).
2. [Add stacked panel to the main horizontally split
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L361)

This node gets attached to the DOM with the main horizontally split panel (see
steps to mount the horizontally split container, above).


### Main document area


The main document area is the area in which notebooks and other documents are
shown. The main area can be split vertically and then again horizontally for a
4-by-4 layout. Inside each split (whether there are no splits or 2 or 3 or 4),
each document has a tab that can be dragged from one split area into another.

![Screenshot on which the main document area is
outlined](annotated-ui-screenshots/main-document-area.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div#jp-main-vsplit-panel >
    div#jp-main-split-panel >
    div#jp-main-dock-panel

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-main-dock-panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L307) |
| HTML role | [main](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L337) |
| Controlling class | [DockPanelSvg](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/ui-components/src/icon/widgets/tabbarsvg.ts#L63) extends [Lumino DockPanel](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/dockpanel.ts#L35) |
| Shell area | [main](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L764) |


Steps to mount:

1. [Create main dock
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L288).
2. [Add main dock panel to the main horizontally split
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L362)

This node gets attached to the DOM with the main horizontally split panel (see
steps to mount the horizontally split container, above).


### Right tab panel container


See left tab panel container. The information is essentially the same, but the
HTML id is `jp-right-stack`.

![Screenshot on which the right tab panel container is
outlined](annotated-ui-screenshots/right-tab-panel-container.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div#jp-main-vsplit-panel >
    div#jp-main-split-panel >
    div#jp-right-stack


### A tab in the right sidebar


See left sidebar tab. The idea is basically the same.

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div[aria-label="alternate sidebar"] >
    ul[aria-label="alternate sidebar"] >
    li[role="tab"]


### The document mode switch in the status bar left panel


This is the switch labeled "Simple" in the lower left of the UI, in the status
bar.

![Screenshot on which the document mode switch in the status bar is
outlined](annotated-ui-screenshots/document-mode-switch.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-bottom-panel > div#jp-main-statusbar >
    div:first-child >
    div#jp-single-document-mode

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [jp-single-document-mode](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/statusbar-extension/src/index.ts#L350) |
| Controlling class | [Switch](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/ui-components/src/components/switch.ts#L11) extends Lumino Widget |


Steps to mount:

1. [Create
   switch](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/statusbar-extension/src/index.ts#L349)
2. [Ask status bar to add switch to its left
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/statusbar-extension/src/index.ts#L379).
   The status bar [passes the switch to its left
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/statusbar/src/statusbar.ts#L84),
   which delegates to the Lumino Panel addWidget method.

The switch is now in the tree of the status bar node, so when the status bar
node get attached to the DOM, so will this node.


### The file browser panel (in the left panel area)


The file browser allows the user to interact with folders and files on their
file system.

![Screenshot on which the file browser panel in the left panel area is
outlined](annotated-ui-screenshots/file-browser-panel.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div#jp-main-vsplit-panel >
    div#jp-main-split-panel >
    div#jp-left-stack
    div#filebrowser

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [filebrowser](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser-extension/src/index.ts#L310) |
| CSS class | [jp-FileBrowser](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser/src/browser.ts#L67) |
| HTML role | [region](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser-extension/src/index.ts#L391) |
| aria-label | [File Browser Section](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser-extension/src/index.ts#L392) |
| Controlling class | [FileBrowser](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser/src/browser.ts#L59) extends [Lumino Widget](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/widget.ts#L38) |

Steps to mount:

1. [Create file browser
   widget](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser-extension/src/index.ts#L301)
2. [Ask shell to add widget to left
   area](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser-extension/src/index.ts#L395).
   The shell [passes the file browser widget to its left
   handler](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1168).
   The left handler [passes the file browser widget to its stacked
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1746).
   The stacked panel delegates to the [Lumino Panel insertWidget
   method](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/panel.ts#L68),
   which in turn delegates to PanelLayout.

The file browser panel is now in the tree of the left tab panel container, so it
will be attached to the DOM when its parent is (see steps to mount the left tab
panel container, above).

After the file browser widget is mounted, it gets shown and hidden via a Lumino
Signal from the TabBar. When TabBar's currentIndex gets changed, it calls
`this._currentChanged.emit`, which triggers
[`shell._leftHandler._onCurrentChanged`](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1855).


### A tab bar of open documents in the main dock area


A tab bar in the main area allows you switch between open documents within a
particular split of the main dock panel.

![Screenshot on which open documents tab bar of the main dock area is
outlined](annotated-ui-screenshots/tab-bar-of-open-documents.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div#jp-main-vsplit-panel >
    div#jp-main-split-panel >
    div#jp-main-dock-panel >
    div.lm-DockPanel-tabBar

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | none |
| CSS class | [lm-DockPanel-tabBar](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/dockpanel.ts#L1394) |
| Controlling class | [Lumino TabBar](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/tabbar.ts#L43) |

The tab bar is created by the main Lumino DockPanel instance via [its private
_createTabBar
method](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/dockpanel.ts#L922).
The Lumino DockLayout [handles mounting the tab
bar](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/docklayout.ts#L1105)
to the DOM.

Like the shell's left sidebar handler, it [connects a currentChanged handler to
the tab
bar](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/dockpanel.ts#L944),
so that when the tab changes, it can change the corresponding tab panel.


### Notebook Panel


A notebook panel is rendered into the main area. It contains a toolbar and the notebook body.

![Screenshot on which the notebook panel in the main area is
outlined](annotated-ui-screenshots/notebook-panel.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div#jp-main-vsplit-panel >
    div#jp-main-split-panel >
    div#jp-main-dock-panel >
    div.jp-NotebookPanel

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [a uuid](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L36) |
| CSS class | [jp-NotebookPanel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/notebook/src/panel.ts#L55) |
| HTML role | [tabpanel](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/docklayout.ts#L2078) |
| aria-labelledby | [tab-key-0](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/docklayout.ts#L2086) (for example) |
| Controlling class | [NotebookPanel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/notebook/src/panel.ts#L45) extends [DocumentWidget](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/docregistry/src/default.ts#L490) extends [MainAreaWidget](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L20) extends [Lumino Widget](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/widget.ts#L38) |


Steps to mount:

There are multiple code paths to mount a notebook into the DOM. For example,
using the open command from the file menu versus double clicking on a notebook
file in the file browser extension.

1. [Double click on notebook in file
   browser](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser/src/listing.ts#L1087)
2. [Use the document manager to open the
   file](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/filebrowser/src/listing.ts#L1020)
3. The document manager maps the file to a widget factory based on the file's
   extension. Using the factory, it [creates the
   widget](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/docmanager/src/manager.ts#L590)
   (in this case, a NotebookPanel widget).
4. The doc manager then [asks the shell to add the widget to the main
   area](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/docmanager-extension/src/index.tsx#L129).
   The shell [passes the widget to its main area
   handler](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/application/src/shell.ts#L1217)
   (a dock panel).
5. The dock panel (through its DockLayout member), [attaches the notebook node
   to the
   DOM](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/docklayout.ts#L555),
   by appending it to the main area container node (#jp-main-dock-panel).


### Notebook toolbar


The notebook toolbar is a strip of buttons rendered above the notebook to
perform actions on the notebook, such as copy, paste, save, insert cell.

![Screenshot on which the notebook toolbar is
outlined](annotated-ui-screenshots/notebook-toolbar.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div#jp-main-vsplit-panel >
    div#jp-main-split-panel >
    div#jp-main-dock-panel >
    div.jp-NotebookPanel >
    div.jp-NotebookPanel-toolbar

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | none |
| CSS class | [jp-NotebookPanel-toolbar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/notebook/src/panel.ts#L56) |
| HTML role | [navigation](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L43) |
| aria-label | [notebook actions](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L44) |
| Controlling class | [ReactiveToolbar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/ui-components/src/components/toolbar.tsx#L357) extends [Toolbar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/ui-components/src/components/toolbar.tsx#L163) extends [Lumino Widget](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/widget.ts#L38) |


Steps to mount:

1. When the NotebookPanel widget is created (see above), it [creates its own
   toolbar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L42).
2. It then [adds the
   toolbar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L57)
   to its layout (BoxLayout), so that when it gets attached to the DOM, so will
   the toolbar.


### Notebook content


The notebook content is where the actual document is rendered for display and
editing.

![Screenshot on which the notebook content is
outlined](annotated-ui-screenshots/notebook-content.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div#jp-main-vsplit-panel >
    div#jp-main-split-panel >
    div#jp-main-dock-panel >
    div.jp-NotebookPanel >
    div.jp-NotebookPanel-notebook

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | [a uuid if no id is provided](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L62) |
| CSS class | [jp-NotebookPanel-notebook](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/notebook/src/panel.ts#L57) |
| HTML role | [region](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L40) |
| tabindex | [0](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L64) |
| aria-label | [notebook content](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L41) |
| Controlling class | [Notebook](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/notebook/src/widget.ts#L1124) extends [StaticNotebook](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/notebook/src/widget.ts#L190) extends [Lumino Widget](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/widget.ts#L38) |


Steps to mount:

1. When the doc manager uses the notebook widget factory to create a new
   notebook panel, it [passes in a notebook
   instance](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/notebook/src/widgetfactory.ts#L102)
   to the notebook panel constructor.
2. The notebook panel constructor (through the MainAreaWidget parent class)
   [adds the notebook widget to its
   layout](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/mainareawidget.ts#L59),
   just like the notebook toolbar, above, so when the notebook panel gets
   attached to the DOM so does the notebook body.


### Notebook toolbar item: save button

![Screenshot on which the notebook toolbar item save button is
outlined](annotated-ui-screenshots/notebook-toolbar-item.png)

Node-to-node CSS selector path for this node:

    div#main > div#jp-main-content-panel >
    div#jp-main-vsplit-panel >
    div#jp-main-split-panel >
    div#jp-main-dock-panel >
    div.jp-NotebookPanel >
    div.jp-NotebookPanel-toolbar >
    div.jp-Toolbar-item

Table of properties:

| Name | Value |
| ---- | ----- |
| HTML tag  | div   |
| HTML id   | none |
| CSS class | [jp-Toolbar-item](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/ui-components/src/components/toolbar.tsx#L226) |
| Controlling class | [ReactiveToolbar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/ui-components/src/components/toolbar.tsx#L357) extends [Toolbar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/ui-components/src/components/toolbar.tsx#L163) extends [Lumino Widget](https://github.com/jupyterlab/lumino/blob/v2021.12.13/packages/widgets/src/widget.ts#L38) |


Steps to mount:

1. The doc manager [uses a factory to create a new notebook
   panel](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/docmanager/src/manager.ts#L590)
2. The factory, using a [toolbar
   factory](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/toolbar/factory.ts#L294),
   [creates the toolbar
   items](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/docregistry/src/default.ts#L433).
   Note: the toolbar items are [gathered from a json
   file](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/notebook-extension/schema/panel.json#L4).
3. The toolbar factory [passes each item to its own item
   factory](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/apputils/src/toolbar/registry.ts#L53).
   For example, the [save button has its own
   factory](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/notebook-extension/src/index.ts#L822).
4. The save button factory [creates the save
   button](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/docmanager-extension/src/index.tsx#L464),
   which is a React button wrapped in a Lumino Widget.
5. The notebook widget factory [adds the save button to the
   toolbar](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/docregistry/src/default.ts#L438).
   The toolbar [passes the save button to its
   layout](https://github.com/jupyterlab/jupyterlab/blob/v4.0.0a18/packages/ui-components/src/components/toolbar.tsx#L230),
   which is a Lumino PanelLayout that handles putting this node into the toolbar
   node tree.

So when the notebook toolbar gets attached to the DOM, so does the toolbar item.
