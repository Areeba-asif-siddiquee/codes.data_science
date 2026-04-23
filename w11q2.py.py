import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Data
data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 4, 6, 8, 10]
}

df = pd.DataFrame(data)

X = df[["X"]]
y = df["Y"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Metrics
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print("MAE:", mae)
print("RMSE:", rmse)

# Plot
plt.figure()
plt.scatter(X, y, label="Actual")
plt.plot(X, y_pred, label="Predicted")
plt.legend()
plt.show()