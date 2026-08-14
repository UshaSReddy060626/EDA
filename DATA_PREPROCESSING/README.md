# 📊 Data Preprocessing

Data preprocessing is the process of **cleaning, transforming, and preparing data** before using it for Machine Learning.

This section covers the major preprocessing techniques used to make data suitable for ML models.

---

## 📌 Topics Covered

* Standardization
* Normalization
* Label Encoding
* One-Hot Encoding
* Feature Engineering
* Feature Selection
* PCA
* Data Leakage

---

## 1. 📏 Standardization

Standardization transforms numerical features so that they have:

* Mean ≈ `0`
* Standard deviation ≈ `1`

### Formula

```text
z = (x - mean) / standard_deviation
```

### Python

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

Standardization is commonly useful for:

* Logistic Regression
* SVM
* KNN
* PCA
* Neural Networks

---

## 2. 📐 Normalization

Normalization scales numerical values to a fixed range, commonly:

```text
0 to 1
```

### Formula

```text
x_scaled = (x - min) / (max - min)
```

### Python

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_normalized = scaler.fit_transform(X)
```

---

## 3. 🏷️ Label Encoding

Label Encoding converts categorical values into numerical labels.

### Example

```text
Small  → 0
Medium → 1
Large  → 2
```

### Python

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

data["Size"] = encoder.fit_transform(data["Size"])
```

⚠️ Label Encoding can imply an order between categories, so it should be used carefully for nominal categorical data.

---

## 4. 🔢 One-Hot Encoding

One-Hot Encoding converts each category into a separate binary column.

### Example

```text
Color
-----
Red
Blue
Green
```

Becomes:

```text
Red  Blue  Green
1     0     0
0     1     0
0     0     1
```

### Python

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False)

encoded = encoder.fit_transform(data[["Color"]])
```

One-Hot Encoding is useful when categories do not have a natural order.

---

## 5. 🛠️ Feature Engineering

Feature engineering means **creating new useful features from existing data**.

### Example

Given:

```text
Height = 1.7
Weight = 70
```

We can create:

```text
BMI = Weight / Height²
```

### Python

```python
data["BMI"] = data["Weight"] / (data["Height"] ** 2)
```

Other examples include extracting:

* Year
* Month
* Day
* Day of week
* Age from date of birth
* Total price from quantity × price

Good feature engineering can help ML models identify useful patterns.

---

## 6. 🎯 Feature Selection

Feature selection means choosing the **most relevant features** for the model.

### Example

Suppose we have:

```text
Age
Salary
Height
Favorite_Color
Experience
Random_ID
```

After feature selection, we may keep:

```text
Age
Salary
Experience
```

### Benefits

* Reduces unnecessary features
* Can improve model performance
* Reduces training time
* Can reduce overfitting
* Improves interpretability

### Common Techniques

* Correlation
* Mutual Information
* Chi-Square
* Recursive Feature Elimination (RFE)
* Feature Importance

---

## 7. 📉 PCA — Principal Component Analysis

PCA is a **dimensionality reduction technique**.

It transforms a dataset with many features into a smaller number of new features called **principal components** while trying to preserve important information.

### Example

```text
Feature 1
Feature 2
Feature 3
Feature 4
Feature 5
```

Can potentially be reduced to:

```text
PC1
PC2
```

### Python

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)
```

PCA is affected by feature scale, so standardization is commonly performed before PCA.

```text
Raw Data
   ↓
Standardization
   ↓
PCA
   ↓
Reduced Features
   ↓
ML Model
```

---

## 8. 🚨 Data Leakage

Data leakage occurs when information that **should not be available during training** is accidentally provided to the model.

This can result in unrealistically high evaluation scores and poor performance on real-world data.

### Example

Suppose we want to predict whether a student will pass.

Features:

```text
Study Hours
Attendance
Previous Marks
Final Exam Result
```

If `Final Exam Result` is used as an input feature to predict whether the student passes, the model has access to information that reveals the answer.

This is **data leakage**.

### Correct Preprocessing

❌ Incorrect:

```python
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2
)
```

The scaler learned information from both training and testing data.

✅ Correct:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Key Rule

```text
Training Data → fit_transform()
Testing Data  → transform()
```

The test set should remain unseen during the learning stage of preprocessing.

---

# 🧠 Quick Comparison

| Technique           | Purpose                                             |
| ------------------- | --------------------------------------------------- |
| Standardization     | Scale data around mean 0 and standard deviation 1   |
| Normalization       | Scale values to a fixed range                       |
| Label Encoding      | Convert categories into numerical labels            |
| One-Hot Encoding    | Convert categories into binary columns              |
| Feature Engineering | Create useful new features                          |
| Feature Selection   | Select important features                           |
| PCA                 | Reduce dimensionality                               |
| Data Leakage        | Prevent unwanted information from entering training |

---

# 🔄 Complete Preprocessing Workflow

```text
Raw Dataset
     ↓
EDA ✅
     ↓
Train/Test Split
     ↓
Handle Missing Values
     ↓
Encode Categorical Data
     ↓
Feature Engineering
     ↓
Feature Selection
     ↓
Standardization / Normalization
     ↓
PCA (if required)
     ↓
Machine Learning Model
```

---

# 🎯 Key Takeaways

* **Standardization** → mean `0`, standard deviation `1`
* **Normalization** → usually scales values between `0` and `1`
* **Label Encoding** → categories → numbers
* **One-Hot Encoding** → categories → binary columns
* **Feature Engineering** → create useful features
* **Feature Selection** → keep important features
* **PCA** → reduce dimensions
* **Data Leakage** → prevent test/future information from influencing training

---

