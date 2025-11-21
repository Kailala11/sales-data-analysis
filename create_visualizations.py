import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")

# Load data
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%b')
df['Day_of_Week'] = df['Date'].dt.day_name()

print("Creating visualizations...")

# ============================================================================
# VISUALIZATION 1: Dashboard Overview (4 subplots)
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)

# 1.1 Monthly Revenue Trend
ax1 = fig.add_subplot(gs[0, :])
monthly_sales = df.groupby(['Year', 'Month'])['Final_Price'].sum().reset_index()
monthly_sales['Year_Month'] = monthly_sales['Year'].astype(str) + '-' + monthly_sales['Month'].astype(str).str.zfill(2)

ax1.plot(range(len(monthly_sales)), monthly_sales['Final_Price'], 
         marker='o', linewidth=2, markersize=6, color='#2E86AB')
ax1.fill_between(range(len(monthly_sales)), monthly_sales['Final_Price'], alpha=0.3, color='#2E86AB')
ax1.set_xlabel('Month', fontsize=12, fontweight='bold')
ax1.set_ylabel('Revenue (Rp)', fontsize=12, fontweight='bold')
ax1.set_title('Monthly Revenue Trend (2023-2024)', fontsize=14, fontweight='bold', pad=20)
ax1.grid(True, alpha=0.3)

# Add annotations for peaks
max_idx = monthly_sales['Final_Price'].idxmax()
max_val = monthly_sales.loc[max_idx, 'Final_Price']
ax1.annotate(f'Peak: Rp {max_val:,.0f}', 
             xy=(max_idx, max_val), 
             xytext=(max_idx+2, max_val+10000),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=10, fontweight='bold', color='red')

# Rotate x-axis labels
tick_positions = range(0, len(monthly_sales), 3)
ax1.set_xticks(tick_positions)
ax1.set_xticklabels([monthly_sales.iloc[i]['Year_Month'] for i in tick_positions], rotation=45)

# 1.2 Top 10 Products
ax2 = fig.add_subplot(gs[1, 0])
top_products = df.groupby('Product')['Final_Price'].sum().nlargest(10).sort_values()
colors = plt.cm.Spectral(np.linspace(0, 1, len(top_products)))
top_products.plot(kind='barh', ax=ax2, color=colors)
ax2.set_xlabel('Revenue (Rp)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Product', fontsize=11, fontweight='bold')
ax2.set_title('Top 10 Products by Revenue', fontsize=12, fontweight='bold', pad=15)
ax2.grid(axis='x', alpha=0.3)

# Add value labels
for i, v in enumerate(top_products.values):
    ax2.text(v, i, f' Rp {v/1000:.0f}K', va='center', fontsize=9)

# 1.3 Category Distribution
ax3 = fig.add_subplot(gs[1, 1])
category_sales = df.groupby('Category')['Final_Price'].sum().sort_values(ascending=False)
colors_pie = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
wedges, texts, autotexts = ax3.pie(category_sales.values, 
                                     labels=category_sales.index,
                                     autopct='%1.1f%%',
                                     startangle=90,
                                     colors=colors_pie,
                                     explode=[0.05 if i == 0 else 0 for i in range(len(category_sales))])
ax3.set_title('Revenue by Category', fontsize=12, fontweight='bold', pad=15)

# Improve text readability
for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(9)
    autotext.set_fontweight('bold')

plt.suptitle('Sales Performance Dashboard', fontsize=18, fontweight='bold', y=0.98)
plt.savefig('dashboard_overview.png', dpi=300, bbox_inches='tight')
print("✓ Saved: dashboard_overview.png")

# ============================================================================
# VISUALIZATION 2: Customer Analysis
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Customer Behavior Analysis', fontsize=18, fontweight='bold', y=0.995)

