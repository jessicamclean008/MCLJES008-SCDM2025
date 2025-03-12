import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def ddmm2dd(ddmm):         
    thedeg = np.floor(ddmm/100.)     
    themin = (ddmm-thedeg*100.)/60.     
    return thedeg+themin

# Define the file path
file_path = "C:\\Users\\jjmcl\\Downloads\\SCDM\\ctd_data_for_2008-11-29.dat"

# Import the data into a DataFrame
df = pd.read_csv(file_path, delimiter='\t')

# Display the column names to adjust accordingly
print(df.columns)

# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 6))

# Plot temperature profile
ax1.plot(df['Temperature(°C)'], df['Depth'], color='blue', label='Temperature', linestyle='-')
ax1.set_xlabel('Temperature (°C)')
ax1.set_ylabel('Depth (m)')
ax1.invert_yaxis()  # Invert y-axis to show depth increasing downward
ax1.set_title('Temperature Profile')
ax1.legend()

# Plot salinity profile
ax2.plot(df['Salinity(psu)'], df['Depth'], color='red', label='Salinity', linestyle='-')
ax2.set_xlabel('Salinity (psu)')
ax2.set_title('Salinity Profile')
ax2.legend()
# Add the main title)'],
fig.suptitle('Temperature and Salinity Profiles on 2008-11-29 measured using a CTD', fontsize=16)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

