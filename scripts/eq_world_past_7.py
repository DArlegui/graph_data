from pathlib import Path
import json
import plotly.express as px

path = Path("./eq_data/eq_data_past_7_days.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data["features"]
graph_title = all_eq_data["metadata"]["title"]

mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    title = eq_dict["properties"]["title"]
    mag = eq_dict["properties"]["mag"]

    if mag > 0:  # skip null or negative magnitudes
        eq_titles.append(title)
        mags.append(mag)
        lons.append(eq_dict["geometry"]["coordinates"][0])
        lats.append(eq_dict["geometry"]["coordinates"][1])
    else:
        print(f"Skipping mag {mag} located: {title}")


fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=graph_title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
