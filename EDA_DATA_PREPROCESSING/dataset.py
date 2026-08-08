import pandas as pd
data={
    "Name":["Usha","Aarav","Keerthi","Aarush"],
    "Age":[21,23,21,20],
    "Marks":[95,95,93,94],
    "City":["Tumkur","Banglore","Mumbai","Chennai"]
}
df=pd.DataFrame(data)
print(df.shape)
print(df.columns)
#to convert it into list
print(df.columns.tolist())
print(df.dtypes)
print(df.memory_usage())
print(df.memory_usage(deep=True).sum())
print(df.info(memory_usage="deep"))
print(df["City"].unique())
print(df["City"].nunique())
print(df.info())
print(df.describe())