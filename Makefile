.PHONY: install lint test format all

# ---------------------------------------------------------------------
# Variables
# ---------------------------------------------------------------------

# Find all Python files in the current directory and subdirectories
PY_FILES := $(shell find . -name "*.py")

# Macro: run a command only if Python files exist
define if_files_exist
	@if [ -z "$(PY_FILES)" ]; then \
		echo "No Python files found. Skipping $1."; \
	else \
		$2; \
	fi
endef

# ---------------------------------------------------------------------
# Targets
# ---------------------------------------------------------------------

## Install all required tools
install:
	@echo "Installing Python dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "Dependencies installed."

## Run linting
lint:
	@echo "Running Pylint..."
	$(call if_files_exist,lint,pylint $(PY_FILES) --fail-under=8)
	@echo "Pylint finished."

## Format code using Black
format:
	@echo "Formatting code with Black..."
	$(call if_files_exist,format,black $(PY_FILES))
	@echo "Black formatting finished."

## Run unit tests (Placeholder for future tests)
test:
	@echo "No tests defined yet. Skipping."
	# python -m unittest discover -s src/tests -t src

## Run everything: install, lint, and format
all: install lint format
	@echo "All tasks completed."
# ---------------------------------------------------------------------