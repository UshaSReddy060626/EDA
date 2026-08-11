import numpy as np
data = np.array([10, 12, 14, 15, 16, 18, 20, 22, 24, 100])
mean = np.mean(data)
std = np.std(data)
z_scores = (data - mean) / std
print(z_scores)
outliers = data[np.abs(z_scores) > 3]
print("Potential Outliers:", outliers)