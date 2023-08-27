import pandas as pd
data = {
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A'],
    'quantity_sold': [3, 2, 1, 4, 3, 2]
}
sales_data = pd.DataFrame(data)
product_sales= sales_data.groupby('product_name')['quantity_sold'].sum()
sorted_product = product_sales.sort_values(ascending=False)
products = sorted_product.head(5)
print("Top 5 products sold:")
print(products)
