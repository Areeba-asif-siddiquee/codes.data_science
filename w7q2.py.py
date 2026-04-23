import pandas as pd

# Load CSV file
df = pd.read_csv("data.csv")

# First 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

# Dataset info
print(df.info())


print(df.iloc[:, 1].mean())
print(df.iloc[0:5, 2:4].mean())
print(df.sum(axis=1))
row_avg = df.mean(axis=1)
print(row_avg.max())