POETRY = poetry

FLASK       = $(POETRY) run flask
FLASK_FLAGS = --app $(FACTORY)
PYTEST      = $(POETRY) run pytest
FACTORY     = src/factory:create_application
BLACK       = $(POETRY) run black
FLAKE8      = $(POETRY) run flake8

SRC = src

.PHONY: all
all: run shell test
default: test run

run:
	$(FLASK) $(FLASK_FLAGS) run

shell:
	$(FLASK) $(FLASK_FLAGS) shell

test:
	$(PYTEST)

lint:
	$(BLACK) $(SRC)
	$(FLAKE8) $(SRC)
