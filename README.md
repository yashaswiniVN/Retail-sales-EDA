# 📊 Retail Sales Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project focuses on **Exploratory Data Analysis (EDA)** of a retail sales dataset using Python.

The main goal is to explore the dataset, identify patterns and trends, detect anomalies, test a hypothesis, and generate meaningful business insights from the data.

---

## 🎯 Objectives

The project aims to:

- Understand the structure of the retail sales dataset
- Explore variables and data types
- Identify missing values and duplicate records
- Ask meaningful business questions
- Analyze sales trends and patterns
- Identify top-performing product categories
- Find the best-selling products
- Analyze monthly sales performance
- Test the relationship between quantity and sales
- Detect unusual values and outliers
- Generate useful business insights

---

## 📂 Dataset

The dataset used in this project is:

**`retail_sales_dataset.csv`**

### Main Features

| Column       | Description                                 |
| ------------ | ------------------------------------------- |
| `Order_ID`   | Unique identification number for each order |
| `Order_Date` | Date on which the order was placed          |
| `Category`   | Product category                            |
| `Product`    | Product name                                |
| `Quantity`   | Number of units sold                        |
| `Unit_Price` | Price of one unit                           |
| `Discount`   | Discount applied to the order               |
| `Sales`      | Total sales value                           |

---

## 🛠️ Technologies Used

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📊 Matplotlib
- 📈 Seaborn
- 📓 Jupyter Notebook
- 💻 GitHub

---

## 🔍 Exploratory Data Analysis

### 1. Meaningful Questions

The following questions were considered during the analysis:

1. Which product category generates the highest sales?
2. Which month has the highest sales?
3. Which products are the top sellers?
4. Is there a relationship between quantity sold and sales?
5. Are there unusual or extreme sales values?
6. Are there missing values or duplicate records?

---

### 2. Data Structure Exploration

The dataset was examined using:

- Number of rows and columns
- Column names
- Data types
- Dataset information
- First few records
- Statistical summary

---

### 3. Data Cleaning

The following data-quality checks were performed:

- Checked for missing values
- Checked for duplicate records
- Converted the order date into the correct date format
- Removed duplicate records
- Filled missing discount values
- Handled missing product values

---

### 4. Sales Trend Analysis

The project analyzes:

- Category-wise sales
- Monthly sales trends
- Top 10 products by sales

Visualizations were created using **Matplotlib and Seaborn** to make the patterns easier to understand.

---

## 🧪 Hypothesis Testing

### Hypothesis

**Null Hypothesis (H₀):**

> Quantity sold and Sales are not linearly related.

**Alternative Hypothesis (H₁):**

> Quantity sold and Sales have a positive relationship.

The hypothesis was investigated using:

- Correlation analysis
- Scatter plot

The correlation coefficient helps understand the strength and direction of the relationship between quantity sold and sales.

---

## 🚨 Outlier Detection

The **Interquartile Range (IQR)** method was used to identify potential outliers in sales.

The following values were calculated:

- Q1 — First Quartile
- Q3 — Third Quartile
- IQR — Interquartile Range
- Lower Limit
- Upper Limit

A boxplot was used to visualize the sales distribution and possible outliers.

---

## 📊 Visualizations

The project includes several visualizations:

### 📌 Sales by Category

A bar chart is used to compare sales across different product categories.

### 📌 Monthly Sales Trend

A line chart is used to identify changes in sales over time.

### 📌 Top 10 Products

A horizontal bar chart shows the products generating the highest sales.

### 📌 Quantity vs Sales

A scatter plot is used to investigate the relationship between quantity sold and sales.

### 📌 Sales Outliers

A boxplot is used to identify unusual sales values.

### 📌 Correlation Heatmap

A heatmap shows relationships between numerical variables such as:

- Quantity
- Unit Price
- Discount
- Sales

---

## 🔑 Key Findings

The analysis provides insights into:

- The highest-performing product category
- The month with the highest sales
- The top-selling product
- The relationship between quantity and sales
- The number of potential sales outliers
- Data-quality issues such as missing values and duplicates

The exact values are generated automatically when the Jupyter Notebook is executed.

---

## 💡 Business Insights

The analysis can help a retail business to:

- Understand which categories perform well
- Identify popular products
- Improve inventory planning
- Understand monthly sales patterns
- Detect unusual transactions
- Support sales and marketing decisions
- Prepare the data for future predictive analysis

---

## 📁 Project Structure

```text
Retail-Sales-EDA/
│
├── 📊 retail_sales_dataset.csv
├── 📓 Retail_Sales_EDA.ipynb
├── 🐍 eda_analysis.py
└── 📄 README.md
```

---

## ▶️ How to Run the Project

### Step 1 — Clone the repository

```bash
git clone https://github.com/YourUsername/Retail-Sales-EDA.git
```

### Step 2 — Open the project folder

```bash
cd Retail-Sales-EDA
```

### Step 3 — Install required libraries

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Step 4 — Start Jupyter Notebook

```bash
jupyter notebook
```

### Step 5 — Open

```text
Retail_Sales_EDA.ipynb
```

Run all the cells from top to bottom.

---

## 📚 What I Learned

Through this project, I gained practical experience in:

- Data exploration
- Data cleaning
- Statistical analysis
- Data visualization
- Correlation analysis
- Hypothesis testing
- Outlier detection
- Extracting business insights from data
- Using Python for real-world data analysis

---

## 🚀 Future Improvements

This project can be extended by adding:

- 📈 Sales prediction
- 🤖 Machine learning models
- 👥 Customer segmentation
- 📊 Interactive Power BI dashboard
- 🔮 Sales forecasting
- 📦 Inventory prediction

---

## ⭐ Conclusion

Exploratory Data Analysis is an important step in any data science project.

This project demonstrates how raw retail data can be cleaned, explored, visualized, and transformed into meaningful insights that can support better business decisions.

**Thank you for visiting this project! ⭐**
