import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.DataFrame({
    "Area": [1000, 1200, 1500, 1800, 2000],
    "Bedrooms": [2, 2, 3, 3, 4],
    "Actual_Selling_Price": [40, 50, 65, 75, 90]})
X = df[["Area", "Bedrooms"]]
y = df["Actual_Selling_Price"]
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,
    random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Actual Price:", y_test.values)
print("Predicted Price:", predictions)