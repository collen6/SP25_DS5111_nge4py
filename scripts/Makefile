# Define folders
<<<<<<< HEAD
PYTHON_FILES := $(shell find ../bin -name "*.py")
=======
PYTHON_FILES=$(shell find . -type f -name "*.py" ! -path "./env/*")
>>>>>>> bc920dcc2f4f04805a20c0ca8e7c6a436d8dccb8
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
	@source  $(VENV_DIR)/bin/activate && python -m pip install --upgrade pip && pip install -r ../requirements.txt
	@echo "Dependencies installed."

gainers:
	@echo "Running gainer fetch and process..."
	@PYTHONPATH=$(PWD)/.. ../env/bin/python -m bin.get_gainer $(SRC)

# Lint the code with pylint
lint:
	echo "Running pylint..."
	$(VENV_DIR)/bin/pylint /home/ubuntu/SP25_DS5111_nge4py/bin/*.py

# Run tests
test:
	$(VENV_DIR)/bin/pytest -vv /home/ubuntu/SP25_DS5111_nge4py/tests

# Run lint and tests together
lint_and_test: lint test

# Normalize CSV files
normalize:
	@$(VENV_DIR)/bin/python bin/csv_normalizer.py
