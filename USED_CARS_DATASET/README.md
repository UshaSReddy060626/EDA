# 🚗 Used Cars Data Cleaning & Exploratory Data Analysis

A data analysis project focused on **cleaning, preprocessing, analyzing, and visualizing a used cars dataset** using Python and popular data science libraries.

The project starts with an **uncleaned used cars dataset**, handles missing values and duplicates, standardizes categorical data, performs statistical analysis and outlier detection, creates a new feature for car age, and generates multiple visualizations to understand used-car pricing and other patterns.

---

## 📌 Project Overview

Used-car datasets often contain issues such as:

* Missing values
* Duplicate records
* Inconsistent categorical values
* Different capitalization and whitespace
* Numerical outliers
* Features that require transformation

This project demonstrates a complete **data cleaning + EDA workflow** before the dataset is used for further machine learning or analysis.

---

## 🎯 Objectives

* Load and inspect the raw used-cars dataset
* Understand dataset structure and data types
* Identify missing values
* Detect duplicate records
* Separate numerical and categorical features
* Clean inconsistent categorical values
* Handle missing values
* Remove duplicate records
* Perform descriptive statistical analysis
* Detect numerical outliers using the IQR method
* Perform feature engineering
* Analyze relationships between car features and price
* Generate meaningful visualizations
* Export the cleaned dataset for future use

---

## 🛠️ Technologies & Libraries

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization

---

## 📂 Dataset

The project uses a used-cars dataset containing information about different vehicles.

### Features

| Feature             | Description                    | Type        |
| ------------------- | ------------------------------ | ----------- |
| `Brand`             | Car manufacturer               | Categorical |
| `Model`             | Car model                      | Categorical |
| `Year`              | Manufacturing year             | Numerical   |
| `Kilometers_Driven` | Distance driven by the car     | Numerical   |
| `Owner`             | Number/type of previous owners | Numerical   |
| `Engine_CC`         | Engine capacity in CC          | Numerical   |
| `Mileage_kmpl`      | Mileage of the vehicle         | Numerical   |
| `Fuel_Type`         | Type of fuel used              | Categorical |
| `Transmission`      | Manual or automatic            | Categorical |
| `City`              | City where the car is listed   | Categorical |
| `Price_INR`         | Car price in INR               | Numerical   |

---

# 🔍 Data Analysis Workflow

## 1. Loading the Dataset

The raw dataset is loaded using Pandas:

```python
df = pd.read_csv("used_cars_uncleaned_dataset.csv")
```

Initial inspection is performed using:

* `head()`
* `sample()`
* `shape`
* `columns`
* `dtypes`

This provides an initial understanding of the dataset.

---

## 2. Feature Classification

The columns are divided into numerical and categorical features.

### Numerical Features

```text
Year
Kilometers_Driven
Owner
Engine_CC
Mileage_kmpl
Price_INR
```

### Categorical Features

```text
Brand
Model
Fuel_Type
Transmission
City
```

---

## 3. Data Quality Checks

The dataset is checked for:

* Missing values
* Duplicate rows
* Unique categorical values
* Inconsistent categorical formatting

Examples:

```python
df.isnull().sum()
df.duplicated().sum()
df['Brand'].unique()
df['Fuel_Type'].unique()
```

---

# 🧹 Data Cleaning

## 4. Standardizing Categorical Data

Categorical columns are cleaned by:

* Removing leading/trailing whitespace
* Standardizing capitalization

For example:

```python
df['Brand'] = df['Brand'].str.strip().str.title()
```

The same process is applied to:

* Brand
* Fuel Type
* Transmission
* City

This helps prevent logically identical categories from being treated as different values.

---

## 5. Removing Duplicate Rows

Duplicate records are removed using:

```python
df = df.drop_duplicates()
```

The number of rows before and after cleaning is also compared to determine how many duplicate records were removed.

---

## 6. Handling Missing Values

Different strategies are used depending on the feature type.

### Categorical Features

Missing values are filled using the **mode**:

```python
mode_val = df[col].mode()[0]
df[col] = df[col].fillna(mode_val)
```

Applied to:

* `Fuel_Type`
* `Transmission`
* `City`

### Numerical Features

Missing values in numerical columns are filled using the **median**:

```python
median_val = df[col].median()
df[col] = df[col].fillna(median_val)
```

Applied to:

* `Engine_CC`
* `Mileage_kmpl`

Using the median helps reduce the influence of extreme values compared with using the mean.

---

# ⚙️ Feature Engineering

## 7. Creating Car Age