# 2.1 Sales by Region
regional_sales = df.groupby('Region')['Final_Price'].sum().sort_values(ascending=False)
colors_region = plt.cm.viridis(np.linspace(0, 0.8, len(regional_sales)))
axes[0, 0].bar(range(len(regional_sales)), regional_sales.values, color=colors_region)
axes[0, 0].set_xticks(range(len(regional_sales)))
axes[0, 0].set_xticklabels(regional_sales.index, rotation=45, ha='right')
axes[0, 0].set_ylabel('Revenue (Rp)', fontsize=11, fontweight='bold')
axes[0, 0].set_title('Revenue by Region', fontsize=12, fontweight='bold', pad=15)
axes[0, 0].grid(axis='y', alpha=0.3)

# Add value labels
for i, v in enumerate(regional_sales.values):
    axes[0, 0].text(i, v, f'Rp {v/1000:.0f}K', ha='center', va='bottom', fontsize=9)

# 2.2 Sales by Day of Week
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_sales = df.groupby('Day_of_Week')['Final_Price'].sum().reindex(day_order)
colors_day = ['#FF6B6B' if day in ['Saturday', 'Sunday'] else '#4ECDC4' for day in day_order]
axes[0, 1].bar(range(len(day_sales)), day_sales.values, color=colors_day, alpha=0.8)
axes[0, 1].set_xticks(range(len(day_sales)))
axes[0, 1].set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
axes[0, 1].set_ylabel('Revenue (Rp)', fontsize=11, fontweight='bold')
axes[0, 1].set_title('Revenue by Day of Week', fontsize=12, fontweight='bold', pad=15)
axes[0, 1].grid(axis='y', alpha=0.3)

# 2.3 Customer Segment Performance
segment_data = df.groupby('Customer_Segment').agg({
    'Final_Price': 'sum',
    'Order_ID': 'count'
}).reset_index()
segment_data.columns = ['Segment', 'Revenue', 'Orders']

x = np.arange(len(segment_data))
width = 0.35

bar1 = axes[1, 0].bar(x - width/2, segment_data['Revenue'], width, label='Revenue', color='#45B7D1')
ax2_twin = axes[1, 0].twinx()
bar2 = ax2_twin.bar(x + width/2, segment_data['Orders'], width, label='Orders', color='#FFA07A')

axes[1, 0].set_xlabel('Customer Segment', fontsize=11, fontweight='bold')
axes[1, 0].set_ylabel('Revenue (Rp)', fontsize=11, fontweight='bold', color='#45B7D1')
ax2_twin.set_ylabel('Number of Orders', fontsize=11, fontweight='bold', color='#FFA07A')
axes[1, 0].set_title('Customer Segment Analysis', fontsize=12, fontweight='bold', pad=15)
axes[1, 0].set_xticks(x)
axes[1, 0].set_xticklabels(segment_data['Segment'])
axes[1, 0].tick_params(axis='y', labelcolor='#45B7D1')
ax2_twin.tick_params(axis='y', labelcolor='#FFA07A')
axes[1, 0].grid(axis='y', alpha=0.3)

# Combined legend
lines1, labels1 = axes[1, 0].get_legend_handles_labels()
lines2, labels2 = ax2_twin.get_legend_handles_labels()
axes[1, 0].legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# 2.4 Payment Method Distribution
payment_counts = df['Payment_Method'].value_counts()
colors_payment = plt.cm.Set3(np.linspace(0, 1, len(payment_counts)))
axes[1, 1].pie(payment_counts.values, 
               labels=payment_counts.index,
               autopct='%1.1f%%',
               startangle=90,
               colors=colors_payment)
axes[1, 1].set_title('Payment Method Distribution', fontsize=12, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('customer_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: customer_analysis.png")

# ============================================================================
# VISUALIZATION 3: Heatmap - Sales Pattern
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 8))

# Create pivot table for heatmap
df['Day'] = df['Date'].dt.day_name()
df['Hour'] = df['Date'].dt.hour
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Since we don't have hour data, let's create a month vs day heatmap
pivot_data = df.pivot_table(
    values='Final_Price', 
    index='Day_of_Week', 
    columns='Month', 
    aggfunc='sum'
)
pivot_data = pivot_data.reindex(day_order)

