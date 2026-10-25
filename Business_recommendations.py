import pandas as pd

sales = pd.read_csv("retail_sales_dataset.csv.csv")

category_sales = sales.groupby("Product Category")["Total Amount"].sum()

best_category = category_sales.max()
lowest_category = category_sales.min()

print("Business Recommendations")
print(f"Total sales: {sales['Total Amount'].sum():,.2f}")
print(f"Best-selling category: {best_category}")
print(f"Lowest-selling category: {lowest_category}")
print(f"Keep enough {best_category} products in stock.")
print(f"Consider a promotion to increase {lowest_category} sales.")
print(f"Promote {best_category} to attract more customers and grow sales.")
print("Offer related products together to encourage customers to buy more.")
print("Track product costs and focus on items with higher profit margins.")
