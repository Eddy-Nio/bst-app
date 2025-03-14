.PHONY: all clean install test run lint

# Python interpreter
PYTHON := python3
VENV := venv
BIN := $(VENV)/bin

# Installation
$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install -r requirements.txt

# Main targets
all: install

install: $(VENV)/bin/activate

clean:
	rm -rf $(VENV) __pycache__ .pytest_cache
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

test: install
	$(BIN)/python -m pytest tests/ -venv

run: install
	$(BIN)/python run.py

lint: install
	$(BIN)/flake8 .
	$(BIN)/black .
