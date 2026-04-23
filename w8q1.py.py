import pandas as pd

df = pd.read_csv("data.csv")

# Rename columns
df.columns = ["A", "B", "C", "D"]   # give new names

# OR rename specific columns
df.rename(columns={"old1": "new1", "old2": "new2"}, inplace=True)

# Change data types
df["A"] = df["A"].astype(int)
df["B"] = df["B"].astype(float)
df["C"] = df["C"].astype(str)

print(df.dtypes)