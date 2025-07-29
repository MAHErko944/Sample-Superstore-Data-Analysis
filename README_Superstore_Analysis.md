# Superstore Sales Analysis

This project is a complete exploratory data analysis (EDA) of a US Superstore dataset. The goal is to uncover business insights from sales data and visualize important trends related to products, customers, and overall performance.

## Dataset

The dataset used in this project is the **Sample - Superstore.csv**, which contains 9,994 records of sales transactions. It includes details like:

- Order date, ship date, and shipping mode  
- Customer and geographic data (name, city, state, region)  
- Product categories and sub-categories  
- Sales, profit, discount, and quantity

## Objective

The main goal is to answer key business questions such as:

- Which products generate the highest sales and profits?
- What is the impact of discounts on sales?
- Which customer segments are the most profitable?
- Are there any products being sold at a loss?
- What regions and cities bring in the most revenue?

## Steps Performed

1. **Data Loading & Cleaning**
   - Read CSV file with correct encoding
   - Converted date columns to datetime
   - Checked and handled missing values

2. **Basic Exploration**
   - Dataset structure and feature types
   - Summary statistics using `.describe()` and `.skew()` to understand distribution

3. **Feature Engineering**
   - Created a new column: `profit margin = Profit / Sales`

4. **Visual Analysis**
   - Top selling products (bar chart)
   - Category sales distribution (pie chart)
   - Monthly sales trend (line plot)
   - Impact of discount on sales (scatter plot)
   - Correlation heatmap

5. **Deep Dive Analysis**
   - Top products with high sales but low margins
   - Sub-categories with low sales and demand
   - Top customers by revenue and profit
   - Customers with consistent losses
   - Top performing regions and cities

## Key Insights

- Some products with high sales bring very little profit, indicating poor pricing strategies.
- Discounts can lead to higher sales, but excessive discounts often reduce profits.
- The Technology category has the highest revenue, while Office Supplies shows lower margins.
- Certain sub-categories like "Binders" and "Chairs" are high in demand.
- A few customers generate consistent losses, which could be a risk to the business.

## Tools Used

- **Python**
- **Pandas**
- **Seaborn & Matplotlib** for visualization
- **NumPy**

## How to Run

1. Make sure you have Python installed.
2. Install required libraries if not already installed:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Place `Sample - Superstore.csv` in your working directory.
4. Run the `.py` file from your IDE or command line.