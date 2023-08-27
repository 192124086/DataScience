import pandas as pd

data = {
    'customer_id': [101, 102, 103, 101, 104, 105, 103],
    'product_id': [1, 2, 1, 3, 2, 1, 3],
    'order_date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05', '2023-07-06', '2023-07-07'],
    'order_quantity': [5, 10, 7, 3, 8, 6, 4]
}

order_data = pd.DataFrame(data)

def main():
    customer = order_data.groupby('customer_id')['order_date'].count()
    print("Total Number of Orders by Each Customer:")
    print(customer)
    print()

    product = order_data.groupby('product_id')['order_quantity'].mean()
    print("Average Order Quantity for Each Product:")
    print(product)
    print()

    earliest = order_data['order_date'].min()
    latest = order_data['order_date'].max()
    print("Earliest Order Date:", earliest)
    print("Latest Order Date:", latest)

if __name__ == "__main__":
    main()
