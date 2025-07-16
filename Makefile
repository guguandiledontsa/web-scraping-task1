.PHONY: install lint test format all

# Find all Python files in the current directory and subdirectories
PY_FILES := $(shell find . -name "*.py")

## Install all required tools
install:
	@echo "Installing Python dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "Dependencies installed."

## Run linting
lint:
	@echo "Running Pylint..."
	pylint $(PY_FILES) --fail-under=8
	@echo "Pylint finished."

## Run unit tests (Placeholder for future tests)
test:
	@echo "No tests defined yet. Skipping."
	# python -m unittest discover -s src/tests -t src

## Format code using Black
format:
	@echo "Formatting code with Black..."
	black $(PY_FILES)
	@echo "Black formatting finished."

## Run everything (install, lint, format - test is optional for now)
all: install lint format
	@echo "All tasks completed."