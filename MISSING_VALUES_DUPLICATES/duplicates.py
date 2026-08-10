import pandas as pd
df = pd.DataFrame({
    "Name": ["Asha", "Ravi", "Priya", "Asha", "Kiran"],
    "Age": [20, 21, 19, 20, 22],
    "Marks": [85, 90, 78, 85, 92]})
print(df.duplicated())
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df)