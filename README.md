🚀 README.md – Project Setup Guid
md
# 🚀 Web Scraping Project with Headless Chrome & Makefile Automation

This project automates web scraping tasks using **headless Chrome**, a **Makefile**, and a **virtual environment** for dependency management.

---

## **1️⃣ Install Headless Chrome**
Before running the project, install **Google Chrome (headless mode)** using the provided script:

```bash
bash install_chrome_headless.sh

To verify the installation, run:

google-chrome-stable --headless --disable-gpu --dump-dom https://example.com/

If you see an HTML response, Chrome is set up correctly ✅.

2️⃣ Set Up Virtual Environment & Install Dependencies
Ensure all required Python packages are installed by running:

make update

This will:

Create a virtual environment.
Activate the virtual environment.
Install dependencies from requirements.txt (currently pandas and lxml).
If make update fails, manually create and activate the virtual environment:

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

3️⃣ Run Web Scraping Jobs

🔹 Scrape Yahoo Finance Gainers

make ygainers.csv

This will:

Use headless Chrome to scrape Yahoo Finance.
Save the HTML page as ygainers.html.
Extract data into ygainers.csv.

🔹 Scrape Wall Street Journal Gainers

make wjsgainers.csv

This will:

Use headless Chrome to scrape WSJ.
Save the HTML page as wjsgainers.html.
Extract data into wjsgainers.csv.


4️⃣ Verify Project Structure
To confirm that everything is set up correctly, run:

tree -I env

Expected output:

.
├── Makefile
├── README.md
├── install_chrome_headless.sh
├── init.sh
├── requirements.txt
├── scripts/
│   ├── scrape_yahoo.py
│   ├── scrape_wsj.py
├── data/
│   ├── ygainers.html
│   ├── ygainers.csv
│   ├── wjsgainers.html
│   ├── wjsgainers.csv
└── env/ (ignored)


5️⃣ Final Steps

Before shutting down your machine, verify:

Headless Chrome is working (google-chrome-stable --version).
The virtual environment is active (source env/bin/activate).
Scraping commands run successfully (make ygainers.csv && make wjsgainers.csv).
If everything works, commit and push your changes:

git add .
git commit -m "Updated README with project setup details"
git push origin main

✅ Project is Ready to Run!

Now you can use make to automate tasks and process data efficiently. 

🚀# SP25_DS5111_nge4py
DS 5111 Repo
