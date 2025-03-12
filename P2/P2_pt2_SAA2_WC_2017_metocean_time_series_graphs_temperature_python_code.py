import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the file path
file_path = r"C:\Users\jjmcl\Downloads\SCDM\SAA2_WC_2017_metocean_10min_avg.csv"

# Load the CSV file and specify missing value indicators
df = pd.read_csv(file_path, index_col='TIME_SERVER', parse_dates=True, na_values=['NaN', 'NULL', ''])

# Interpolate missing values
df = df.interpolate(method='linear')

# Define departure and arrival date-times
departure_date_time = pd.to_datetime("2017/06/28 17:10")
arrival_date_time = pd.to_datetime("2017/07/04 23:50")

# Filter the DataFrame based on the date range
selected_data = df[(df.index >= departure_date_time) & (df.index <= arrival_date_time)]

# Plot the time series of temperature
plt.style.use('grayscale')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(selected_data.index, selected_data['AIR_TEMPERATURE'], label='Air Temperature')
ax.plot(selected_data.index, selected_data['TSG_TEMP'], label='TSG Temp')
ax.set_title('Time Series of TEMPERATURE(°C)')
ax.set_xlabel('Date')
ax.set_ylabel('TEMPERATURE(°C)')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('temperature_timeseries.png')

# Plot a histogram of the salinity distribution using bins of 0.5 psu between 30 and 35
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(selected_data['TSG_SALINITY'], bins=np.arange(30, 35.5, 0.5), color='black')
ax.set_title('Histogram of Salinity Distribution')
ax.set_xlabel('TSG_SALINITY')
ax.set_ylabel('Frequency')
plt.tight_layout()
plt.savefig('salinity_histogram.png')

plt.show()

