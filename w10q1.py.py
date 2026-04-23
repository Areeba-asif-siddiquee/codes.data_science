import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (no CSV error)
data = {
    "Year": [2020, 2021, 2022, 2023],
    "Sales": [100, 150, 200, 250]
}

df = pd.DataFrame(data)

# Line plot
plt.figure()
plt.plot(df["Year"], df["Sales"], marker='o')
plt.title("Line Plot")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()

# Bar plot
plt.figure()
plt.bar(df["Year"], df["Sales"])
plt.title("Bar Plot")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()