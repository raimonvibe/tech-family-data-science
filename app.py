import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_excel('original.xlsx')


# Data preparation
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M').astype(str)
df['Year'] = df['Date'].dt.year

# Calculate KPIs
total_sales = df['Total Cost (USD)'].sum()
total_quantity = df['Quantity'].sum()
average_sales_per_transaction = df['Total Cost (USD)'].mean()

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Sale per Transaction: ${average_sales_per_transaction:,.2f}")

# Monthly Sales Trend
monthly_sales = df.groupby('Month')['Total Cost (USD)'].sum().reset_index()
fig_monthly_sales = px.line(
    monthly_sales, 
    x='Month', 
    y='Total Cost (USD)', 
    title='Monthly Sales Trend (2023)', 
    markers=True
)
fig_monthly_sales.show()

# Top Product Categories
top_categories = df.groupby('Product Category')['Total Cost (USD)'].sum().reset_index().sort_values(by='Total Cost (USD)', ascending=False)
fig_top_categories = px.bar(
    top_categories, 
    x='Product Category', 
    y='Total Cost (USD)', 
    title='Sales by Product Category'
)
fig_top_categories.show()

# Top States by Sales
top_states = df.groupby('State')['Total Cost (USD)'].sum().reset_index().sort_values(by='Total Cost (USD)', ascending=False)
fig_top_states = px.bar(
    top_states, 
    x='State', 
    y='Total Cost (USD)', 
    title='Sales by State'
)
fig_top_states.show()

# Export cleaned data
df.to_csv('cleaned_sales_data_2023.csv', index=False)
print("Cleaned data exported to 'cleaned_sales_data_2023.csv'")
