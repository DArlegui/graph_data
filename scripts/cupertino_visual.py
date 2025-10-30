# Cupertino Weather Data 2024 - 2025
import matplotlib.pyplot as plt
from func.csv_plotting import captureTempsDate, printHeaders

file_path = "./weather_data/cupertino_2024.csv"
printHeaders(file_path)
dates, highs, lows = captureTempsDate(file_path, 2, 5, 6)

# Plot the high and low temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
ax.set_title("Cupertino High and Low Temperatures, 2024-2025", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
