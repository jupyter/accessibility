# JupyterLab Accessibility Statement

## Edited from the [W3C accessibility statement generator](https://www.w3.org/WAI/planning/statements/generator/#create)


## :construction: Draft Accessibility Statement for JupyterLab

This is an accessibility statement from Jupyter accessibility contributors.

### Measures to support accessibility

Jupyter accessibility contributors take the following measures to ensure accessibility of JupyterLab:

* Include accessibility as part of our mission statement.
* Provide continual accessibility training for our community.
* Assign clear accessibility goals and responsibilities.
* Employ formal accessibility quality assurance methods.
* Document changes, approaches, and improvements to the above methods and to JupyterLab itself.

### Conformance status

The [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag) defines requirements for designers and developers to improve accessibility for people with disabilities. It defines three levels of conformance: Level A, Level AA, and Level AAA. JupyterLab is non conformant with WCAG 2.1 level AA. Non conformant means that the content does not meet the accessibility standard.

[Picture accessibility compliance levels as mountains. The first peak to reach is AA. This includes both A and AA criteria. Behind it, in the mist, there is a larger peak, AAA. That one is not always completely reachable--Marie Guillaumet, Access42](https://stephaniewalter.design/wp-content/uploads/2022/05/stephaniewalter-sommets-de-l-accessibilite.jpg)

*By [Stéphanie Walter](https://stephaniewalter.design) ([Source](https://stephaniewalter.design/blog/5-illustrations-to-understand-and-promote-accessibility/))*

### Feedback and Formal complaints

We welcome your feedback and formal complaints on the accessibility status of JupyterLab. Please let us know if you encounter accessibility barriers on JupyterLab:

* [Write an issue on jupyter/accessibility](https://github.com/jupyter/accessibility/issues/new)
* [Write an issue on jupyterlab/jupyterlab](https://github.com/jupyterlab/jupyterlab/issues/new) and request it be labeled [tag:accessibility](https://github.com/jupyterlab/jupyterlab/labels/tag%3AAccessibility)

At the time of writing, there is no non-public way to contact us for JupyterLab accessibility issues.

### Compatibility with browsers and assistive technology

JupyterLab is designed to be compatible with the following technologies:

* Windows, macOS, iOS, Android; Firefox, Chrome, Safari, Chromium browsers (mobile and desktop).

JupyterLab is not compatible with:

* Internet Explorer, Edge; JAWS, NVDA, VoiceOver, Narrator, Orca screen readers; voice control technology.

### Technical specifications

Accessibility of JupyterLab relies on the following technologies to work with the particular combination of web browser and any assistive technologies or plugins installed on your computer:

* HTML
* WAI-ARIA
* CSS
* JavaScript

These technologies are relied upon for conformance with the accessibility standards used.

### Limitations and alternatives

Despite our best efforts to ensure accessibility of JupyterLab, there may be some limitations. Below is a description of known limitations, and potential solutions. Please contact us if you observe an issue not listed below.

**Known limitations for JupyterLab:**

1. **Documents**: Documents written by the community may not include accessible content because we do not and cannot review every document that can be opened and edited in JupyterLab. To support accessible documents, we are drafting guidelines for accessible document content with an emphasis on Jupyter notebooks. Please report the issue to the author and [open an issue on jupyter/accessibility](https://github.com/jupyter/accessibility/issues/new) describing the problem and the behavior you expect so we may integrate it into our content guidelines.
    
2. **JupyterLab extensions**: JupyterLab extensions written by the community may not be accessible because JupyterLab extensions can be written by anyone in the community and have no standard review process. We do not and can not review every JupyterLab extension. To support accessible extensions, we encourage extension authors to use existing, accessible JupyterLab components for their extensions. We also provide periodic opportunities for community education on accessibility. Please report the issue to the author and let them know the [jupyter/accessibility](https://github.com/jupyter/accessibility/) community may be able to provide guidance.

### Assessment approach

Jupyter accessibility contributors assessed the accessibility of JupyterLab by the following approaches:

* Self-evaluation
* Regular automated testing to monitor for regressions (can be found at [jupyter/accessibility](https://github.com/jupyter/accessibility)
* User feedback

### Evaluation report

An evaluation for JupyterLab is available at: [jupyterlab/jupyterlab/issues/9399](https://github.com/jupyterlab/jupyterlab/issues/9399).


User reports on JupyterLab's accessibility are available at:[the jupyterlab/jupyterlab label `tag:accessibility`](https://github.com/jupyterlab/jupyterlab/labels/tag%3AAccessibility).

### Date

This statement was created on 16 May 2022 using the [W3C Accessibility Statement Generator Tool](https://www.w3.org/WAI/planning/statements/).