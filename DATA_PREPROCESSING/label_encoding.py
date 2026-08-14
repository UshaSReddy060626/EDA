from sklearn.preprocessing import LabelEncoder
sizes = ["Small", "Medium", "Large", "Medium", "Small"]
encoder = LabelEncoder()
encoded = encoder.fit_transform(sizes)
print(encoded)