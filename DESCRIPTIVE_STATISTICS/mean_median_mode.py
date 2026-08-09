import pandas as pd
df=pd.DataFrame({"Marks":[67,66,90,66,54,78,43]})
print(df["Marks"].mean())

#median
print(df["Marks"].median())

#mode
print(df["Marks"].mode())

#covert the result to list
print(df["Marks"].mode().tolist())