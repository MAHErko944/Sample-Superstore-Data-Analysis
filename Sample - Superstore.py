
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline

df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

df.head()

df.shape

df.columns

df.describe().T

# Select only numeric columns before calculating skewness
df.select_dtypes(include=np.number).skew()

"""Quick Skewness Summary:

If skewness ≈ 0, the data is symmetric.

If skewness > 1, the data is highly right-skewed (long tail on the right).

If skewness < -1, it's highly left-skewed (long tail on the left).

Row ID looks perfect — no skew at all.

Postal Code has a tiny skew to the left, nothing serious.

Sales, Profit are heavily skewed to the right, which means a few values are much higher than the rest.

Quantity and Discountis also skewed a bit to the right.


"""

df.info()

"""Our dataset features consists of three datatypes
float
integer
object
Of which total numerical features are 6
And categorical features are 15.
"""

#We'll be applying the same changes to df and test dataset.

features_to_change = ['Order Date' , 'Ship Date' ]


for feature in features_to_change:
    df[feature] = pd.to_datetime(df[feature])

df.isna().sum()

df.isna().sum().sum()

missing = df.isna().sum()
missing = missing[missing > 0].sort_values()

if not missing.empty:
    fig, ax = plt.subplots(figsize=(10, len(missing)*0.4))
    bars = ax.barh(missing.index, missing.values, color='#89cff0')

    ax.set_xlabel('Missing')
    ax.set_title('Missing values per column')
    ax.grid(axis='x', linestyle='--', alpha=0.6)
    ax.bar_label(bars, padding=3, color='blue')
    plt.tight_layout()
    plt.show()
else:
    print("Not Found Missing Values")

## What are the top selling products in the superstore?

df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

""" ## ● Which category of products generates the highest revenue and profit?

"""

df.groupby('Category')[['Sales' , 'Profit']].sum().sort_values(by = 'Sales' , ascending = False)

df.groupby('Region')['Sales'].sum().sort_values(ascending = False).head(10)

"""Index(['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
       'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State',
       'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category',
       'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'],
      dtype='object')



       ● What is the impact of discounts and promotions on sales?

"""

## ● What is the impact of discounts and promotions on sales?
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Discount', y='Sales', color='steelblue', alpha=0.6)

plt.title('Relationship Between Discount and Sales')
plt.xlabel('Discount')
plt.ylabel('Sales')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

"""## What is the average profit margin for each product category?
 ○ profit margin = profit/sales (consider it this way)
"""

df['profit margin'] = df['Profit'] / df['Sales']

df.groupby('Category')['profit margin'].mean().sort_values()

""" ● Which sub-category of products has the highest demand?

"""

df.groupby('Sub-Category')['Quantity'].sum().sort_values(ascending=False).head(1)

"""# Customer Analysis

Who are the top 10 customers in terms of total revenue?

Which customers generate the highest profit per order?

What customer segments are the most profitable?

Are there customers with consistent losses (negative profit)?


"""

df.groupby('Customer Name')['Sales'].sum().sort_values(ascending = False).head(10)

df.groupby(['Order ID' , 'Customer Name'])['Profit'].sum().sort_values(ascending = False).head(10)

df.groupby('Segment')['Profit'].sum().sort_values(ascending = False)

df[df['Profit'] < 0].groupby('Customer Name')['Profit'].sum().sort_values()

"""# Product Analysis

Which products have high sales but low profit margins?

Which products are being sold at a loss most frequently?

Which sub-categories have low sales and low demand — possibly overstocked?


"""

product_df = df.groupby('Product Name')[['Sales', 'Profit']].sum()
product_df['Profit_Margin'] = product_df['Profit'] / product_df['Sales']

high_sales_low_margin = product_df[
    (product_df['Sales'] > product_df['Sales'].quantile(0.75)) &
    (product_df['Profit_Margin'] < 0.1)
]

high_sales_low_margin.sort_values(by='Sales', ascending=False).head(10)

df[df['Profit'] < 0]['Product Name'].value_counts().head(10)

df.groupby('Sub-Category')[['Sales', 'Quantity']].sum().sort_values(by='Sales')

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

top_products.plot(kind='barh', color='skyblue', figsize=(10, 6))
plt.title('Top 10 Selling Products')
plt.xlabel('Total Sales')
plt.tight_layout()
plt.show()

category_sales = df.groupby('Category')['Sales'].sum()

category_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, figsize=(6, 6))
plt.title('Sales Distribution by Category')
plt.ylabel('')
plt.show()

df['Order Date'] = pd.to_datetime(df['Order Date'])
monthly_sales = df.resample('M', on='Order Date')['Sales'].sum()

monthly_sales.plot(kind='line', figsize=(12, 5), marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

import seaborn as sns

plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Discount', y='Sales', hue='Category', alpha=0.8)
plt.title('Impact of Discount on Sales')
plt.xlabel('Discount')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

top_citys = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_citys.index, y=top_citys.values, palette='viridis')
plt.title('Top 10 Cities by Sales')
plt.show()

