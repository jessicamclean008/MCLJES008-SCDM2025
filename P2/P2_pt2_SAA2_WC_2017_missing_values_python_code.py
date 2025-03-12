import pandas as pd

# Define the file path using a raw string literal
file_path = r"C:\Users\jjmcl\Downloads\SCDM\SAA2_WC_2017_metocean_10min_avg.csv"

# Load the CSV file and set the appropriate column as the time index
df = pd.read_csv(file_path, index_col='TIME_SERVER', parse_dates=True)

# Check for missing values
missing_values = df.isnull().sum()

# Display the first few rows and the missing values summary
print(df.head())
print("\nMissing Values Summary:")
print(missing_values)



