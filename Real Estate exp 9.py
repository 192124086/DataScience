import pandas as pd
data = {
    'location': ['Location_A', 'Location_B', 'Location_A', 'Location_C', 'Location_B', 'Location_C', 'Location_A'],
    'price': [500000, 700000, 600000, 800000, 750000, 900000, 550000],
    'bedrooms': [3, 4, 3, 5, 6, 4, 5],
    'area': [1200, 1500, 1300, 1800, 2000, 1600, 1400]
}
property_data = pd.DataFrame(data)
def main():
    average = property_data.groupby('location')['price'].mean()
    print("Average Listing Price of Properties in Each Location:")
    print(average)
    print()
    
    properties = property_data[property_data['bedrooms'] > 4]
    number_of_properties = properties.shape[0]
    print("Number of Properties with More Than Four Bedrooms:", number_of_properties)
    print()
    
    largest_area= property_data.loc[property_data['area'].idxmax()]
    print("Property with the Largest Area:")
    print(largest_area)

if __name__ == "__main__":
    main()
