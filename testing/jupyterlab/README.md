# JupyterLab accessibility tests

## :package: Requirements

To run the tests in this directory you need the following pre-requisites:

- mamba (or conda)
- Your system must also meet the [Playwright system requirements](https://playwright.dev/docs/library#system-requirements)

## :zap: Running the tests

You can run tests locally on your machine, or remotely in the cloud.

At the time of this writing, we have configured the tests to only run with
Chromium, but you can
[test other browsers](https://github.com/MarcusFelling/demo.playwright/blob/main/accessibility/playwright.config.ts)
by modifying the `playwright.config.ts` file.
### :laptop: Locally

1. Make sure you are in the correct directory:

    ```bash
    cd testing/jupyterlab
    ```

2. Install the Python dependencies:

    ```bash
    # if using conda
    conda env create -f environment.yml

    # if using mamba
    mamba env create -f environment.yml
    ```

3. Install the Node.js dependencies:

    ```bash
    yarn install
    npx playwright install
    ```

4. Run the tests:

    ```bash
    yarn test
    ```

Your console should output a local url that you can open in your browser to see
the test results:

    http://127.0.0.1:9323

When you click on a test result, if it does not seem particularly readable, then
look for a link to an HTML report and follow that link.

### :cloud: Running in Gitpod

As an alternative to running the tests locally on your own machine, you can run them in a cloud environment on Gitpod.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/jupyter/accessibility)

Once you are in the Gitpod workspace, run:

```bash
yarn test
```

The Gitpod console should output a local url that you can open in your browser
to see the test results:

    http://127.0.0.1:9323

When you click on a test result, if it does not seem particularly readable, then
look for a link to an HTML report and follow that link.

In case you're wondering how you can open a local url from a cloud environment,
Gitpod opens a remote session in VS Code (or other supported editor) and sets it
up to proxy the local url to its remote server address.
