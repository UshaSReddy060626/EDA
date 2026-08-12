import seaborn as sns
import matplotlib.pyplot as plt
city = ["Bangalore", "Mumbai", "Delhi"]
salary = [65000, 60000, 55000]
sns.barplot(x=city, y=salary)
plt.xlabel("City")
plt.ylabel("Average Salary")
plt.title("Average Salary by City")
plt.show()