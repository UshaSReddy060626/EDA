# 📊 Descriptive Statistics

This section focuses on using descriptive statistics to summarize and understand datasets before performing deeper Exploratory Data Analysis and Machine Learning.

## 📚 Concepts Learned

### `describe()`

Used Pandas `describe()` to generate a quick statistical summary of numerical columns.

```python
df.describe()
```

It provides:

* Count
* Mean
* Standard deviation
* Minimum
* 25th percentile
* Median
* 75th percentile
* Maximum

---

### Mean

The mean represents the average value of a dataset.

```python
df["Marks"].mean()
```

It is calculated by adding all values and dividing by the number of values.

The mean can be strongly affected by extreme values.

---

### Median

The median is the middle value of an ordered dataset.

```python
df["Marks"].median()
```

If there are an even number of observations, the median is calculated using the two middle values.

The median is generally less sensitive to extreme values than the mean.

---

### Mode

The mode is the most frequently occurring value.

```python
df["Marks"].mode()
```

Mode can also be useful for categorical data.

---

### Quartiles

Quartiles divide ordered data into four sections.

* Q1 → 25th percentile
* Q2 → 50th percentile / Median
* Q3 → 75th percentile

Using Pandas:

```python
df["Marks"].quantile(0.25)
df["Marks"].quantile(0.50)
df["Marks"].quantile(0.75)
```

---

### Percentiles

Percentiles describe the position of a value within an ordered dataset.

For example:

```python
df["Marks"].quantile(0.90)
```

returns the 90th percentile.

The 90th percentile represents a value at or below which approximately 90% of observations fall.

---

### Skewness

Skewness describes the asymmetry of a distribution.

* Positive skew → longer right tail
* Negative skew → longer left tail
* Approximately zero → approximately symmetric

Using Pandas:

```python
df["Marks"].skew()
```

---

### Kurtosis

Kurtosis provides information about the tail behavior of a distribution.

Using Pandas:

```python
df["Marks"].kurt()
```

Pandas uses an excess-kurtosis convention, where a normal distribution has a value of approximately 0.

---

## 💻 Practical Work

Practiced calculating:

* Descriptive statistics
* Mean
* Median
* Mode
* Quartiles
* Percentiles
* Skewness
* Kurtosis

using Python and Pandas.

---

## 🛠️ Library Used

```python
import pandas as pd
```

---

## 🧠 Key Takeaways

* `describe()` provides a quick statistical summary.
* Mean represents the average.
* Median represents the middle of ordered data.
* Mode represents the most frequently occurring value.
* Quartiles divide ordered data into four sections.
* Percentiles describe positions within ordered data.
* Q2 is the same as the median.
* Mean is generally more sensitive to extreme values than median.
* Skewness describes the asymmetry and direction of a distribution's tail.
* Kurtosis provides information about distribution tail behavior.
* Descriptive statistics provide an initial numerical understanding of a dataset.

---

## 🎯 Goal

Use descriptive statistics to understand:

```text
Center
  ↓
Position
  ↓
Distribution Shape
  ↓
Data Characteristics
```

before moving to deeper Exploratory Data Analysis and Data Preprocessing.

---

**Descriptive Statistics 📊 — Learning through Python, Pandas, and practice.**
