import pandas as pd
df = pd.DataFrame({
    "Salary": [25000, 28000, 30000, 32000, 35000, 38000, 40000, 150000]})
print("Original Data:")
print(df)

# 1. Remove outlier
remove_df = df[df["Salary"] < 100000]
print("After Removing Outlier:")
print(remove_df)


#Correct outlier
correct_df = df.copy()
correct_df.loc[correct_df["Salary"] == 150000, "Salary"] = 50000
print("After Correcting Outlier:")
print(correct_df)


#Cap outlier
cap_df = df.copy()
upper_limit = 50000
cap_df["Salary"] = cap_df["Salary"].clip(upper=upper_limit)
print("After Capping Outlier:")
print(cap_df)