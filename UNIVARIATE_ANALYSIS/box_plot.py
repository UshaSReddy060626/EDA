import seaborn as sns
import matplotlib.pyplot as plt
marks = [45, 50, 52, 55, 56, 58, 60, 62, 65, 100]
sns.boxplot(y=marks)
plt.ylabel("Marks")
plt.title("Marks Distribution")
plt.show()