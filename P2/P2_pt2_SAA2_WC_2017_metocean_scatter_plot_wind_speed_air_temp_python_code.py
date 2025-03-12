import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the conversion function
def ddmm2dd(ddmm):        
    thedeg = np.floor(ddmm / 100.0)     
    themin = (ddmm - thedeg * 100.0) / 60.0     
    return thedeg + themin

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

# Convert latitude from DDMM to decimal degrees
df['LATITUDE'] = df['LATITUDE'].apply(ddmm2dd)

# Create a scatter plot of wind speed and air temperature
plt.style.use('grayscale')
fig, ax = plt.subplots(figsize=(12, 6))
scatter = ax.scatter(df['WIND_SPEED_TRUE'], df['AIR_TEMPERATURE'], c=df['LATITUDE'], cmap='viridis', alpha=0.7)
ax.set_title('Scatter Plot of Wind Speed (m/s) and Air Temperature (°C)')
ax.set_xlabel('Wind Speed (m/s)')
ax.set_ylabel('Air Temperature (°C)')
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Latitude')
plt.savefig('wind_speed_air_temperature_scatter.png', dpi=300)
plt.show()
