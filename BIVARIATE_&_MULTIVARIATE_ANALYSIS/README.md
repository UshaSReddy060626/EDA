# 📊 Bivariate & Multivariate Analysis

This section focuses on understanding relationships between variables using statistical analysis and visualization.

## 📚 Concepts Learned

### 🔹 Bivariate Analysis

Bivariate analysis studies the relationship between **two variables**.

Example:

```text
Hours Studied ↔ Marks
```

Common tools:

* Scatter Plot
* Pearson Correlation
* Spearman Correlation

---

### 🔹 Multivariate Analysis

Multivariate analysis studies **three or more variables** together.

Common tools:

* Pair Plot
* Correlation Matrix
* Heatmap
* VIF

---

## 🔹 Scatter Plot

A scatter plot shows the relationship between two numerical variables.

```python
plt.scatter(df["Hours"], df["Marks"])

plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Hours vs Marks")

plt.show()
```

It can help identify:

* Positive relationships
* Negative relationships
* No clear relationship
* Clusters
* Potential outliers

---

## 🔹 Correlation

Correlation measures the strength and direction of a relationship between variables.

Correlation values generally range from:

```text
-1 → 0 → +1
```

### Interpretation

```text
+1 → Perfect positive relationship
 0 → No linear correlation
-1 → Perfect negative relationship
```

Correlation does not prove causation.

---

## 🔹 Pearson Correlation

Pearson correlation measures the strength of a **linear relationship** between two numerical variables.

```python
pearson = df["Hours"].corr(
    df["Marks"],
    method="pearson"
)

print(pearson)
```

---

## 🔹 Spearman Correlation

Spearman correlation measures the strength of a **monotonic relationship** using ranked values.

```python
spearman = df["Hours"].corr(
    df["Marks"],
    method="spearman"
)

print(spearman)
```

### Pearson vs Spearman

| Pearson                                   | Spearman                                                    |
| ----------------------------------------- | ----------------------------------------------------------- |
| Measures linear relationship              | Measures monotonic relationship                             |
| Uses actual values                        | Uses ranks                                                  |
| More sensitive to outliers                | Generally more robust to outliers                           |
| Best for appropriate linear relationships | Useful for consistently increasing/decreasing relationships |

---

## 🔹 Correlation Matrix

A correlation matrix displays correlations between multiple numerical variables.

```python
corr = df[
    ["Hours", "Sleep", "Attendance", "Marks"]
].corr()

print(corr)
```

The diagonal is always `1` because each variable is perfectly correlated with itself.

---

## 🔹 Heatmap

A heatmap provides a visual representation of a correlation matrix.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")
plt.show()
```

`annot=True` displays the correlation values inside the cells.

Heatmaps make it easier to quickly identify strong positive and negative relationships.

---

## 🔹 Pair Plot

A pair plot provides multiple pairwise visualizations between numerical variables.

```python
sns.pairplot(
    df[["Hours", "Sleep", "Attendance", "Marks"]]
)

plt.show()
```

It helps identify:

* Relationships
* Distributions
* Patterns
* Potential outliers

---

## 🔹 Crosstab

A crosstab is useful for analyzing relationships between categorical variables.

Example:

```python
pd.crosstab(
    df["Gender"],
    df["Passed"]
)
```

This can answer questions such as:

```text
How many males/females passed or failed?
```

Crosstab is essentially useful for examining **category vs category** counts.

---

## 🔹 VIF

VIF stands for:

**Variance Inflation Factor**

VIF is used to identify **multicollinearity** among predictor variables.

Multicollinearity occurs when independent variables are highly related to each other.

For example:

```text
House Size
     ↕
Square Feet
```

These features may contain very similar information.

VIF helps identify this issue.

### Basic interpretation

| VIF | General Interpretation        |
| --: | ----------------------------- |
|  ~1 | Very little multicollinearity |
| 1–5 | Usually acceptable/moderate   |
|  >5 | Potential concern             |
| >10 | Often considered serious      |

These values are rules of thumb and should be interpreted in context.

### Basic Python

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

X = df[
    ["Hours", "Sleep", "Attendance"]
]

vif = pd.DataFrame()

vif["Feature"] = X.columns

vif["VIF"] = [
    variance_inflation_factor(
        X.values,
        i
    )
    for i in range(X.shape[1])
]

print(vif)
```

---

## 🆚 Visualization & Analysis Guide

| Tool               | Purpose                                           |
| ------------------ | ------------------------------------------------- |
| Scatter Plot       | Relationship between two numerical variables      |
| Pearson            | Linear correlation                                |
| Spearman           | Monotonic/rank correlation                        |
| Correlation Matrix | Correlations between multiple numerical variables |
| Heatmap            | Visualizes correlation matrix                     |
| Pair Plot          | Multiple pairwise relationships                   |
| Crosstab           | Category vs category counts                       |
| VIF                | Detects multicollinearity                         |

---

## 🧠 Key Takeaways

* Bivariate analysis studies two variables.
* Multivariate analysis studies three or more variables.
* Scatter plots visualize relationships between numerical variables.
* Correlation measures the strength and direction of relationships.
* Pearson measures linear correlation.
* Spearman measures monotonic/rank correlation.
* Correlation does not imply causation.
* A correlation matrix shows correlations between multiple variables.
* Heatmaps make correlation matrices easier to interpret visually.
* Pair plots provide a quick overview of multiple pairwise relationships.
* Crosstabs are useful for categorical variables.
* VIF helps detect multicollinearity among features.

---

## 🔄 EDA Workflow

```text
Dataset
   ↓
Select Variables
   ↓
Understand Relationships
   ↓
Visualize
   ↓
Calculate Correlations
   ↓
Check Multicollinearity
   ↓
Interpret Results
```

---

## 🛠️ Libraries Used

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
```

### Pandas

Used for:

* DataFrames
* Correlation
* Crosstab
* Data manipulation

### Matplotlib

Used for:

* Scatter plots
* Plot customization

### Seaborn

Used for:

* Pair plots
* Heatmaps
* Count/visual analysis

### Statsmodels

Used for:

* VIF calculation

---

## 🎯 Goal

Learn how to analyze relationships between variables, identify correlations and patterns, visualize multivariate relationships, and recognize multicollinearity before building Machine Learning models.

**Bivariate & Multivariate Analysis 📊 — Understanding relationships, correlations, and feature interactions through EDA.**
