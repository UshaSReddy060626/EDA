import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6],
    "Study_Time": [1.1, 2.2, 2.8, 4.1, 5.2, 5.8],
    "Attendance": [60, 65, 70, 75, 80, 85]})
X = df[["Hours", "Study_Time", "Attendance"]]
vif = pd.DataFrame()
vif["Feature"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i)
    for i in range(X.shape[1])]
print(vif)