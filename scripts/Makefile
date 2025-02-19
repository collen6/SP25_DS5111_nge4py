# Define folders
VENV_DIR=../env
DATA_DIR=../sample_data

.PHONY: default env update test ygainers ygainers.html ygainers.csv wjsgainers wjsgainers.html wjsgainers.csv

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

# Fetch Yahoo Finance gainers (HTML)
$(DATA_DIR)/ygainers.html:
	@mkdir -p $(DATA_DIR)
	@echo "Fetching Yahoo Finance gainers..."
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > $(DATA_DIR)/ygainers.html
	@echo "Saved Yahoo gainers to $(DATA_DIR)/ygainers.html."

# Convert Yahoo Finance HTML to CSV
$(DATA_DIR)/ygainers.csv: $(DATA_DIR)/ygainers.html
	@echo "Converting Yahoo Finance gainers to CSV..."
	python -c "import pandas as pd; raw = pd.read_html('$(DATA_DIR)/ygainers.html'); raw[0].to_csv('$(DATA_DIR)/ygainers.csv', index=False)"
	@echo "Saved Yahoo gainers to $(DATA_DIR)/ygainers.csv."

# Fetch WSJ gainers (HTML)
$(DATA_DIR)/wjsgainers.html:
	@mkdir -p $(DATA_DIR)
	@echo "Fetching Wall Street Journal gainers..."
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 'https://www.wsj.com/market-data/stocks/us/movers' > $(DATA_DIR)/wjsgainers.html
	@echo "Saved WSJ gainers to $(DATA_DIR)/wjsgainers.html."

# Convert WSJ gainers HTML to CSV
$(DATA_DIR)/wjsgainers.csv: $(DATA_DIR)/wjsgainers.html
	@echo "Converting WSJ gainers to CSV..."
	python -c "import pandas as pd; raw = pd.read_html('$(DATA_DIR)/wjsgainers.html'); raw[0].to_csv('$(DATA_DIR)/wjsgainers.csv', index=False)"
	@echo "Saved WSJ gainers to $(DATA_DIR)/wjsgainers.csv."
