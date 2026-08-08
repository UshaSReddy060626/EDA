import pandas as pd
data={
    "Name":["Usha","Aarav","Keerthi","Aarush"],
    "Age":[21,23,21,20],
    "Marks":[95,95,93,94],
    "City":["Tumkur","Banglore","Mumbai","Chennai"]
}
df=pd.DataFrame(data)
print(df)
