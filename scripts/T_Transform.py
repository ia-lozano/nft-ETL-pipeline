import pandas as pd
import re

#Loading raw_dataset
dataset = pd.read_csv("processed/raw_dataset.csv")

#Removing non ascii chars from raw_dataset.csv
#Useful to generate keep unique names, remove duplicates later
# and avoid problems when loading to a SQL db.
def normalize_name(name:str) -> str:
    '''
    Params: string potentially containing non ascii chars.
    Output: string with no ascii chars.
    '''
    fixed_name = ""
    for char in name:
        if char.isascii():
            fixed_name += char
        else:
            fixed_name += str(ord(char))
    return fixed_name.replace(" ", "")

#Applying normalization to "name" column
dataset["name"] = dataset["name"].apply(normalize_name)

#Removing annoying characters to avoid SQL problems
dataset["name"] = dataset["name"].apply(lambda x: re.sub(r"[^A-Za-z0-9]", "", x))

#Removing duplcated names (character name must be unique), so this line
# removes double-scraped characters
dataset["name"] = dataset["name"].str.strip()
dataset = dataset.drop_duplicates(subset=["name", "price"])

#Rewritting dataset
dataset.to_csv("processed/final_dataset.csv", index=False)


