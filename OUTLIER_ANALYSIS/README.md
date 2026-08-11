# 📦 Outlier Analysis

This section focuses on identifying, visualizing, and handling unusual observations in datasets using Python.

Outlier analysis is an important part of Exploratory Data Analysis because extreme values can affect statistical calculations and Machine Learning models.

## 📚 Concepts Learned

### 🔹 Outliers

An outlier is an observation that is unusually far away from the other values in a dataset.

Outliers can occur because of:

* Data-entry errors
* Measurement errors
* Incorrect values
* Rare events
* Genuine extreme observations

An unusual value is not automatically an error and should be investigated before removing it.

---

### 🔹 Box Plot

Learned how to use box plots to visualize the distribution of numerical data and identify potential outliers.

```python
import matplotlib.pyplot as plt

plt.boxplot(data)
plt.show()
```

A box plot displays important distribution information such as:

* Q1
* Median
* Q3
* Whiskers
* Potential outliers

---

### 🔹 IQR

IQR stands for **Interquartile Range**.

It represents the range covered by the middle 50% of the data.

The formula is:

```text
IQR = Q3 - Q1
```

Potential outliers can be identified using:

```text
Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

Values below the lower bound or above the upper bound are treated as potential outliers under this rule.

Using Pandas:

```python
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
```

---

### 🔹 Z-Score

Learned that a Z-score measures how far a value is from the mean in terms of standard deviations.

The formula is:

```text
z = (x - mean) / standard deviation
```

A common rule of thumb is that values with:

```text
|z| > 3
```

may be potential outliers.

This rule should be interpreted in context and works best when the distribution is reasonably compatible with the assumptions of the method.

Using NumPy:

```python
import numpy as np

mean = np.mean(data)
std = np.std(data)

z_scores = (data - mean) / std
```

---

### 🔹 Outlier Treatment

Learned that outliers should be investigated before deciding how to handle them.

Possible approaches include:

* Removing incorrect observations
* Correcting data-entry errors
* Capping extreme values
* Keeping genuine extreme observations
* Applying transformations when appropriate

The correct treatment depends on the dataset and the reason behind the extreme value.

---

## 🆚 IQR vs Z-Score

| IQR                             | Z-Score                                                       |   |      |
| ------------------------------- | ------------------------------------------------------------- | - | ---- |
| Uses Q1 and Q3                  | Uses mean and standard deviation                              |   |      |
| Less affected by extreme values | Mean and standard deviation can be affected by extreme values |   |      |
| Useful for skewed data          | Often useful for approximately normal data                    |   |      |
| Uses the 1.5 × IQR rule         | Common rule of thumb is `                                     | z | > 3 |

---

## 🛠️ Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

### Pandas

Used for:

* Data handling
* Quartile calculation
* IQR calculation

### NumPy

Used for:

* Mean
* Standard deviation
* Z-score calculations
* Numerical operations

### Matplotlib

Used for:

* Box plot visualization

---

## 🔄 Outlier Analysis Workflow

```text
Raw Dataset
     ↓
Visualize Data
     ↓
Box Plot
     ↓
Detect Potential Outliers
     ↓
IQR / Z-Score
     ↓
Investigate Outliers
     ↓
Decide Treatment
     ↓
Clean Dataset
```

---

## 🧠 Key Takeaways

* Outliers are unusually extreme observations.
* Outliers are not automatically errors.
* Box plots help visualize potential outliers.
* IQR represents the range of the middle 50% of data.
* IQR is calculated as `Q3 - Q1`.
* The 1.5 × IQR rule can be used to identify potential outliers.
* Z-score measures distance from the mean in standard-deviation units.
* A common Z-score rule of thumb is `|z| > 3`.
* IQR is generally less sensitive to extreme values than Z-score.
* Outliers should be investigated before removing them.
* Genuine extreme observations may need to be retained.

---

## 🎯 Goal

Learn how to:

```text
Visualize
   ↓
Detect
   ↓
Investigate
   ↓
Decide
   ↓
Treat
```

outliers correctly before continuing with further Exploratory Data Analysis and Machine Learning preprocessing.

---

**Outlier Analysis 📦 — Learning through Python, statistics, visualization, and practice.**
