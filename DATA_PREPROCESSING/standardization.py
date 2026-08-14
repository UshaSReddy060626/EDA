from sklearn.preprocessing import StandardScaler
data = [[20, 30000],
        [25, 50000],
        [30, 80000],
        [35, 100000],
        [40, 150000]]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
print(scaled_data)