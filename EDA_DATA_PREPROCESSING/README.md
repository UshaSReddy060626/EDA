# 📊 Day 01 – Dataset Understanding

Today, I started ** EDA & Data Preprocessing** of my Machine Learning roadmap.

The goal of today's learning was to understand a dataset before performing analysis or training a machine learning model.

## 📚 Topics Covered

### 🔹 Shape

Learned how to determine the number of rows and columns in a dataset using:

```python
df.shape
```

The output follows:

```text
(rows, columns)
```

### 🔹 Columns

Learned how to inspect the names of all columns using:

```python
df.columns
df.columns.tolist()
```

### 🔹 Data Types

Learned how to identify the data type of each column using:

```python
df.dtypes
```

Common data types include:

* `int64` – Integer values
* `float64` – Decimal values
* `object` – Usually text/string data
* `bool` – True/False values

### 🔹 Memory Usage

Learned how to inspect the memory used by a DataFrame using:

```python
df.memory_usage()
```

For deeper memory inspection:

```python
df.memory_usage(deep=True)
```

Total memory can be calculated using:

```python
df.memory_usage(deep=True).sum()
```

### 🔹 Unique Values

Learned how to find the unique values in a column using:

```python
df["Column"].unique()
```

Learned how to count unique values using:

```python
df["Column"].nunique()
```

### 🔹 Dataset Overview

Learned how to get a general overview of a dataset using:

```python
df.info()
```

`df.info()` provides information about:

* Number of rows
* Number of columns
* Column names
* Non-null values
* Data types
* Memory usage

Also explored:

```python
df.describe()
```

to obtain a statistical summary of numerical columns.

---

## 💻 Practical Work

Created a Pandas DataFrame and practiced:

* Checking dataset shape
* Inspecting column names
* Checking data types
* Checking memory usage
* Finding unique values
* Counting unique values
* Inspecting dataset information
* Generating a statistical summary

---

## 🧠 Important Pandas Commands Learned

| Purpose                 | Pandas Command                     |
| ----------------------- | ---------------------------------- |
| Dataset shape           | `df.shape`                         |
| Column names            | `df.columns`                       |
| Column names as list    | `df.columns.tolist()`              |
| Data types              | `df.dtypes`                        |
| Memory usage            | `df.memory_usage()`                |
| Detailed memory usage   | `df.memory_usage(deep=True)`       |
| Total memory            | `df.memory_usage(deep=True).sum()` |
| Unique values           | `df["Column"].unique()`            |
| Number of unique values | `df["Column"].nunique()`           |
| Dataset overview        | `df.info()`                        |
| Statistical summary     | `df.describe()`                    |

---

## 🤖 Why Dataset Understanding Matters in Machine Learning

Before training a model, it is important to understand:

* How large the dataset is
* What features are available
* Which columns are numerical or categorical
* How much memory the dataset requires
* How many unique categories exist
* Whether missing values may exist
* The basic statistical characteristics of the data

Understanding the dataset first helps prevent mistakes during preprocessing and model development.

---

## 🛠 Library Used

* Pandas

```python
import pandas as pd
```

---

## 🎯 Key Takeaways

* A DataFrame is a tabular data structure provided by Pandas.
* `shape` tells us the number of rows and columns.
* `columns` shows the available features.
* `dtypes` identifies the type of each column.
* `memory_usage()` helps understand memory consumption.
* `unique()` shows distinct values.
* `nunique()` counts distinct values.
* `info()` provides a complete structural overview.
* `describe()` provides a statistical summary of numerical data.

---

✅ **Day 01 Completed – Dataset Understanding 🚀**
