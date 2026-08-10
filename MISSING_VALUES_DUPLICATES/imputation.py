import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Age": [20, 21, np.nan, 22, 23],
    "Marks": [80, 85, 90, np.nan, 95],
    "City": ["Bangalore", "Mumbai", np.nan, "Bangalore", "Bangalore"]})
print("Before Imputation:")
print(df)

# Mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Median
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

# Mode
df["City"] = df["City"].fillna(df["City"].mode()[0])
print("\nAfter Imputation:")
print(df)