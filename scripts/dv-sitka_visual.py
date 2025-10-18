# Death Valley - Sikta (Temp Comparison)
from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def captureTempsDate(file_name: str, index: int) -> tuple[list, list]:
    path = Path(file_name)
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)

    dates, highs = [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[index])
        except ValueError:
            print(f"Missing data for {row[2]}")
        else:
            dates.append(current_date)
            highs.append(high)

    return dates, highs

dv_dates, dv_highs = captureTempsDate("./weather_data/death_valley_2021_full.csv", 6)
s_dates, s_highs = captureTempsDate("./weather_data/sitka_weather_2021_full.csv", 7)

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
