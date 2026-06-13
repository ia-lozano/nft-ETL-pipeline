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
- Python
- SQLAlchemy
- Pandas
- Selenium

# Structure
mir4project/
├── analytics/
├── processed/
├── raw/
├── scripts/
├── tests/
├── README.md
└── requirements.txt

# Pipeline Workflow
Extract (Selenium)
↓
Merge Raw CSVs
↓
Transform / Deduplicate
↓
Load to MySQL

# Installation

## MacOS / Linux
python3 -m venv .venv 
source .venv/bin/activate

## Windows
python -m venv .venv 
.venv\Scripts\activate

Run: pip install -r requirements.txt

## Export your local MySQL password:

Mac/Linux:
export DB_PASSWORD='your_password'
Windows:
set DB_PASSWORD=your_password

cd to project folder
Run: python scripts/pipeline.py

## Load stage is optional and requires:
- local MySQL instance
- DB_PASSWORD environment variable


