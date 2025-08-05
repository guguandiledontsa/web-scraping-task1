.PHONY: install lint test format all main

PY_FILES := $(shell git ls-files '*.py')

install:
	@echo "Installing dependencies..."
	pip install --upgrade pip
	pip install -e .[dev]
	@echo "Installation complete."

lint:
	@echo "Linting with Pylint..."
	pylint $(PY_FILES) --fail-under=6
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
	papermill src/main/scraping.ipynb /dev/null
	@echo "Notebook execution finished."
	@echo "=== Scraping Log Output ==="
	@cat logs/scraping.log || echo "Log file not found."

all: install lint format
	@echo "All steps complete."
