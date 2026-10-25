import os
import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("retail_sales_dataset.csv")
except FileNotFoundError:
    print("File not found: retail_sales_dataset.csv")


os.makedirs("visualizations", exist_ok=True)

# 
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"]).copy()
    df["Month"] = df["Date"].dt.to_period("M")


if "Month" in df.columns and "Total Amount" in df.columns:
    monthly_sales = df.groupby("Month")["Total Amount"].sum().sort_index()
    monthly_sales.index = monthly_sales.index.astype(str)

    plt.figure(figsize=(10, 5))
    plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join("visualizations", "monthly_sales.png"), dpi=300)
    plt.close()

# Top products chart
if "Product Category" in df.columns and "Total Amount" in df.columns:
    top_products = (
        df.groupby("Product Category")["Total Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(10, 5))
    top_products.plot(kind="barh")
    plt.title("Top 5 Products by Sales")
    plt.xlabel("Total Sales")
    plt.ylabel("Product Category")
    plt.grid(2)
    plt.tight_layout()
    plt.savefig(os.path.join("visualizations", "top_products.png"), dpi=300)
    plt.close()

print("Charts saved in the 'visualizations' folder.")