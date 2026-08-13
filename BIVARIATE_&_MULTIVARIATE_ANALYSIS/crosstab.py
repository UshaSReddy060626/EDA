import pandas as pd
df = pd.DataFrame({
    "Gender": ["F", "M", "F", "M", "F"],
    "Passed": ["Yes", "No", "Yes", "Yes", "No"]})
result = pd.crosstab(df["Gender"], df["Passed"])
print(result)