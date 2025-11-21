import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Load data
print("Loading sales data...")
df = pd.read_csv('sales_data.csv')

# Convert date to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%B')
df['Day_of_Week'] = df['Date'].dt.day_name()
df['Quarter'] = df['Date'].dt.quarter

print("="*80)
print("SALES DATA ANALYSIS - EXECUTIVE SUMMARY")
print("="*80)

# 1. OVERALL STATISTICS
print("\n1. OVERALL PERFORMANCE")
print("-" * 80)
total_revenue = df['Final_Price'].sum()
total_orders = len(df)
total_items_sold = df['Quantity'].sum()
avg_order_value = df['Final_Price'].mean()
total_customers = df['Customer_ID'].nunique()

print(f"Total Revenue: Rp {total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Items Sold: {total_items_sold:,}")
print(f"Average Order Value: Rp {avg_order_value:,.2f}")
print(f"Total Unique Customers: {total_customers:,}")
print(f"Period: {df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}")

# 2. MONTHLY TRENDS
print("\n2. MONTHLY REVENUE TRENDS")
print("-" * 80)
monthly_sales = df.groupby(['Year', 'Month', 'Month_Name'])['Final_Price'].sum().reset_index()
monthly_sales = monthly_sales.sort_values(['Year', 'Month'])

print("\nTop 5 Months by Revenue:")
top_months = monthly_sales.nlargest(5, 'Final_Price')
for idx, row in top_months.iterrows():
    print(f"  {row['Month_Name']} {int(row['Year'])}: Rp {row['Final_Price']:,.2f}")

# 3. TOP PRODUCTS
print("\n3. TOP PERFORMING PRODUCTS")
print("-" * 80)
product_performance = df.groupby('Product').agg({
    'Final_Price': 'sum',
    'Quantity': 'sum',
    'Order_ID': 'count'
}).round(2)
product_performance.columns = ['Total_Revenue', 'Units_Sold', 'Orders']
product_performance = product_performance.sort_values('Total_Revenue', ascending=False)

print("\nTop 10 Products by Revenue:")
for idx, (product, row) in enumerate(product_performance.head(10).iterrows(), 1):
    print(f"  {idx}. {product}")
    print(f"     Revenue: Rp {row['Total_Revenue']:,.2f} | Units: {int(row['Units_Sold'])} | Orders: {int(row['Orders'])}")

# 4. CATEGORY ANALYSIS
print("\n4. CATEGORY PERFORMANCE")
print("-" * 80)
category_performance = df.groupby('Category').agg({
    'Final_Price': 'sum',
    'Quantity': 'sum',
    'Order_ID': 'count'
}).round(2)
category_performance.columns = ['Total_Revenue', 'Units_Sold', 'Orders']
category_performance = category_performance.sort_values('Total_Revenue', ascending=False)

print("\nRevenue by Category:")
for category, row in category_performance.iterrows():
    percentage = (row['Total_Revenue'] / total_revenue) * 100
    print(f"  {category}: Rp {row['Total_Revenue']:,.2f} ({percentage:.1f}%)")

# 5. REGIONAL ANALYSIS
print("\n5. REGIONAL PERFORMANCE")
print("-" * 80)
regional_sales = df.groupby('Region')['Final_Price'].sum().sort_values(ascending=False)
print("\nRevenue by Region:")
for region, revenue in regional_sales.items():
    percentage = (revenue / total_revenue) * 100
    print(f"  {region}: Rp {revenue:,.2f} ({percentage:.1f}%)")

# 6. PURCHASING PATTERNS
print("\n6. PURCHASING PATTERNS")
print("-" * 80)

# Day of week analysis
day_sales = df.groupby('Day_of_Week')['Final_Price'].agg(['sum', 'count']).round(2)
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_sales = day_sales.reindex(day_order)

print("\nSales by Day of Week:")
for day, row in day_sales.iterrows():
    print(f"  {day}: Rp {row['sum']:,.2f} ({int(row['count'])} orders)")

# Peak shopping day
peak_day = day_sales['sum'].idxmax()
print(f"\nPeak Shopping Day: {peak_day}")

# 7. CUSTOMER SEGMENT ANALYSIS
print("\n7. CUSTOMER SEGMENT ANALYSIS")
print("-" * 80)
segment_analysis = df.groupby('Customer_Segment').agg({
    'Final_Price': 'sum',
    'Order_ID': 'count',
    'Customer_ID': 'nunique'
}).round(2)
segment_analysis.columns = ['Total_Revenue', 'Total_Orders', 'Unique_Customers']
segment_analysis['Avg_Order_Value'] = (segment_analysis['Total_Revenue'] / segment_analysis['Total_Orders']).round(2)

print("\nPerformance by Customer Segment:")
for segment, row in segment_analysis.iterrows():
    print(f"\n  {segment}:")
    print(f"    Revenue: Rp {row['Total_Revenue']:,.2f}")
    print(f"    Orders: {int(row['Total_Orders'])}")
    print(f"    Customers: {int(row['Unique_Customers'])}")
    print(f"    Avg Order Value: Rp {row['Avg_Order_Value']:,.2f}")

# 8. PAYMENT METHOD ANALYSIS
print("\n8. PAYMENT METHOD PREFERENCE")
print("-" * 80)
payment_analysis = df.groupby('Payment_Method')['Order_ID'].count().sort_values(ascending=False)
print("\nOrders by Payment Method:")
for method, count in payment_analysis.items():
    percentage = (count / total_orders) * 100
    print(f"  {method}: {count} orders ({percentage:.1f}%)")

# 9. KEY INSIGHTS
print("\n" + "="*80)
print("KEY INSIGHTS & RECOMMENDATIONS")
print("="*80)

print("\n📊 Business Highlights:")
print(f"  • Best performing category: {category_performance.index[0]}")
print(f"  • Top selling product: {product_performance.index[0]}")
print(f"  • Highest revenue region: {regional_sales.index[0]}")
print(f"  • Most active shopping day: {peak_day}")
print(f"  • Most used payment: {payment_analysis.index[0]}")

# Calculate growth (2024 vs 2023)
sales_2023 = df[df['Year'] == 2023]['Final_Price'].sum()
sales_2024 = df[df['Year'] == 2024]['Final_Price'].sum()
growth = ((sales_2024 - sales_2023) / sales_2023) * 100

print(f"\n📈 Growth Metrics:")
print(f"  • YoY Revenue Growth (2024 vs 2023): {growth:.1f}%")

# Customer behavior
repeat_customers = df.groupby('Customer_ID')['Order_ID'].count()
repeat_rate = (repeat_customers > 1).sum() / total_customers * 100
print(f"  • Customer Repeat Rate: {repeat_rate:.1f}%")
print(f"  • Average orders per customer: {repeat_customers.mean():.1f}")

print("\n💡 Recommendations:")
print("  1. Focus marketing efforts on high-performing categories")
print("  2. Optimize inventory for top-selling products")
print(f"  3. Strengthen presence in {regional_sales.index[0]} region")
print("  4. Run promotions on slower days to balance weekly sales")
print("  5. Develop loyalty programs to increase repeat customer rate")

print("\n" + "="*80)
print("Analysis Complete! Check visualizations folder for charts.")
print("="*80)

# Save summary statistics to CSV
print("\nSaving analysis results...")

# Monthly sales summary
monthly_sales.to_csv('monthly_sales_summary.csv', index=False)

# Product performance
product_performance.to_csv('product_performance.csv')

# Category performance
category_performance.to_csv('category_performance.csv')

print("\nFiles saved:")
print("  • monthly_sales_summary.csv")
print("  • product_performance.csv")
print("  • category_performance.csv")
