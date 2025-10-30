# Death Valley - Sikta (Temp Comparison)
import matplotlib.pyplot as plt
from func.csv_plotting import captureTempsDate

dv_path = "./weather_data/death_valley_2021_full.csv"
s_path = "./weather_data/sitka_weather_2021_full.csv"

dv_dates, dv_highs = captureTempsDate(dv_path, 2, 6)
s_dates, s_highs = captureTempsDate(s_path, 2, 7)

# Merge and remove duplicates
# all_dates = sorted(set(dv_dates) | set(s_dates))

# Plot the high and low temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dv_dates, dv_highs, color="red", alpha=0.5)
ax.plot(s_dates, s_highs, color="blue", alpha=0.5)
ax.fill_between(s_dates, dv_highs, s_highs, facecolor="blue", alpha=0.1)

# Format plot.
title = "Death Valley (Red) - Sitka (Blue) Temp Comparison"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
