.PHONY: install lint test format all main

PY_FILES := $(shell git ls-files '*.py')

install:
	@echo "Installing dependencies..."
	pip install --upgrade pip
	pip install -e .[dev]
	@echo "Installation complete."

lint:
	@echo "Linting with Pylint..."
	pylint $(PY_FILES) --fail-under=5
	@echo "Lint complete."

format:
	@echo "Formatting with Black..."
	black $(PY_FILES)
	@echo "Format complete."

test:
	@echo "Running unit tests..."
	python -m unittest discover -s tests -p "test_*.py"

main:
	@echo "Running scraping notebook..."
	papermill src/main/scraping.ipynb output.ipynb --log-output
	@echo "Notebook execution finished."

all: install lint format
	@echo "All steps complete."