sns.heatmap(pivot_data, annot=False, fmt='.0f', cmap='YlOrRd', 
            cbar_kws={'label': 'Revenue (Rp)'}, ax=ax, linewidths=0.5)
ax.set_title('Sales Heatmap: Day of Week vs Month', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12, fontweight='bold')
ax.set_ylabel('Day of Week', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('sales_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Saved: sales_heatmap.png")

# ============================================================================
# VISUALIZATION 4: Quarterly Performance
# ============================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Quarterly & Yearly Performance', fontsize=16, fontweight='bold')

# 4.1 Quarterly Sales
df['Quarter'] = df['Date'].dt.quarter
quarterly_sales = df.groupby(['Year', 'Quarter'])['Final_Price'].sum().reset_index()
quarterly_sales['Label'] = 'Q' + quarterly_sales['Quarter'].astype(str) + ' ' + quarterly_sales['Year'].astype(str)

colors_q = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
axes[0].bar(range(len(quarterly_sales)), quarterly_sales['Final_Price'], 
            color=colors_q[:len(quarterly_sales)], alpha=0.8)
axes[0].set_xticks(range(len(quarterly_sales)))
axes[0].set_xticklabels(quarterly_sales['Label'], rotation=45, ha='right')
axes[0].set_ylabel('Revenue (Rp)', fontsize=11, fontweight='bold')
axes[0].set_title('Quarterly Revenue Trend', fontsize=12, fontweight='bold', pad=15)
axes[0].grid(axis='y', alpha=0.3)

# Add value labels
for i, v in enumerate(quarterly_sales['Final_Price'].values):
    axes[0].text(i, v, f'Rp {v/1000:.0f}K', ha='center', va='bottom', fontsize=9)

# 4.2 Year-over-Year Comparison
yearly_sales = df.groupby('Year')['Final_Price'].sum()
yearly_orders = df.groupby('Year')['Order_ID'].count()

x = np.arange(len(yearly_sales))
width = 0.35

bar1 = axes[1].bar(x - width/2, yearly_sales.values, width, label='Revenue', color='#2E86AB')
ax2_twin = axes[1].twinx()
bar2 = ax2_twin.bar(x + width/2, yearly_orders.values, width, label='Orders', color='#A23B72')

axes[1].set_xlabel('Year', fontsize=11, fontweight='bold')
axes[1].set_ylabel('Revenue (Rp)', fontsize=11, fontweight='bold', color='#2E86AB')
ax2_twin.set_ylabel('Number of Orders', fontsize=11, fontweight='bold', color='#A23B72')
axes[1].set_title('Year-over-Year Comparison', fontsize=12, fontweight='bold', pad=15)
axes[1].set_xticks(x)
axes[1].set_xticklabels(yearly_sales.index)
axes[1].tick_params(axis='y', labelcolor='#2E86AB')
ax2_twin.tick_params(axis='y', labelcolor='#A23B72')
axes[1].grid(axis='y', alpha=0.3)

# Add value labels
for i, (rev, ord) in enumerate(zip(yearly_sales.values, yearly_orders.values)):
    axes[1].text(i - width/2, rev, f'Rp {rev/1000000:.1f}M', 
                ha='center', va='bottom', fontsize=9, color='#2E86AB')
    ax2_twin.text(i + width/2, ord, f'{ord:,}', 
                 ha='center', va='bottom', fontsize=9, color='#A23B72')

# Combined legend
lines1, labels1 = axes[1].get_legend_handles_labels()
lines2, labels2 = ax2_twin.get_legend_handles_labels()
axes[1].legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.tight_layout()
plt.savefig('performance_trends.png', dpi=300, bbox_inches='tight')
print("✓ Saved: performance_trends.png")

print("\n" + "="*80)
print("All visualizations created successfully!")
print("="*80)
print("\nGenerated files:")
print("  1. dashboard_overview.png - Main dashboard with key metrics")
print("  2. customer_analysis.png - Customer behavior and segments")
print("  3. sales_heatmap.png - Sales pattern heatmap")
print("  4. performance_trends.png - Quarterly and yearly trends")
print("\nVisualization complete! 🎉")
