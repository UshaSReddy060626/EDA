import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6],
    "Sleep": [8, 7, 7, 6, 6, 5],
    "Attendance": [60, 65, 70, 75, 80, 85],
    "Marks": [40, 45, 50, 58, 65, 70]})
sns.pairplot(df)
plt.show()