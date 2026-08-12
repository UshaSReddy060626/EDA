import matplotlib.pyplot as plt
marks=[45, 48, 52, 55, 56, 60, 62, 65, 67, 70, 72, 75, 80, 85, 90]
plt.hist(marks,bins=5)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.show()