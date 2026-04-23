import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Basic info
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Plot histogram
df.hist()
plt.show()

# Correlation
print(df.corr())