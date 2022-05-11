# JupyterLab accessibility tests

## :package: Requirements

To run the tests in this directory you need the following pre-requisites:

- mamba

- Your system must also meet the [Playwright system requirements](https://playwright.dev/docs/library#system-requirements).

## :zap: Running the tests

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

## :cloud: Running in Gitpod

As an alternative to running the tests locally on your own machine, you can run them in a cloud environment on Gitpod.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/jupyter/accessibility)

Once you are in the Gitpod workspace, run:

```bash
yarn test
```
