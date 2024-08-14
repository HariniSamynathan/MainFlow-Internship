import pandas as pd

# Load a CSV file into a Pandas DataFrame
# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('C:\Users\Admin\Documents\MainFlow\data.csv.csv')

# Display the first few rows of the DataFrame
print("Initial DataFrame:")
print(df.head())

# Filtering data based on conditions
# For example, filtering rows where the 'age' column is greater than 30
filtered_df = df[df['age'] > 30]
print("\nFiltered DataFrame (age > 30):")
print(filtered_df)

# Handling missing values
# Check for missing values in the DataFrame
print("\nMissing Values in DataFrame:")
print(df.isnull().sum())

# Fill missing values with a specified value (e.g., 0)
df.fillna(0, inplace=True)

# Alternatively, drop rows with missing values
# df.dropna(inplace=True)

print("\nDataFrame after handling missing values:")
print(df.head())

# Calculating summary statistics
summary_statistics = df.describe()
print("\nSummary Statistics:")
print(summary_statistics)
