## Requirements

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


## Testing

### Coverage report
```sh
poetry poe test
```

### Mutation testing

```sh
poetry poe mutmut
```
