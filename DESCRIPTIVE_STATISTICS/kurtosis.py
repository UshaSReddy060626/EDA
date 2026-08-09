import pandas as pd
df=pd.DataFrame({"Marks":[67,89,90,66,54,78,43]})
print(df["Marks"].kurt())
