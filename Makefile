.PHONY: install lint test format all main

PY_FILES := $(shell git ls-files '*.py')

install:
	@echo "Installing dependencies..."
	pip install --upgrade pip
	pip install -e .[dev]
	@echo "Installation complete."

lint:
	@echo "Linting with Pylint..."
	pylint $(PY_FILES)
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
	jupyter nbconvert --to script src/main/scraping.ipynb --stdout | python
	@echo "Notebook execution finished."

all: install lint format
	@echo "All steps complete."
