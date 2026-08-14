from sklearn.preprocessing import MinMaxScaler
data = [[10],
        [20],
        [30],
        [40],
        [50]]
scaler = MinMaxScaler()
normalized = scaler.fit_transform(data)
print(normalized)