import pandas as pd

# Load CSV file
df = pd.read_csv("data.csv")

# First 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

# Dataset info
print(df.info())