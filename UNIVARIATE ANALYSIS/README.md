# 📊 Univariate Analysis

This section focuses on analyzing **one variable at a time** using different statistical visualizations.

Univariate analysis is an important part of Exploratory Data Analysis (EDA) because it helps us understand the distribution, frequency, spread, and patterns within individual variables.

## 📚 Concepts Learned

### 🔹 Univariate Analysis

Univariate analysis means analyzing a **single variable/column** at a time.

For example:

```text
Age
Salary
City
Marks
```

Each variable can be studied independently using appropriate visualizations.

---

### 🔹 Histogram

A histogram is used to visualize the distribution of **numerical data**.

It divides numerical values into ranges called **bins** and shows how many observations fall into each range.

```python
import matplotlib.pyplot as plt

plt.hist(df["Age"], bins=5)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()
```

**Main purpose:**

> Understand how numerical values are distributed.

---

### 🔹 KDE Plot

KDE stands for **Kernel Density Estimation**.

A KDE plot provides a smooth curve representing the estimated distribution of numerical data.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.kdeplot(df["Age"])
plt.xlabel("Age")
plt.title("Age KDE")
plt.show()
```

**Main purpose:**

> Understand the smooth shape and concentration of a numerical distribution.

---

### 🔹 Count Plot

A count plot is mainly used for **categorical variables**.

It displays how many observations belong to each category.

```python
sns.countplot(x="City", data=df)
plt.xlabel("City")
plt.ylabel("Count")
plt.title("People by City")
plt.show()
```

**Main purpose:**

> Find how frequently each category occurs.

---

### 🔹 Box Plot

A box plot is used to understand the distribution and spread of numerical data.

It helps visualize:

* Median
* Q1
* Q3
* Spread
* Potential outliers

```python
sns.boxplot(y=df["Salary"])
plt.ylabel("Salary")
plt.title("Salary Distribution")
plt.show()
```

**Main purpose:**

> Understand spread and identify potential outliers.

---

### 🔹 Bar Plot

A bar plot compares a numerical value across categories.

For example, average salary by city:

```python
sns.barplot(x="City", y="Salary", data=df)
plt.xlabel("City")
plt.ylabel("Average Salary")
plt.title("Average Salary by City")
plt.show()
```

**Main purpose:**

> Compare a numerical measurement across categories.

---

## 🆚 Visualization Comparison

| Visualization | Data Type               | Main Purpose                               |
| ------------- | ----------------------- | ------------------------------------------ |
| Histogram     | Numerical               | Understand distribution                    |
| KDE Plot      | Numerical               | See smooth distribution shape              |
| Count Plot    | Categorical             | Count observations in each category        |
| Box Plot      | Numerical               | Understand spread and potential outliers   |
| Bar Plot      | Categorical + Numerical | Compare numerical values across categories |

---

## 🧠 Easy Memory Guide

```text
Histogram → Distribution
KDE       → Smooth Distribution
Count     → How Many?
Box       → Spread + Outliers
Bar       → Compare Values
```

---

## 🛠️ Libraries Used

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

### Pandas

Used for:

* Creating datasets
* Working with DataFrames
* Preparing data for visualization

### Matplotlib

Used for:

* Histograms
* Plot customization
* Labels and titles

### Seaborn

Used for:

* KDE plots
* Count plots
* Box plots
* Bar plots

---

## 🔄 Univariate Analysis Workflow

```text
Dataset
   ↓
Select One Variable
   ↓
Understand Its Data Type
   ↓
Choose Appropriate Visualization
   ↓
Visualize
   ↓
Identify Patterns
   ↓
Interpret the Data
```

---

## 🎯 Key Takeaways

* Univariate analysis studies one variable at a time.
* Histograms are useful for numerical distributions.
* KDE plots provide a smooth representation of numerical distributions.
* Count plots show the frequency of categorical values.
* Box plots show spread, quartiles, median, and potential outliers.
* Bar plots compare numerical measurements across categories.
* Choosing the correct visualization depends on the type of variable and the question being asked.

---

## 🎯 Goal

Learn how to select and interpret the appropriate visualization for a single variable during Exploratory Data Analysis.

The goal is not just to create plots, but to understand **what information each plot provides and why it is useful**.

---

**Univariate Analysis 📊 — Understanding individual variables through visualization and EDA.**
