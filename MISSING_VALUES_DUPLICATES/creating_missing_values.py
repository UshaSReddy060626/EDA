import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Asha", "Ravi", "Priya", "Arun"],
    "Age": [20, 21, np.nan, 20],
    "Marks": [85, 90, 78, np.nan]})
print(df)