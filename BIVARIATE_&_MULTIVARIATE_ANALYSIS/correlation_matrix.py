import pandas as pd
df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Sleep": [8, 7, 7, 6, 6, 5, 5, 4],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "Marks": [40, 45, 50, 58, 65, 70, 78, 85],
    "Gender": ["F", "M", "F", "M", "F", "M", "F", "M"],
    "Passed": ["No", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]})
corr = df[
    ["Hours", "Sleep", "Attendance", "Marks"]
].corr()
print(corr)