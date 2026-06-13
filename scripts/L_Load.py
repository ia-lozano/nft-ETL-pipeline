import os
from sqlalchemy import create_engine
import pandas as pd

#sudo /usr/bin/python3 -m pip install sqlalchemy pymysql

#note to self: remember to use single quotes ' ' when pwd contains $ sign
#and plz do not hardcode password....

#Getting local exported pwd, resets after terminal session ends
password = os.getenv("DB_PASSWORD")
if not password:
    raise EnvironmentError(
        "\nDB_PASSWORD not found.\n"
        "Run:\n"
        "export DB_PASSWORD='your_password'\n"
        "Then execute again.")

#Creating engine with a previously created MySQL local DB
engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/mir4_DB")

#Pushing dataset to database
dataset = pd.read_csv("processed/final_dataset.csv")
dataset.to_sql("nft_data", engine, if_exists="replace", index=False)

engine.dispose()