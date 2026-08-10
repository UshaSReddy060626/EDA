# 🧹 Missing Values & Duplicates

This section focuses on identifying and handling **missing values** and **duplicate records** in datasets using Python and Pandas.

These are important data-cleaning steps in Exploratory Data Analysis because real-world datasets often contain incomplete or repeated information.

## 📚 Concepts Learned

### 🔹 Missing Value Detection

Learned how to identify missing values using:

```python
df.isnull()
```

To count missing values in each column:

```python
df.isnull().sum()
```

`True` indicates that a value is missing, while `False` indicates that a value is present.

---

### 🔹 Removing Missing Values

Learned how to remove rows containing missing values using:

```python
df.dropna()
```

Columns can also be removed when necessary:

```python
df.drop(columns=["ColumnName"])
```

Removing missing data should be done carefully because it can result in the loss of useful observations.

---

### 🔹 Imputation

Learned that **imputation** means filling missing values with reasonable replacement values.

#### Mean Imputation

Used for numerical data when the mean is an appropriate representation.

```python
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```

#### Median Imputation

Useful when numerical data is skewed or contains extreme values.

```python
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
```

#### Mode Imputation

Useful for categorical data.

```python
df["City"] = df["City"].fillna(df["City"].mode()[0])
```

---

### 🔹 Duplicate Detection

Learned how to detect duplicate rows using:

```python
df.duplicated()
```

To count duplicate rows:

```python
df.duplicated().sum()
```

---

### 🔹 Duplicate Removal

Learned how to remove duplicate rows using:

```python
df = df.drop_duplicates()
```

Duplicates can also be identified based on selected columns:

```python
df.duplicated(subset=["Email"])
```

and removed using:

```python
df = df.drop_duplicates(subset=["Email"])
```

---

## 🛠️ Library Used

```python
import pandas as pd
import numpy as np
```

**Pandas** was used for dataset inspection, missing-value handling, and duplicate detection/removal.

**NumPy** was used to create `NaN` values for practice.

---

## 🧠 Key Takeaways

* Missing values represent unavailable or unknown information.
* `isnull()` detects missing values.
* `isnull().sum()` counts missing values by column.
* `dropna()` removes rows containing missing values.
* `fillna()` replaces missing values.
* Mean, median, and mode can be used for simple imputation depending on the data.
* Median can be useful for skewed numerical data or data with extreme values.
* Mode is useful for categorical data.
* `duplicated()` detects duplicate rows.
* `duplicated().sum()` counts duplicate rows.
* `drop_duplicates()` removes duplicate rows.
* Missing-value handling and duplicate removal should be based on the dataset rather than applied blindly.
* During ML preprocessing, imputation should be fitted using training data to avoid data leakage.

---

## 🔄 Data Cleaning Workflow

```text
Raw Dataset
     ↓
Check Missing Values
     ↓
isnull().sum()
     ↓
Handle Missing Values
     ↓
Drop or Impute
     ↓
Check Duplicates
     ↓
duplicated().sum()
     ↓
Remove Duplicates
     ↓
Clean Dataset
```

---

## 🎯 Goal

Learn how to transform a dataset containing:

```text
Missing Values
      +
Duplicate Records
```

into a cleaner dataset that is ready for further **Exploratory Data Analysis and Machine Learning preprocessing**.

---

**Missing Values & Duplicates 🧹 — Learning through Python, Pandas, and practice.**
