# Notebook Authoring Accessibility Guide

Writing notebooks is an art, depending on what as an author you want to share to the world the way that the writing and publishing techniques can vary widely. No matter what interface a notebook is opened in, writing a notebook with good structure and content that can be accessed multiple ways will increase the accessibility of your work.

In this section, we will introduce some guidelines to make edits to your notebooks for accessibility. It is an excellent step you can take to make our communities more inclusive!

All the information presented is based on the [draft authoring tips](https://github.com/Iota-School/notebooks-for-all/blob/main/resources/event-hackathon/accessibility-tips-for-jupyter-notebooks.md) and the [Notebook authoring accessibility checklist](https://github.com/Iota-School/notebooks-for-all/blob/main/resources/event-hackathon/notebook-authoring-checklist.md) from the Notebooks For All team.

# Table of contents
1. [Structure](#structure)
2. [Text](#text)
3. [Code](#code)
4. [Media](#media)
    1. [Images](#images)
    2. [Visualizations](#visualizations)
    3. [Videos](#videos)
    4. [Audio and Sonifications](#audio)
    5. [Interactive Widgets](#interactive)
5. [Resources](#resources)
6. [Acknowledgements](#acknowledgements)

## Structure <a name="structure"></a>

Sighted users are able to perceive structure and relationship using different visual cues. We want to ensure that **information and relationships** are perceivable to all. In order to accomplish this goal, we as content authors need to provide access to the information in different modalities.

At the time of writing, notebooks gain most of their structure from their content and content headings (like `<h1>`, `<h2>`, etc. or the Markdown equivalents `#`, `##`, etc.). Making sure to use headings and other markdown as intended is one of the most important things an author can do to make an approachable and navigable notebook. 

### The First Cell

- [ ] The title of the notebook in a first-level heading (eg. `<h1>` or `# in markdown`).
- [ ] A brief description of the notebook.
- [ ] A brief summary of the notebook.
- [ ] The date first published.
- [ ] The author(s) and affiliation(s) (if relevant).
- [ ] The date last edited (if relevant).
- [ ] A link to the notebook's source(s) (if relevant).
- [ ] A table of contents in an [ordered list](https://www.markdownguide.org/basic-syntax/#ordered-lists) (`1., 2.,` etc. in Markdown).

### Other cells

- [ ] There should be only one H1 (`#` in Markdown) used in the notebook; it should not appear in other cells.
- [ ] The notebook uses other [heading tags](https://www.markdownguide.org/basic-syntax/#headings) in order throughout. This creates a table of contents that supports the whole notebook.

## Text (Markdown cells)<a name="text"></a>

- [ ] All link text is descriptive. It tells users where they will be taken if they open the link.
- [ ] Use plain language wherever possible.
- [ ] All acronyms are defined at least the first time they are used.
- [ ] Field-specific/specialized terms are used when needed, but not excessively.
- [ ] Text is broken into paragraphs and/or cells where relevant.
- [ ] Text is in complete sentences where relevant.

## Code (code cells) <a name="code"></a>

- [ ] Code sections are introduced and explained before they appear in the notebook. This can be fulfilled with a heading in a prior Markdown cell, a sentence preceding it, or a code comment in the code section.
- [ ] Code has explanatory comments (if relevant). This is most important for long sections of code.
- [ ] If the author has control over the syntax highlighting theme in the notebook, that theme has enough color contrast to be legible.
- [ ] Code and code explanations focus on one task at a time. Unless comparison is the point of the notebook, only one method for completing the task is described at a time.

## Media <a name="media"></a>

This category include images, visualizations, videos and interactive widgets. If you are reviewing a notebook with mixed content please keep in mind the following two points,

- Text is flexible. Whether it is in the document or linked out, text can be read visually, be read audibly, be magnified, or be translated to another language. Having a text alternative is a good back up plan.

- Having enough color contrast is required on almost all visual content.

### Images <a name="images"></a>

- [ ] All images (jpg, png, svgs) have an [image description](https://www.w3.org/WAI/tutorials/images/decision-tree/). This could be
    - [ ] [Alt text](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/alt) (an `alt` property)
    - [ ] [Empty alt text](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/alt#decorative_images) for decorative images/images meant to be skipped (an `alt` attribute with no value)
    - [ ] Captions
    - [ ] If no other options will work, the image is described in surrounding paragraphs.

- [ ] Any [text present in images](https://www.w3.org/WAI/WCAG21/Understanding/images-of-text.html) exists in a text form outside of the image (this can be alt text, captions, or surrounding text.)
- [ ] Content in images [have enough contrast](https://www.w3.org/TR/WCAG22/#contrast-minimum) for its type.

### Visualizations <a name="visualizations"></a>

- [ ] All visualizations have an image description. Review the previous section, [Images](#images), for more information on how to add it.
- [ ] [Visualization descriptions](http://diagramcenter.org/specific-guidelines-e.html) include
    - [ ] The type of visualization (like bar chart, scatter plot, etc.)
    - [ ] Title
    - [ ] Axis labels and range
    - [ ] Key or legend
    - [ ] An explanation of the visualization's significance to the notebook (like the trend, an outlier in the data, what the author learned from it, etc.)

- [ ] All visualizations have the following labels
    - [ ] Title
    - [ ] Labels on all axes
    - [ ] Key or legend (if relevant)

- [ ] All visualizations and their parts have [enough color contrast](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html) ([color contrast checker](https://webaim.org/resources/contrastchecker/)) to be legible. Remember that transparent colors have lower contrast than their opaque versions.
- [ ] All visualizations [convey information with more visual cues than color coding](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html). Use text labels, patterns, or icons alongside color to achieve this.
- [ ] All visualizations have an additional way for notebook readers to access the information. Linking to the original data, including a table of the data in the same notebook, or sonifying the plot are all options.

### Videos <a name="videos"></a>

- [ ] All videos have titles in the player or in the text before them.
- [ ] All videos have [captions/subtitles](https://www.w3.org/WAI/media/av/captions/). This can include visual information descriptions if relevant.
- [ ] All videos have [transcripts](https://www.w3.org/WAI/media/av/transcripts/). This can include visual information descriptions if relevant.
- [ ] All [video players](https://www.w3.org/WAI/media/av/player/) have buttons with labels. This can be a persistent label or appear when hovered.
- [ ] All video players have buttons with [enough color contrast](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html).
- [ ] No videos have [flashing images at more than three frames per second](https://www.w3.org/WAI/WCAG21/Understanding/three-flashes-or-below-threshold.html).


### Audio and Sonifications <a name="audio"></a>

- [ ] Sonifications include a key explaining the mapping of data to sound. A written description can be used to convey this information.
- [ ] Sonification outputs reference the method that generated the sonification. This can be done in a code cell or with a link to the file used to generate the sonification.
- [ ] Audio players include basic listening controls for starting, pausing, volume, and speed.
- [ ] All audio players have buttons with labels. This can be a persistent label or appear when hovered.
- [ ] All audio players have buttons with [enough color contrast](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html).


### Interactive Widgets <a name="interactive"></a>

The accessibility of interactive widgets varies greatly depending how they are included in the notebook. Review beyond this checklist may be needed.

- [ ] All interactive widgets with visual controls have labels. This can be a persistent label or appear when hovered.
- [ ] All interactive widgets with visual controls have [enough color contrast](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html).
- [ ] All interactive widgets have a summary of what they are and what they do in the surrounding text.
- [ ] If an interactive widget's contents are needed to understand the rest of the notebook, the widget either needs to be tested further or have that content fully represented not as a widget elsewhere in the notebook.

## Related resources <a name="resources"></a>

Resources are for information purposes only, no endorsement implied.

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet)
- [An `alt` Decision Tree - World Wide Web Consortium Web Accessibility Initiative](https://www.w3.org/WAI/tutorials/images/decision-tree/)
- [Image Description Guidelines - DIAGRAM Center](http://diagramcenter.org/table-of-contents-2.html)
- [Alt text style guide for Jupyter accessibility workshops](https://github.com/Quansight-Labs/jupyter-accessibility-workshops/blob/fd1d7f96ca40943eda050a339ba64bcf16dd638a/docs/alt-text-guide.md)
- [Contrast Checker - Web Accessibility In Mind](https://webaim.org/resources/contrastchecker/)
- Accessible syntax highlighting themes. [a11y-syntax-highlighting by Eric Bailey on GitHub](https://github.com/ericwbailey/a11y-syntax-highlighting)
- Accessible visualization guidelines. [Chartability](https://chartability.fizz.studio/)
- A package for sonifying astronomical data. [Astronify](https://astronify.readthedocs.io/en/latest/)
- [Quick accessibility tests anyone can do - Tetralogical blog](https://tetralogical.com/blog/2022/01/18/quick-accessibility-tests-anyone-can-do/)
- Other [Notebooks For All resources](https://iota-school.github.io/notebooks-for-all/)
- [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/)
- Guidance for writing, designing, and developing for accessibility.[Design and Develop Overview - World Wide Web Consortium Web Accessibility Initiative](https://www.w3.org/WAI/design-develop/)
- [Guidance and tools for digital accessibility - GOV.UK](https://www.gov.uk/guidance/guidance-and-tools-for-digital-accessibility)
- [Accessibility for Teams - United States General Services Administration](https://accessibility.digital.gov/)


## Acknowledgements <a name="acknowledgements"></a>

All the information presented is based on the [draft authoring tips](https://github.com/Iota-School/notebooks-for-all/blob/main/resources/event-hackathon/accessibility-tips-for-jupyter-notebooks.md) and the [Notebook authoring accessibility checklist](https://github.com/Iota-School/notebooks-for-all/blob/main/resources/event-hackathon/notebook-authoring-checklist.md) from the Notebooks For All team.
