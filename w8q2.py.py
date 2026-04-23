import pandas as pd

df = pd.read_csv("data.csv")

# Remove rows with missing values
df = df.dropna()

# Filter rows where column A < 50
filtered = df[df["A"] < 50]

# Select specific columns
selected = df[["A", "B"]]

print(filtered)
print(selected)