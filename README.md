# Maklai Python Intership Test Task

## Table of contents

1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)

### Description

A simple web-service that generates paraphrases from a given parse tree. Contains one endpoint `paraphrase`, that
accepts two arguments: `tree (str)` and `limit (int)` and returns a json with paraphrases. In case of an error
returns json with error message;

#### Technology stack

- flask - web framework
- marshmallow - serialization for api
- pytest - testing framework
- nltk - working with parse trees
- black - keeping single code style
- flake8 - static code checking
- make - task runner
- poetry - environment and dependency manager

#### Structure

All source code located in `src/` directory:
- `core/` - core, where application factory is located
- `api/` - controllers and schemas
- `services/` - directory for services, business logic

All tests located in `tests/` directory;

### Installation

Clone project:

```bash
$ git clone https://github.com/dieisabel/maklai-python-intership-test-task
```

Install dependencies using poetry:

```bash
$ poetry install
```

### Usage

Start development server using:

```bash
$ make run
```

Run tests:

```bash
$ make test
```

Lint:

```bash
$ make lint
```

Enter flask shell:

```bash
$ make shell
```
