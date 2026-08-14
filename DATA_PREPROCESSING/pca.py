import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
X = np.array([
    [170, 60],
    [172, 62],
    [175, 65],
    [178, 70],
    [180, 72]
])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=1)
X_pca = pca.fit_transform(X_scaled)
print("Original data:")
print(X)
print("\nPCA data:")
print(X_pca)