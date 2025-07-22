.PHONY: install lint test format all

# ---------------------------------------------------------------------
# Variables
# ---------------------------------------------------------------------

# Find all Python files in the current directory and subdirectories
# Using 'git ls-files' is reliable if Git is installed.
PY_FILES := $(shell git ls-files '*.py')

# ---------------------------------------------------------------------
# Targets
# ---------------------------------------------------------------------

## Install all required tools
install:
	@echo "Installing Python dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .
	@echo "Dependencies installed."

## Run linting (Pylint)
lint:
	@echo "Running Pylint..."
	pylint $(PY_FILES) --fail-under=6
	@echo "Pylint finished."

## Format code using Black
format:
	@echo "Formatting code with Black..."
	black $(PY_FILES)
	@echo "Black formatting finished."

## Run unit tests (Placeholder for future tests)
test:
	@echo "No tests defined yet. Skipping."
	# python -m unittest discover -s src/tests -t src
	python -m unittest discover -s tests -p "test_*.py"

## Run the main application
main:
	@echo "Running scrapper.py..."
	# python -m main.scraper
	jupyter nbconvert --to script src/main/scraping.ipynb --stdout | python
	@echo "scraper.py done."

## Run everything: install, lint, and format
all: install lint format
	@echo "All tasks completed."