A new feature called `Car_Age` is created from the manufacturing year.

```python
current_year = 2026
df['Car_Age'] = current_year - df['Year']
```

This converts the manufacturing year into a more interpretable feature representing the approximate age of the vehicle.

---

# 📊 Exploratory Data Analysis

## 8. Descriptive Statistics

Statistical summaries are generated for numerical features using:

```python
df[numerical_cols].describe()
```

This provides information such as:

* Count
* Mean
* Standard deviation
* Minimum
* 25th percentile
* Median
* 75th percentile
* Maximum

---

## 9. Categorical Analysis

Value counts are calculated for each categorical feature to understand the distribution of:

* Brands
* Models
* Fuel types
* Transmission types
* Cities

---

# 🚨 Outlier Detection

Outliers are identified using the **Interquartile Range (IQR)** method.

### Formula

```text
IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

The method is applied to:

* `Price_INR`
* `Kilometers_Driven`

The number of detected outliers and their boundaries are displayed.

> Note: The project identifies outliers for analysis but does not automatically remove them.

---

# 📈 Visualizations

The project generates **8 visualizations** to understand the dataset.

### 1. Car Price Distribution

Shows how used-car prices are distributed.

```text
chart1_price_hist.png
```

### 2. Number of Cars by Brand

Shows the number of vehicles available for each brand.

```text
chart2_brand_bar.png
```

### 3. Price Distribution by Transmission

Compares the price distributions of automatic and manual cars.

```text
chart3_transmission_box.png
```

### 4. Car Age vs Price

Examines the relationship between vehicle age and price, with fuel type represented.

```text
chart4_age_vs_price.png
```

### 5. Kilometers Driven vs Price

Visualizes the relationship between mileage driven and vehicle price.

```text
chart5_km_vs_price.png
```

### 6. Correlation Heatmap

Shows correlations between numerical variables.

```text
chart6_heatmap.png
```

### 7. Cars by Fuel Type

Shows the distribution of vehicles across different fuel types.

```text
chart7_fueltype_count.png
```

### 8. Average Price by Brand

Compares the average used-car price across different brands.

```text
chart8_avg_price_brand.png
```

---

# 🔥 Key Analysis Areas

The analysis focuses on questions such as:

* How are used-car prices distributed?
* Which brands have the most cars in the dataset?
* Which brands have higher average prices?
* How does car age relate to price?
* Does the number of kilometers driven relate to price?
* How do automatic and manual cars differ in price?
* What is the distribution of fuel types?
* Which numerical features have strong relationships with price?
* Are there significant outliers in price or kilometers driven?

---

# 💾 Output

After cleaning and preprocessing, the final dataset is exported as:

```text
cars_cleaned.csv
```

The generated charts are also saved as PNG files:

```text
chart1_price_hist.png
chart2_brand_bar.png
chart3_transmission_box.png
chart4_age_vs_price.png
chart5_km_vs_price.png
chart6_heatmap.png
chart7_fueltype_count.png
chart8_avg_price_brand.png
```

---

# 📁 Project Structure

```text
Used-Cars-EDA/
│
├── used_cars_uncleaned_dataset.csv
├── cars_cleaned.csv
├── analysis.py
│
├── chart1_price_hist.png
├── chart2_brand_bar.png
├── chart3_transmission_box.png
├── chart4_age_vs_price.png
├── chart5_km_vs_price.png
├── chart6_heatmap.png
├── chart7_fueltype_count.png
├── chart8_avg_price_brand.png
│
└── README.md
```

---

# 🚀 How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project

```bash
cd Used-Cars-EDA
```

### 3. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

### 4. Run the analysis

```bash
python analysis.py
```

The cleaned dataset and visualization files will be generated automatically.

---

# 📚 Concepts Practiced

This project demonstrates practical knowledge of:

* Data Loading
* Data Inspection
* Data Cleaning
* Missing Value Handling
* Duplicate Removal
* Categorical Data Standardization
* Numerical Data Analysis
* Descriptive Statistics
* Outlier Detection
* IQR Method
* Feature Engineering
* Correlation Analysis
* Data Visualization
* Exploratory Data Analysis (EDA)
* CSV Data Export

---

# 🔮 Future Improvements

The cleaned dataset can be used for further machine learning tasks such as:

* Used-car price prediction
* Regression modeling
* Feature importance analysis
* Model comparison
* Hyperparameter tuning
* Price prediction API deployment

---

## 👩‍💻 Author

**Usha.S.Reddy**

This project was created as part of practical learning in **Python, Data Analysis, and Machine Learning**.
