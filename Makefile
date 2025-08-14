.PHONY: install lint test format all main preview_csvs

install:
@echo "Installing dependencies..."
pip install --upgrade pip
pip install -e .[dev]
@echo "Installation complete."

lint:
@echo "Linting with Pylint..."
pylint $(shell git ls-files '*.py') --fail-under=5
@echo "Lint complete."

format:
@echo "Formatting with Black..."
black $(shell git ls-files '*.py')
@echo "Format complete."

test:
@echo "Running unit tests..."
python -m unittest discover -s tests -p "test_*.py"

main:
@echo "Running scraping notebook..."
papermill src/main/scraping.ipynb output.ipynb --log-output
@echo "Notebook execution finished."
@$(MAKE) preview_csvs

preview_csvs:
@echo "Previewing CSV files ..."
@for file in src/main/data/*.csv; do \
	if [ -f "$$file" ]; then \
		echo "---- $$file ----"; \
		head -n 10 "$$file"; \
	else \
		echo "No CSV files found in $(DATA_DIR)"; \
	fi \
done

all: install lint format
@echo "All steps complete."