import matplotlib.pyplot as plt
hours = [1, 2, 3, 4, 5, 6]
marks = [40, 45, 55, 65, 72, 80]
plt.scatter(hours,marks)
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours Studied vs Marks")
plt.show()
