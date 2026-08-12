import seaborn as sns
import matplotlib.pyplot as plt
marks = [45, 48, 52, 55, 56, 60, 62, 65, 67, 70, 72, 75, 80, 85, 90]
sns.kdeplot(marks)
plt.xlabel("Marks")
plt.ylabel("Density")
plt.title("KDE Plot of Marks")
plt.show()