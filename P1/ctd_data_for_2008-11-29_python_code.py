import pandas as pd

# Define the file path
file_path = "C:\\Users\\jjmcl\\Downloads\\SCDM\\ctd_data_for_2008-11-29.dat"

# Import the data into a DataFrame
df = pd.read_csv(file_path, delimiter='\t')  # Adjust the delimiter as needed

# Display the first few rows of the DataFrame
print(df.head())

print(df)