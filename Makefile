SCRIPTS := scripts
MAIN := $(SCRIPTS)/main.py
VENV := .venv
BIN := $(VENV)/bin
PRE_COMMIT := $(BIN)/pre-commit
PYTHON := $(BIN)/python

run-etl:
	PYTHONPATH=. $(PYTHON) $(MAIN)

bootstrap:
	@poetry install
	@$(PRE_COMMIT) install

docker-pull:
	@docker pull metabase/metabase:v0.37.2

clean:
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +

clean-all: clean
	@rm -r $(VENV)

format: clean
	@poetry run black $(SCRIPTS)

lint:
	@poetry run flake8 $(SCRIPTS)
