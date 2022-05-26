# JupyterLab Testing Scripts

This is a series of [testing scripts](). designed to mimic common manual accessibility tests in an automated testing setting for JupyterLab. They currently reference [WCAG 2.1](), but ideally will be updated for future versions of WCAG or to align with [ACT-rules]().

Those unfamiliar with manual testing techniques may also find these scripts helpful in understanding what to do and observe in a manual testing setting as well.

Different scripts apply to different levels of JupyterLab (ie. the whole application versus a single extension). The ideal implementation of these tests is noted in their `Proposed JupyterLab success criteria` section.

## Test proposals

### [1.3.4 - Orientation](https://www.w3.org/WAI/WCAG21/quickref/#orientation)

#### Proposed JupyterLab success criteria

JupyterLab is responsive. When switched to portrait orientation or viewed on mobile, no UI content is lost.

This can be tested on the whole JupyterLab application.

#### Proposed testing script

| Step | Expected Behavior | 
|-----|-----|
| 1. Open default JupyterLab | JupyterLab opens with unmodified workspace. |
| 2. Set viewport orientation to portrait (And/or mobile viewport?) | JupyterLab accepts the orientation change and doesn't error out. |
| 3. Check menu bar is in expected location |  Menu bar is at the top of the page and have all menu items visible (currently it has a scroll bar).| 
| 4. Check left side bar is in expected location | Left side bar is the leftmost part of the viewport . It stretches from the menu bar to status bar. All icons are visible. |
| 5. Check document area is in expected location | Document area is the center and majority of the viewport. |
| 6. Check document area toolbar is in expected location | The document area toolbar is at the top of the document area. All items are visible (currently it has a scroll bar).|
| 7. Check right side bar is in expected location | Right side bar is the rightmost part of the viewport. It stretches from the menu bar to status bar. All icons are visible. (Right now, I believe this side bar is not able to be accessed in this mode.) |
| 8. Check status bar is in expected location | The status bar is at the bottom of the page. All information is visible.|
| 9. Success if all main regions are in expected location | | 

### [2.1.2 No keyboard trap](https://www.w3.org/WAI/WCAG21/quickref/#no-keyboard-trap)

#### Proposed JupyterLab success criteria

Focusable areas in JupyterLab can all be unfocused.

This can be tested on multiple regions of JupyterLab. For example, this script will test that JupyterLab's menu bar can be focused and unfocused.

#### Proposed testing script

| Step | Expected Behavior | 
|-----|-----|
| 1. Open default JupyterLab | JupyterLab opens with unmodified workspace. |
| 2. Start focus at top of tree | Focus goes to JupyterLab tab, may hit skip link. |
| 3. Tab into menu bar | Focus goes to menu bar (whole). | 
| 4. Open file menu | Focus goes to File menu (within menu bar). Menu bar opens full list of menu items. |
| 5. Close file menu | Focus stays on File menu, but menu bar is closed. |
| 6. Tab out of menu bar | Focus moves from File menu, to other menu items until it leaves the region. Focus will move the left side bar/file browser. |
| 7. Success if focus switches to side bar/file browser |  |


### [2.4.3 Focus Order](https://www.w3.org/WAI/WCAG21/quickref/#focus-order)

#### Proposed JupyterLab success criteria

In JupyterLab, areas can be focused in the following order: 

1. Skip link
2. Menu bar
3. Left side bar
4. Inside left side bar (selected section)
5. Top of document area (document toolbar first if it has one)
6. Document (if there is no toolbar for the document type, users go immediately into the document)
7. Right side bar
8. Inside right side bar (selected section)
9. Status bar

This can be tested on the whole JupyterLab application.

#### Proposed testing script

| Step | Expected Behavior | 
|-----|-----|
| 1. Open default JupyterLab | JupyterLab opens with unmodified workspace. |
| 2. Tab to focus menu bar | Tab until focus is on the menu bar. (Will this run into the skip link?) |
| 3. Tab through major regions as needed (see above section) | Tab to move focus through left side bar, inside left side bar, top of document area, document area, right side bar, and inside right side bar. | 
| 4. Tab to focus status bar | Focus moves to status bar. |
| 5. Success if tab brings focus to status bar |  |

### [2.5.6 Concurrent input mechanisms](https://www.w3.org/WAI/WCAG21/quickref/#concurrent-input-mechanisms)

#### Proposed JupyterLab success criteria

In JupyterLab, a single task can be completed using mouse, keyboard, and touch screen inputs. This works even when completing a single continuous task.

This can be tested on multiple regions of JupyterLab. For example, this script will test that JupyterLab can open a new notebook from the launcher with mouse, keyboard, and touch screen inputs.

#### Proposed testing script

| Step | Expected Behavior | 
|-----|-----|
| 1. Open default JupyterLab | JupyterLab opens with unmodified workspace. | 
| 2. Open the file menu with a mouse click | File menu opens and full list of menu items appears. |
| 3. Navigate to menu item New Launcher with arrow keys | Focus moves through the File menu list items until it reaches the New Launcher item. | 
| 4. Use touch screen input to create new Notebook from Launcher | The New Notebook from Launcher is selected and the command is initiated. |
| 5. Success if new notebook opens |  |