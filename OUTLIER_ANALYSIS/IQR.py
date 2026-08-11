import pandas as pd
data = pd.Series([10, 12, 14, 15, 16, 18, 20, 22, 24, 100])
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

#detecting outliers
outliers = data[
    (data < lower_bound) |
    (data > upper_bound)]
print("Outliers:")
print(outliers)