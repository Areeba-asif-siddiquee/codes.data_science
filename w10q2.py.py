import pandas as pd
import matplotlib.pyplot as plt

data = {
    "A": [10, 20, 30, 40],
    "B": [15, 25, 35, 45],
    "C": [5, 10, 15, 20]
}

df = pd.DataFrame(data)

# Scatter plot
plt.figure()
plt.scatter(df["A"], df["B"])
plt.xlabel("A")
plt.ylabel("B")
plt.title("Scatter Plot")
plt.show()

# Correlation heatmap (simple)
corr = df.corr()

plt.figure()
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)
plt.title("Correlation Heatmap")
plt.show()