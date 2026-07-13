# NFT ETL Pipeline
This project extracts nft character data from XDraco.com (Mir4 NFT marketplace) using Selenium
to generate raw CSV files. Then cleans the data and merges the raw files into a unified dataset which
will be pushed to a local MySQL instance.

# Features
- Extraction with Selenium.
- Data cleaning: Removes troublesome characters for MySQL and name/price duplicates.
- Generates .csv files that can be analyzed later.
- Pushes the dataset to a local MySQL instance.

# TechStack
- Python 3.14
- SQLAlchemy
- Pandas
- Selenium

# Project Structure

```plaintext
mir4project/
├── analytics/      # SQL, notebooks and analysis
├── processed/      # merged and transformed datasets
├── raw/            # scraped CSV files
├── scripts/        # ETL scripts
├── tests/          # unit tests (future me's problem)
├── README.md
└── requirements.txt
```

# Pipeline Workflow

```plaintext
Extract (Selenium) 
↓ 
Merge Raw CSVs 
↓
Transform / Deduplicate 
↓ 
Load to MySQL
```

# Installation

## MacOS / Linux
python3 -m venv .venv <br>
source .venv/bin/activate

## Windows
python -m venv .venv <br>
.venv\Scripts\activate

Run: pip install -r requirements.txt

## Export your local MySQL password:

Mac/Linux:<br>
export DB_PASSWORD='your_password'<be>
Windows:<br>
set DB_PASSWORD=your_password

cd to project folder<br>
Run: python scripts/pipeline.py

## Load stage is optional and requires:
- local MySQL instance
- DB_PASSWORD environment variable

