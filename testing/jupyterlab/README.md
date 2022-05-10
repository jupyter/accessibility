# JupyterLab accessibility tests

## :package: Requirements

To run the tests in this directory you need the following pre-requisites:

- mamba

Your system must also meet the [Playwright system requirements](https://playwright.dev/docs/library#system-requirements).

## :zap: Running the tests

1. Make sure you are in the correct directory:

    ```bash
    cd testing/jupyterlab
    ```

2. Install the Python dependencies:

    ```bash
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
