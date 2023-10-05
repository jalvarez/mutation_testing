# Mutation testing

This repository contains the code used in the PyConES 2023 talk "X-Men: How a bunch of mutants can help you to improve 
your tests?".

It is adaptation of the original code kata
[**Using Mutation Testing to Weed Out Fake Unit Tests**](https://github.com/vmzakharov/mutate-test-kata) using
the package [mutmut](https://github.com/boxed/mutmut) as mutation tester.

## Requirements

The following tools are required to run the repository code:

### Python 3.10

Install python 3.10 with pypenv, and configure to use

```sh
pyenv install 3.10
pyenv local 3.10
pyenv versions
```

### Poetry

Install poetry in runtime python system

```sh
pip3 install poetry
```

### PoeThePoet

Install poethepoet to run the scripts into the project using poetry

```sh
poetry self add 'poethepoet[poetry_plugin]'
```

### Configure poetry

```sh
poetry env use 3.10
poetry install
```


## Workflow

We added some commands that can help you to resolve the kata:

### Init

To initialise mutmut, run the mutation tester and get the first results:
```sh
poetry poe init
```

### Launch tests

To run the tests and get the coverage report:
```sh
poetry poe pytest
```

### Show and apply a mutant

To show the mutant and apply this mutant to our code, and get the test:
```sh
poetry poe select [mutant identifier]
```


## Solving

The repository contains the branch [a solution](../../tree/a-solution), which contains a sequence of steps to eliminate all the mutants.

However, this solution does not raise all the test smells suggested by the original kata. For example, it didn't catch the bug in the `test_leading_trailing_spaces_removed_from_employee_name` test.