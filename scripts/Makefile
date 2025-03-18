# Define folders
PYTHON_FILES := $(shell find ../bin -name "*.py")
VENV_DIR=../env
DATA_DIR=../sample_data

.PHONY: default env update test lint gainers

# Show Makefile contents if no target is specified
default:
	@cat scripts/Makefile

# Ensure virtual environment exists
env:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv $(VENV_DIR); \
	fi
	@echo "Virtual environment is ready."

# Install dependencies inside the virtual environment
update: env
	@echo "Activating virtual environment and installing dependencies..."
	@.  $(VENV_DIR)/bin/activate && python -m pip install --upgrade pip && pip install -r ../requirements.txt
	@echo "Dependencies installed."

gainers:
	@echo "Running gainer fetch and process..."
	@PYTHONPATH=$(PWD)/.. ../env/bin/python -m bin.get_gainer $(SRC)

# Lint the code with pylint
lint:
	@echo "Running pylint..."
	$(VENV_DIR)/bin/pylint $(PYTHON_FILES)

# Run tests
test:
	PYTHONPATH=.. $(VENV_DIR)/bin/pytest -vv ../tests/

# Run lint and tests together
lint_and_test: lint test

# Normalize CSV files
normalize:
	@$(VENV_DIR)/bin/python bin/csv_normalizer.py
