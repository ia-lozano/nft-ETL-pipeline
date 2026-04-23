import pandas as pd
dataset = pd.read_csv("processed/final_dataset.csv")

print(dataset.shape[0])
print(dataset.columns)
print(dataset.dtypes)
