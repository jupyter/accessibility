# Useful Jupyter Accessibility Resources

🔔 Looking for [accessibility docs?](../accessibility-docs)

One of our goals is to collect information about accessibility and create documentation to empower the Jupyter community to help us make our software accessible. Please use this section to begin to aggregate relevant accessibility third party standards, guides, and documentation.

## Accessibility guidelines

The World Wide Web Consortium (W3C) publishes a number of international recognized technical guidelines, like the Web Accessibility Initiative (WAI) and XHTML standards. These guidelines assure that a given website can be accessed and consumed by as many people as possible.

### Accessible Rich Internet Applications (WAI-ARIA)

[WAI-ARIA](https://www.w3.org/WAI/standards-guidelines/aria/) provides a route to make web content and applications more accessible, it specifically targets dynamic content and advanced user interface controls that are normally developed in JavaScript, HTML and other related technologies. A website that doesn't implement this guideline will not be accessible to some users with disabilities, specially the ones that rely on a screen reader or cannot use the mouse.

Is important to remember that links, buttons and form elements are the only elements that can receive focus in HTML. Meaning that lists, paragraphs, `div` or `span`, will never get focus from the keyboard making them not accessible to users that are not using a mouse. This is where WAI-ARIA provides web developers with techniques to enable keyboard users have a structure, making their websites more navigable. This guideline also include modules for Graphics and Digital Publishing.

ARIA is an additional layer to web content, not a required layer. Though ARIA is powerful, it is important to remember that misused ARIA can make a worse experience for assistive tech users, especially screen reader users. It is often warned that "[No ARIA is better than Bad ARIA](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)." Doing relevant research before using ARIA and testing results with screen readers is especially wise here.

More info:

- [WAI-ARIA standard](https://www.w3.org/TR/wai-aria/)
- [ARIA Authoring Practices Guide (APG)](https://www.w3.org/WAI/ARIA/apg/)
- [WAI-ARIA 1.1 Standard](https://www.w3.org/TR/wai-aria-1.1/)

### Web Content Accessibility Guidelines (WCAG)

The WCAG is a technical standard that takes care of information shared through websites. This includes content like text, images and sounds, and code or markup that specify structure and presentation.

This standard is stable and does not change after it is published. The latest draft, [WCAG 2.2](https://www.w3.org/TR/WCAG22/), has 13 guidelines organized under four principles: perceivable, operable, understandable, and robust. Each guideline has a testable success criteria for conformance that can vary from A, AA, and AAA. Until WCAG 2.2 formally becomes a standards document, [WCAG 2.1](https://www.w3.org/TR/WCAG21/) remains the most up to date standard.

More info:

- [Web Content Accessibility Guidelines 2.1](https://www.w3.org/TR/WCAG21/) - The current W3C Recommendation
- [WCAG intro](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [A glance of WCAG 2.1](https://www.w3.org/WAI/standards-guidelines/wcag/glance/)
- [Four principles of accessibility](https://www.w3.org/WAI/WCAG21/Understanding/intro#understanding-the-four-principles-of-accessibility)
- [Levels of conformance](https://www.w3.org/WAI/WCAG21/Understanding/conformance#levels)

### More resources

- [Accessibility Weekly Newsletter Archives](https://a11yweekly.com/issues/)
- [The A11y Project](https://a11yproject.com/)

## Accessibility Legislature

Many countries have laws that specify the ways in which they expect digital content to be accessible. Some of these laws require that software meet their accessibility guidelines to be used in specific places, like schools. For example, [Section 508](https://www.section508.gov/about-us/) compliance is important in the U.S.

Depending on the project and where in the world it is intended for use, there may be more specific accessibility resources.It's worth noting that several digital accessibility laws globally do draw on the work of the W3C including WCAG.
- [18F Accessibility Guide](https://accessibility.18f.gov/)
- [The tota11y toolbar](https://khan.github.io/tota11y/) is a lightweight javascript toolbar for quick a11y analysis.
- [The WAVE tool](http://wave.webaim.org/report#/http://z2jh.jupyter.org/) is a web analyzer for page accessibility.


## Accessibility-related issues

A number of open issue related to accessibility are already open on the repos above.
Please help us to aggregate links to those here.
The preferred way to do this is for each repo to have a unique GitHub label for accessibility,
and then to link to the GitHub issue search that automatically lists those issues:

- [Jupyter Notebook Accessibility Issues](https://github.com/jupyter/notebook/issues?q=is%3Aopen+is%3Aissue+label%3Atag%3AAccessibility)
- [JupyterHub Accessibility Issues](https://github.com/jupyterhub/jupyterhub/issues?q=is%3Aopen+is%3Aissue+label%3Aaccessibility)
- [JupyterLab Accessibility Issues](https://github.com/jupyterlab/jupyterlab/issues?q=is%3Aopen+is%3Aissue+label%3Atag%3AAccessibility)
