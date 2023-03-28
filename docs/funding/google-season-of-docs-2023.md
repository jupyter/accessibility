# Proposal Title - organization name

<!---
Your proposal title should be short and specific. “Update ORGNAME Contributor Guide” is a good proposal title. “Documentation Improvements” is too vague; “Update Sections 5,7,23,99 of Contributor Guide, Create FAQ, and Create Style Guide” is too long.
-->

Create foundational user-focused accessibility documentation for JupyterLab

# About your organization

<!---
In this section, tell us about your organization or project in a few short paragraphs. What problem does your project solve? Who are your users and contributors? How long has your organization or project been in existence? Give some context to help us understand why funding your proposal would create a positive impact in open source and the world.
-->

[JupyterLab](https://jupyter.org/) is an extensible environment for interactive and reproducible computing based on the Jupyter Notebook. It allows scientists, researchers, engineers, journalists, students, and many other users to configure and arrange workflows combining code development, visualization and text inside a single web-based interface. Characterized by its powerful execution engine, Jupyter supports over 40 programming languages, including Python, Julia, R and Scala.

JupyterLab is a user interface comprising notebook manipulation, text editor, file browser, and terminal, among other development tools. It has a seamless integration with the most common scientific packages and is included in multiple downstream applications as a dependency. Moreover, JupyterLab is flexible, robust, and extensible by third-party and official extensions distributed via PyPi, conda, and other package managers.

Since its first release in 2018, JupyterLab has grown as an open source project, offering more features than just the Notebook interface. It is used by many applications and it has served as a reference for multiple web-based interfaces like [Google Codespaces](https://github.com/features/codespaces), [Google Colab](https://colab.research.google.com/) and [Coursera](https://coursera.org/), among others.

One part of that story of growth, adoption, and inclusivity that was overlooked for too long was the inclusion of disabled users and the implementation of accessibility best practices. That’s why during the past years, the Jupyter Accessibility team has been leading efforts to make the JupyterLab interface more accessible and usable by disabled users. There’s still much to do, but it’s vitally important—not just for JupyterLab but for the wider ecosystem of data science and open source—that this work continues.

# About your project

## Your project’s problem

<!---
Tell us about the problem your project will help solve. Why is it important to your organization or project to solve this problem?
-->

[The JupyterLab accessibility team](https://jupyter-accessibility.readthedocs.io/en/latest/index.html) has been concentrating its efforts on accessibility remediation through work on interface audits, testing events, improvements to UI/UX and automated testing. Due to the limited resources and the prioritization of such remediation work, documenting accessibility features has been a secondary priority. As more accessibility-focused improvements are added, it is becoming increasingly necessary that we provide a dedicated focus on adding user accessibility documentation for JupyterLab.

Through this project, we aim to create documentation primarily targeted at anyone with a temporary, situational, or permanent disability that wants or needs to use JupyterLab. We want to provide the JupyterLab community with a comprehensive guide about the accessibility features present in the application. For example, developing documentation that answers questions such as “What can and can’t I do in JupyterLab with accessibility accommodations?” and “How can I adjust JupyterLab to work better for me with assistive technology?”

## Your project’s scope

<!---
Tell us about what documentation your organization will create, update, or improve. If some work is deliberately not being done, include that information as well. Include a time estimate, and whether you have already identified organization volunteers and a technical writer to work with your project.
-->

This project includes:

- Creation of an accessibility section in JupyterLab documentation containing default accessibility settings and customizations inspired by VSCode's documentation https://code.visualstudio.com/docs/editor/accessibility
- Create user-focused documentation that summarizes the state of JupyterLab areas that have been audited for accessibility. This includes an approachable report on [keyboard navigation](https://github.com/jupyterlab/jupyterlab/issues/9399) and [400% zoom audit](https://github.com/Quansight-Labs/jupyterlab-accessible-themes/issues/34) results.

As a stretch goal, we would like to include:

- An authoring guide focused on best practices to generate accessible notebooks.

Work that is out of the scope of this project includes:

- Creation of developer-focused documentation
- Tutorials and workshops to present in conferences
- Live streams and social media engagement

The developer that will be mentoring this project has previously mentored successful GSoD in another project last year and has been involved in the accessibility remediation work for JupyterLab. We don’t have a technical writer for this project, but we intend to start the  application and selection process once we receive the acceptance by Google Season of Docs.

We estimate that this project will be completed by one technical writer working full-time in a span of six months.

## Measuring your project’s success

<!---
How will you know that your new documentation has helped solve your problem? What metrics will you use, and how will you track them?
-->

Even though JupyterLab users vary in their experience, knowledge and confidence of the application, there’s an overall unfamiliarity about the accessibility features available within it. This is primarily a result of the lack of reliable and official documentation that can guide users through different situations like adjusting theming, keyboard and assistive technologies support. There have been numerous questions raised about accessibility features in the issue tracker of the project, and in general, the community wants to move to more inclusive access to the information given that JupyterLab is one of the most common tools used in education, research and scientific development.

We will track two metrics to measure this documentation project's success. The first is the number of accessibility features documented; the second is the number of pages added regarding the audits for keyboard navigation and 400% zoom.

We would consider the project successful if, after finalizing this project:

- **At least 7** accessibility features are documented.
- **1 page** has been added describing audits in keyboard navigation and 400% zoom.

## Timeline

<!---
How long do you estimate this work will take? Are you able to break down the tech writer tasks by month/week?
The project overall will take approximately six months to complete. Once we have the technical writer in the team, we’ll spend the time as follows,
-->

| Month   | Action items |
| :--:    |      :---:   |
| Month 1 | Onboarding - setup of development environment and understanding of the current workflow for building, reviewing and deploying the documentation |
| Month 2 & 3 | Document JupyterLab’s accessibility features, and publish the documentation |
| Month 4 & 5 | Document the results from the keyboard navigation and 400% zoom audits. |
| Month 6 | Project completion - write the case study and one blog post |


# Project budget

<!---
You can include your budget in your proposal, or as a separate link. If your budget is fewer than ten items, we recommend including it in your proposal.
All budgets should be in US dollars. We expect grants to range from US$5000 to US$15000; if your project is outside of that range, please provide additional information to justify your budget.
We expect the bulk of your budget (60-70% minimum) to be allocated to the technical writer working on your project. We recommend budgeting on a per-project basis wherever possible.
We expect open source projects to use open source tools whenever possible; if your project absolutely requires funds for proprietary software licenses or support, please include a justification for the amount.
Other possible expenses include:
Design work to create branding, logos, templates, or other design assets for your documentation site
Minimal amounts (<US$200) for project swag (t-shirts or stickers for your participants). If you use the Season of Docs logo, it must be accompanied by your project or organization logo or name. Your swag may not use the name Google.
Minimal stipends for volunteers who take on considerable mentorship or guidance roles in the project (we recommend no more than $500 per volunteer, please)
Downstream donations to other open source projects should be no more than 10% of your budget total.
Include other budget items as needed, along with justification for the amount sought. Expense justifications should highlight how the expenditure will contribute to the success of the project as a whole.
-->

| Budget item | Amount | Running Total | Notes/Justifications |
| :--:    |      :---:   | :--:    |      :---:   |
| Technical writer that will update, test and publish new accessibility documentation |$10000 |$10000 |The mentors’ time will be provided as in-kind donation by [Quansight Labs](https://labs.quansight.org/) so the budget will be used in full for the technical writer’s compensation. |

# Additional information

<!--
Include here any additional information that is relevant to your proposal.
Previous experience with technical writers or documentation: If you or any of your mentors have worked with technical writers before, or have developed documentation, mention this in your application. Describe the documentation that you produced and the ways in which you worked with the technical writer. For example, describe any review processes that you used, or how the technical writer's skills were useful to your project. Explain how this previous experience may help you to work with a technical writer in Season of Docs.
-->

## Current state of JupyterLab documentation

JupyterLab documentation was first released for version 1.2. It has four main pillars: how to get started with the application, end-user guide, developer guide and how to contribute. As with any project, this documentation has grown organically as new features are implemented.

In addition to the JupyterLab documentation, there is also a dedicated website for Jupyter Accessibility. Right now, it works as a team compass for the Jupyter Accessibility project and as a reliable source for accessibility resources, efforts and community efforts.

## How JupyterLab documentation is built
JupyterLab’s documentation is written in Markdown and reStructuredText, and is rendered using Sphinx. It is then deployed automatically from the main JupyterLab repository. A development environment for contributing can be installed with Python and pip, and the current documentation contains a writing style guide and user interface naming conventions.

## Current documentation

- Latest JupyterLab version: https://JupyterLab.readthedocs.io/en/stable/
- Latest JupyterLab accessibility docs: https://jupyter-accessibility.readthedocs.io/en/latest/index.html
- Jupyter project website: https://jupyter.org/
- JupyterLab Github repository: https://github.com/JupyterLab/JupyterLab

## Contact information

If you are a technical writer interested in working in this project please reach out to Stephannie Jimenez at `sgacha@quansight.com`.
