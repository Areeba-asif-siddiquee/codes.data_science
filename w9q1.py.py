import pandas as pd
import matplotlib.pyplot as plt

data ={
  "a":100 ,
  "b":200
  }

df = pd.DataFrame(data)

# Draw boxplot
df.boxplot()
plt.show()

# Detect outliers using IQR
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Remove outliers
df_clean = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

print(df_clean)