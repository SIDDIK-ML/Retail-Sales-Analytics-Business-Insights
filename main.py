from pathlib import Path

import pandas as pd


folder = Path(__file__).resolve().parent
data_file = folder / "retail_sales_dataset.csv.csv"
cleaned_file = folder / "retail_sales_cleaned.csv"

# Read the sales data
df = pd.read_csv(data_file)

print("First five rows:")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values:")
print(df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Clean the data
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

for column in ["Quantity", "Price per Unit", "Total Amount"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.drop_duplicates()

for column in ["Quantity", "Price per Unit", "Total Amount"]:
    df[column] = df[column].fillna(df[column].median())

df = df.dropna(subset=["Date", "Product Category", "Total Amount"])

print("\nRows after cleaning:", len(df))
print("Missing values after cleaning:")
print(df.isna().sum())
print("Duplicate rows after cleaning:", df.duplicated().sum())

df.to_csv(cleaned_file, index=False)
print(f"\nCleaned data saved to: {cleaned_file.name}")

# Show sales summary
print(f"\nTotal sales: {df['Total Amount'].sum():,.2f}")
print(f"Average sale: {df['Total Amount'].mean():,.2f}")
print(f"Largest sale: {df['Total Amount'].max():,.2f}")
print(f"Smallest sale: {df['Total Amount'].min():,.2f}")

df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total Amount"].sum().sort_index()
print("\nMonthly sales:")
print(monthly_sales)

category_sales = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)
print("\nSales by product category:")
print(category_sales)
