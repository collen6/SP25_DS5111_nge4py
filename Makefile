default:
	@cat Makefile

env:
	python3 -m venv env
	. env/bin/activate
	pip install --upgrade pip

update: env
	. env/bin/activate
	pip install -r requirements.txt

# Create scripts directory if missing and scrape Yahoo Finance Gainers
ygainers.html:
	mkdir -p scripts
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > scripts/ygainers.html

# Convert Yahoo Finance HTML to CSV
ygainers.csv: ygainers.html
	python -c "import pandas as pd; raw = pd.read_html('scripts/ygainers.html'); raw[0].to_csv('scripts/ygainers.csv')"

# Create scripts directory if missing and scrape Wall Street Journal Gainers
wjsgainers.html:
	mkdir -p scripts
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 'https://www.wsj.com/market-data/stocks/us/movers' > scripts/wjsgainers.html

# Convert WSJ Gainers HTML to CSV
wjsgainers.csv: wjsgainers.html
	python -c "import pandas as pd; raw = pd.read_html('scripts/wjsgainers.html'); raw[0].to_csv('scripts/wjsgainers.csv')"
