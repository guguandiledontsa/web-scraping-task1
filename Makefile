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
	@echo "Dependencies installed."

## Run linting (Pylint)
lint:
	@echo "Running Pylint..."
	pylint $(PY_FILES) --fail-under=8
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

## Run the main application
main:
	@echo "Running main.py..."
	python src/main/main.py
	@echo "main.py executed."

## Run everything: install, lint, and format
all: install lint format
	@echo "All tasks completed."
