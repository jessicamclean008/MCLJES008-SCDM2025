import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Define the file path for the oceanographic data
file_path = r"C:\Users\jjmcl\Downloads\SCDM\SAA2_WC_2017_metocean_10min_avg.csv"

# Load the CSV file and specify missing value indicators
df = pd.read_csv(file_path, index_col='TIME_SERVER', parse_dates=True, na_values=['NaN', 'NULL', ''])

# Interpolate missing values
df = df.interpolate(method='linear')

# Define departure and arrival date-times
departure_date_time = pd.to_datetime("2017/06/28 17:10")
arrival_date_time = pd.to_datetime("2017/07/04 23:50")

# Filter the DataFrame based on the date range
df = df[(df.index >= departure_date_time) & (df.index <= arrival_date_time)]

# Calculate statistics for temperature
mean_temperature = df['AIR_TEMPERATURE'].mean()
std_temperature = df['AIR_TEMPERATURE'].std()
iqr_temperature = df['AIR_TEMPERATURE'].quantile(0.75) - df['AIR_TEMPERATURE'].quantile(0.25)

# Calculate statistics for salinity
mean_salinity = df['TSG_SALINITY'].mean()
std_salinity = df['TSG_SALINITY'].std()
iqr_salinity = df['TSG_SALINITY'].quantile(0.75) - df['TSG_SALINITY'].quantile(0.25)

# Create a table to present the statistics
statistics_table = pd.DataFrame({
    'Mean': [mean_temperature, mean_salinity],
    'Standard Deviation': [std_temperature, std_salinity],
    'Interquartile Range': [iqr_temperature, iqr_salinity]
}, index=['Air Temperature (°C)', 'Salinity (psu)'])

print(statistics_table)

# Plot the statistics table
fig, ax = plt.subplots(figsize=(6, 2))
ax.axis('tight')
ax.axis('off')
table_data = ax.table(cellText=statistics_table.values, colLabels=statistics_table.columns, rowLabels=statistics_table.index, cellLoc='center', loc='center')
table_data.auto_set_font_size(False)
table_data.set_fontsize(12)
table_data.scale(1.2, 1.2)
plt.savefig('statistics_table.png', dpi=300)
plt.show()