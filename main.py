import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


#reading data
df = pd.read_csv("retail_sales_dataset.csv",encoding = "latin1")

pd.set_option('display.max_columns', None)
print("First five rows:")
print(df.head())

print("Dataset shape(rows, columns):")
print(df.shape)

print("Column names:")
print(df.columns.tolist())

print("Data types and non-null counts:")
df.info()

print("Numerical summary")
print(df.describe())

print("Missing values by column:")
print(df.isna().sum())

print("Duplicate rows:")
print(df.duplicated().sum())

print("Data types:")
print(df.dtypes)

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    print("Unspared order Date values:",df["Date"].isna().sum())

df = df.copy()

df = df.drop_duplicates()

for col in ['Sales','Quantity','Profit']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors ="coerce")

numeric_cols = df.select_dtypes(include ='number').columns
for col in numeric_cols:
    if df[col].isna().any():
        df[col] = df[col].fillna(df[col].median())

key_cols =[col for c in ["Date","Product","Sales"] if c in df.columns]
if key_cols:
    df = df.dropna(subset = key_cols)


print("Rows after cleaning:",len(df))
print("Missing values after cleaning:")
print(df.isna().sum())
print("Duplicates adfter cleaning:",df.duplicated().sum())

df.to_csv("retail_sales-dataset.csv",index = False)
print("Saved:retail_sales_dataset.csv")



df = pd.read_csv("retail_sales_dataset.csv")
print(df)
if "Sales" not in df.columns:
    raise ValueError("Find the correct Sales column name and update this code")

print("Total sales:",round(df["Sales"].sum(),2))
print("Average Sales per row:",round(df["Sales"].mean(),2))
print("Largest Sale value:",df["Sales"].max())
print("Smallest Sale value:",df["Sales"].min())

sales_col = "Total Amount"


df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"]).copy()
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total Amount"].sum().sort_index()
print("Monthly sales:") 
print(monthly_sales)

# Top product categories
print("\nTop 5 Product Categories:")
top_products = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(top_products)
