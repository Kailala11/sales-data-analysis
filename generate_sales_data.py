import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate dates for 2 years (2023-2024)
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start_date, end_date, freq='D')

# Product categories and products
products_data = {
    'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch', 'Headphones', 'Camera'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Dress', 'Sneakers', 'Backpack'],
    'Home & Living': ['Coffee Maker', 'Blender', 'Vacuum Cleaner', 'Bedding Set', 'Lamp', 'Cookware Set'],
    'Books': ['Fiction Novel', 'Business Book', 'Cookbook', 'Self-Help Book', 'Biography', 'Magazine'],
    'Sports': ['Yoga Mat', 'Dumbbells', 'Running Shoes', 'Bicycle', 'Tennis Racket', 'Sports Bottle']
}

# Price ranges for each category
price_ranges = {
    'Electronics': (50, 1500),
    'Clothing': (15, 150),
    'Home & Living': (25, 300),
    'Books': (10, 50),
    'Sports': (20, 800)
}

# Regions
regions = ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang', 'Makassar']

# Customer segments
customer_segments = ['Regular', 'Premium', 'VIP']

# Generate sales data
sales_records = []
order_id = 1000

# Generate 3000-5000 transactions
num_transactions = random.randint(3000, 5000)

for _ in range(num_transactions):
    # Random date with higher probability on weekends and certain months
    date = random.choice(date_range)
    
    # Add some seasonality - more sales in certain months
    month = date.month
    if month in [11, 12, 6, 7]:  # Holiday seasons and mid-year sale
        quantity_multiplier = 1.5
    else:
        quantity_multiplier = 1.0
    
    # Select random category and product
    category = random.choice(list(products_data.keys()))
    product = random.choice(products_data[category])
    
    # Generate price with some variation
    min_price, max_price = price_ranges[category]
    base_price = random.uniform(min_price, max_price)
    price = round(base_price, 2)
    
    # Generate quantity (with higher probability for lower quantities)
    quantity = int(np.random.exponential(2) + 1)
    quantity = min(quantity, 10)  # Cap at 10
    quantity = int(quantity * quantity_multiplier)
    quantity = max(1, quantity)
    
    # Calculate total
    total_sales = round(price * quantity, 2)
    
    # Random region
    region = random.choice(regions)
    
    # Customer segment (weighted)
    customer_segment = random.choices(
        customer_segments, 
        weights=[60, 30, 10]  # 60% Regular, 30% Premium, 10% VIP
    )[0]
    
    # Apply discount based on segment
    discount = 0
    if customer_segment == 'Premium':
        discount = random.choice([0, 5, 10])
    elif customer_segment == 'VIP':
        discount = random.choice([10, 15, 20])
    
    discount_amount = round(total_sales * (discount / 100), 2)
    final_price = round(total_sales - discount_amount, 2)
    
    # Payment method
    payment_method = random.choices(
        ['Credit Card', 'Debit Card', 'E-Wallet', 'Bank Transfer', 'Cash'],
        weights=[30, 25, 25, 15, 5]
    )[0]
    
    # Customer ID (simulate returning customers)
    customer_id = random.randint(1001, 1001 + num_transactions // 3)
    
    sales_records.append({
        'Order_ID': f'ORD{order_id}',
        'Date': date.strftime('%Y-%m-%d'),
        'Customer_ID': f'CUST{customer_id}',
        'Customer_Segment': customer_segment,
        'Region': region,
        'Category': category,
        'Product': product,
        'Quantity': quantity,
        'Unit_Price': price,
        'Total_Sales': total_sales,
        'Discount_Percent': discount,
        'Discount_Amount': discount_amount,
        'Final_Price': final_price,
        'Payment_Method': payment_method
    })
    
    order_id += 1

# Create DataFrame
df = pd.DataFrame(sales_records)

# Sort by date
df = df.sort_values('Date').reset_index(drop=True)

# Save to CSV
df.to_csv('/home/claude/sales_data.csv', index=False)

print(f"Dataset generated successfully!")
print(f"Total transactions: {len(df)}")
print(f"\nDataset Info:")
print(df.info())
print(f"\nFirst few rows:")
print(df.head())
print(f"\nBasic Statistics:")
print(df.describe())
print(f"\nData saved to: sales_data.csv")
