# Sitka Death, Valley Comparison
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import csv

path = Path("./weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines) # Creates recorder/pointer
header_row = next(reader) # Points to the first element of array

"""Debugging Purposes"""
# print(plt.style.available)

# for index, column_header in enumerate(header_row): # Checks for first ele of reader
#     print(index, column_header)

# first_values = next(reader)
# for index, column_header in enumerate(first_values):  # Checks for first ele of reader
#     print(index, column_header.strip())

dates, rainfalls = [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        #Captures the 
        rainfall_amount = float(row[5].strip()) 
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainfalls.append(rainfall_amount)

# Plot the high temperatures.
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color="blue")
plt.style.use("_mpl-gallery")

# Format plot.
ax.set_title("Daily Rainfall Amounts, Sitka, Alaska", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation Amount (inches)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
