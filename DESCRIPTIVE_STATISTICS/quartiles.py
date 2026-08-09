import pandas as pd
df=pd.DataFrame({"Marks":[67,89,90,66,54,78,43]})
print(df["Marks"].quantile(0.25))
print(df["Marks"].quantile(0.50))
print(df["Marks"].quantile(0.75))