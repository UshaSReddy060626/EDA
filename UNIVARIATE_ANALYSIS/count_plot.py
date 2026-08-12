import seaborn as sns
import matplotlib.pyplot as plt
cities = ["Bangalore","Mumbai","Bangalore","Delhi","Mumbai","Bangalore","Delhi"]
sns.countplot(x=cities)
plt.xlabel("City")
plt.ylabel("Count")
plt.title("Number of People by City")
plt.show()