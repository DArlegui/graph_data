from pathlib import Path
import plotly.express as px
import csv

# Load data
path = Path("./eq_data/world_fires_7_day.csv")
lines = path.read_text().splitlines()
print(len(lines))
reader = csv.reader(lines)

title = "World Fires (Last 7 Days)"
lats, lons, lums, dates = [], [], [], []

for row in reader:
    curr_date = row[5]
    try:
        lat = float(row[0].strip())
        lon = float(row[1].strip())
        lum = float(row[2].strip())
    except ValueError:
        print(f"Missing data for {curr_date}")
    else:
        lats.append(lat)
        lons.append(lon)
        lums.append(lum)
        dates.append(curr_date)

# Create figure
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=lums,
    color=lums,
    color_continuous_scale="hot",
    projection="natural earth", 
    title=title,
    hover_name=dates,
    labels={"color": "Brightness"},
)

# Optional layout tweaks for nicer appearance
fig.update_layout(
    geo=dict(showland=True, landcolor="rgb(217, 217, 217)"),
    margin=dict(l=0, r=0, t=50, b=0),
)

fig.show()
