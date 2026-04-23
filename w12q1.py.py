import pandas as pd
from sklearn.model_selection import train_test_split

# Sample dataset (safe, no CSV error)
data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 4, 6, 8, 10]
}

df = pd.DataFrame(data)

# Features and target
X = df[["X"]]
y = df["Y"]

# Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(X_train, X_test)