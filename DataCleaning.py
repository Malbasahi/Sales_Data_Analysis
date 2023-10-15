import pandas as pd

# Load the Sales Data from the specified location
data = pd.read_csv(r'C:\Users\malba\Downloads\Dataset MeriSKILL\SalesData.csv')

# 1. Handling Missing Values
# Check for missing values in the entire dataset
missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)

# Handle missing values (if any)
# For example, if 'Product' is missing, replace it with 'Unknown'
data['Product'].fillna('Unknown', inplace=True)

# 2. Handling Duplicates
# Remove duplicate rows based on the 'Order ID' column
data = data.drop_duplicates(subset='Order ID', keep='first')

# 3. Inconsistencies and Data Types 
# Check for inconsistencies in the 'City' column
inconsistent_cities = data['City'].unique()
print("Inconsistent Cities:\n", inconsistent_cities)

# Address inconsistencies
data['City'] = data['City'].str.strip().str.title()

# 4. Data Types
# Convert 'Order Date' to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'])

# 5. Save the cleaned data to a new CSV file
data.to_csv(r'C:\Users\malba\Downloads\Dataset MeriSKILL\CleanedSalesData.csv', index=False)

print("Data Cleaning and Transformation Completed.")
