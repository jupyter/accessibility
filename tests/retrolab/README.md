# Retrolab accessibility tests

## :package: Requirements

To run the tests in this directory you need the following pre-requisites:

- mamba
- python > 3.7
- nox
- pyyaml

you can install both nox and pyyaml from the command line with the following command:

```bash
python3 -m  pip install nox pyyaml
```

## :zap: Running the tests

1. Make sure you are in the correct directory:

    ```bash
    cd tests/retrolab
    ```

2. Run the test with nox from the command line:

    ```bash
    nox -s a11y_tests
    ```

 If you are invoking the nox command for the first time, this may take while to install the dependencies and run the tests.
