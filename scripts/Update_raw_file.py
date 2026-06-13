import pandas as pd
from pathlib import Path

#Scanning raw folder for new files
raw_folder = Path("raw")
raw_files = list(raw_folder.glob("*.csv"))
if not raw_files:
    raise FileNotFoundError(
        "No CSV files found in raw/"
    )
df_dummy = pd.DataFrame()

for file in raw_files:
    df = pd.read_csv(file)
    df_dummy = pd.concat([df_dummy, df], ignore_index=True)

#Saving merged file to processed folder
df_dummy.to_csv("processed/raw_dataset.csv", index=False)
