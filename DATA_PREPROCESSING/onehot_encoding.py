from sklearn.preprocessing import OneHotEncoder
colors = [["Red"],
          ["Blue"],
          ["Green"],
          ["Red"]]
encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(colors)
print(encoded)