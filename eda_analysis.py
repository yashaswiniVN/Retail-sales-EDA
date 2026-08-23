"""
Retail Sales Data Visualization - Internship Project

Tools:
- Python
- Pandas
- NumPy
- Matplotlib

Input:
- retail_sales_dataset.csv

Output:
- PNG charts inside the charts/ folder
- Console-based business insights
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "retail_sales_dataset.csv"
CHART_DIR = BASE_DIR / "charts"
CHART_DIR.mkdir(exist_ok=True)


# 1. Load dataset
df = pd.read_csv(DATA_FILE)

print("=" * 60)
print("RETAIL SALES DATA VISUALIZATION")
print("=" * 60)

# 2. Data cleaning
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df = df.drop_duplicates()
df = df.dropna()
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

print("\nDataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df[["Quantity", "Unit_Price", "Sales", "Profit"]].describe())


# 3. Sales by region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
region_sales.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(CHART_DIR / "01_sales_by_region.png", dpi=300)
plt.show()


# 4. Sales by category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(CHART_DIR / "02_sales_by_category.png", dpi=300)
plt.show()


# 5. Monthly sales trend
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(CHART_DIR / "03_monthly_sales_trend.png", dpi=300)
plt.show()


# 6. Profit by category
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
category_profit.plot(kind="bar")
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit (₹)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(CHART_DIR / "04_profit_by_category.png", dpi=300)
plt.show()


# 7. Top 10 products
top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))
top_products.plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales (₹)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(CHART_DIR / "05_top_10_products.png", dpi=300)
plt.show()


# 8. Quantity sold by category
category_quantity = df.groupby("Category")["Quantity"].sum()

plt.figure(figsize=(9, 5))
category_quantity.plot(kind="bar")
plt.title("Quantity Sold by Category")
plt.xlabel("Category")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(CHART_DIR / "06_quantity_by_category.png", dpi=300)
plt.show()


# 9. Sales distribution
plt.figure(figsize=(9, 5))
plt.hist(df["Sales"], bins=30, edgecolor="black")
plt.title("Sales Distribution")
plt.xlabel("Sales (₹)")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig(CHART_DIR / "07_sales_distribution.png", dpi=300)
plt.show()


# 10. Sales vs profit
plt.figure(figsize=(9, 5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.6)
plt.title("Sales vs Profit")
plt.xlabel("Sales (₹)")
plt.ylabel("Profit (₹)")
plt.tight_layout()
plt.savefig(CHART_DIR / "08_sales_vs_profit.png", dpi=300)
plt.show()


# 11. Correlation heatmap
numeric_df = df[["Quantity", "Unit_Price", "Sales", "Profit"]]
correlation = numeric_df.corr()

plt.figure(figsize=(7, 5))
plt.imshow(correlation, aspect="auto")
plt.colorbar(label="Correlation")
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=30)
plt.yticks(range(len(correlation.columns)), correlation.columns)

for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(
            j, i, f"{correlation.iloc[i, j]:.2f}",
            ha="center", va="center"
        )

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(CHART_DIR / "09_correlation_heatmap.png", dpi=300)
plt.show()


# 12. Business insights
best_region = region_sales.idxmax()
best_category = category_sales.idxmax()
best_profit_category = category_profit.idxmax()
best_product = top_products.idxmax()
best_month = monthly_sales.idxmax()

print("\n" + "=" * 60)
print("KEY BUSINESS INSIGHTS")
print("=" * 60)
print(f"Highest sales region    : {best_region}")
print(f"Highest sales category  : {best_category}")
print(f"Highest profit category : {best_profit_category}")
print(f"Top product by sales    : {best_product}")
print(f"Best sales month       : {best_month}")

print(f"\nTotal Sales             : ₹{df['Sales'].sum():,.2f}")
print(f"Total Profit            : ₹{df['Profit'].sum():,.2f}")
print(f"Total Quantity Sold     : {df['Quantity'].sum():,}")
print(f"Average Order Value     : ₹{df['Sales'].mean():,.2f}")

print("\nCharts saved in:", CHART_DIR)
