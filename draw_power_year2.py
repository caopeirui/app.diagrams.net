import matplotlib.pyplot as plt
import numpy as np
# Assuming the years and data growth pattern based on the image provided
years = np.arange(2006, 2024)  # Extended to 2023 for forecast
# Data for plotting, using polynomial fit as an estimation from the visual inspection of the chart.
# These are dummy values and should be replaced with actual data for accurate results.
# The coefficients are estimated and should be adjusted for a more accurate fit.
poly_100Mb = np.poly1d(np.polyfit([2006, 2012, 2018], [0.3, 0.2, 0.1], 2))
poly_1000Mb = np.poly1d(np.polyfit([2006, 2012, 2018], [0.7, 0.5, 0.2], 2))
poly_10Gb = np.poly1d(np.polyfit([2006, 2012, 2018], [0.3, 0.8, 1.2], 2))
poly_40Gb = np.poly1d(np.polyfit([2006, 2012, 2018], [0.4, 1.1, 1.6], 2))



# Calculate the y values based on the polynomial fit
data_100Mb = poly_100Mb(years)
data_1000Mb = poly_1000Mb(years)
data_10Gb = poly_10Gb(years)
data_40Gb = poly_40Gb(years)
# Ensure that each higher data category starts where the previous one ends
data_1000Mb = np.maximum(data_1000Mb, data_100Mb)
data_10Gb = np.maximum(data_10Gb, data_1000Mb)
data_40Gb = np.maximum(data_40Gb, data_10Gb)
# Plotting the data
fig, ax = plt.subplots()
# Filling between the data segments
ax.fill_between(years, 0, data_100Mb, color='red', step='pre', alpha=0.6)
ax.fill_between(years, data_100Mb, data_1000Mb, color='green', step='pre', alpha=0.6)
ax.fill_between(years, data_1000Mb, data_10Gb, color='blue', step='pre', alpha=0.6)
ax.fill_between(years, data_10Gb, data_40Gb, color='purple', step='pre', alpha=0.6)
# Adding forecast line and text
forecast_year = 2018
# plt.axvline(x=forecast_year, color='black', linestyle='--')
# plt.text(forecast_year + 0.2, 1.3, 'forecast ->', fontsize=9, verticalalignment='center')
# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Network Electricity Use (billion kWh)')
ax.set_title('Network Electricity Use Forecast')
# Adding grid
# plt.grid(True)
# Show the plot
plt.show()