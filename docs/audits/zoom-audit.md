# Zoom Audit

## Background and Overview

Zoom is one of the mechanisms used by vision impaired users to navigate through Web interfaces and programs. This is a builtin functionality in any Web browser that can offer from 25% up to 400% zoom by resizing the contents of a webpage. Given the importance of this tool in the accessibility context, WCAG has a complete set of guidelines regarding the expected behavior of webpages when zoom is used.

The main premise of the WCAG standard is that websites need to preserve all the information regardless of the zoom level and the size of the user’s screen. The reality is that the way zoom is handled in webpages varies, and a lot of them will often break when more than 200% zoom is used.

Given the importance of this tool for disabled users it was important to recognize the state of JupyterLab when used in higher zoom values. The following document will state the methodology, results and recommendations found in the audit.

## Methodology

Given that the JupyterLab interface is so complex, it was impossible to do one general audit of the whole interface. Instead, it was decided to break down the UI in the main 7 areas, left sidebar, right sidebar, main content area, menu bar, context menu, settings and the status bar.

Each of the areas was tested in 0%, 200% and 400% zoom. In all the scenarios, JupyterLab default settings were used.

## Findings

All of the tests were made using JupyterLab 3.4.3 in a 16-inch Macbook Pro in Google Chrome.

The major findings are listed below,

The definition of vertical padding and height are working as they are and they have sense to leave them in px in the sidebars items.
We need to define a new UX for when the left sidebar is taking too much space compared to the main area. My suggestion will be to compress the left pane to give priority to the main content area.
Files in the main content area are wrapping lines instead of having a horizontal scrollbar, which allows to see all the code without any action.
If zoom is activated some filenames are not visible in the tabs, but hovering over them will give the complete information of the file
Opening a lot of files in zoom may cause to just seeing the icon and not being able to even close it
The notebook's toolbar is responsive and all the options are visible and usable
Cell options layout breaks with 400% zoom
Python logo in the launcher pixelates with zoom
Dialogs occupy the complete interface with 400% zoom
The menu items start getting lost as zoom increases
The dropdown menus are not visible or usable with 400% zoom
Modifying to responsive layouts break the menubar and its usability
Automatically we have a scrollbar to navigate through the options in context menus if not visible at first
The size of context menus is fixed in px which occupy a lot of space in small screens or high zoom
Settings is not usable in small screens or with zoom, the options are chopped and not readable
Settings left menu area doesn't resize
Settings is using the same gear icon for multiple entries
The Status bar is responsive for even mobile screen sizes

## Overall recommendations

The following list of tasks was proposed,

- Define a new UX for the left sidebar when they are taking too much space compared to the main area
- Define a new UX for the right sidebar when they are taking too much space compared to the main area
- Define a new UX/UI for the tabs in the main content area, especially the cases where too many of them are opened.
- Make the cell options layout be responsive (it may include removing some options or adding ellipsis when the space is small)
- Change the python logo to a new image that has better resolution
- Dialogs sizes need to be checked for high zoom or small screens
- Add a hamburger menu in the main menu bar when the space is smaller to avoid losing items.
- Dropdown menus from the main menu bar should open to the left/right depending on the space in the screen
- Check and define the UI/UX for context menus in small screens and/or high zoom
- Define a new UX for the Settings pane to handle small screens and/or high zoom

## References

If you are interested in reading the full audit, see the actual screenshots of the interface and be part of the discussions please refer to the following issues,

- [Summary of the zoom audit](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/34#issuecomment-1210168155)
- [Left sidebar audit](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/3)
- [Right sidebar audit](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/6)
- [Main content area audit](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/9)
- [Menu bar audit](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/11)
- [Context menu audit](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/14)
- [Settings audit](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/16)
- [Status bar](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/18)
