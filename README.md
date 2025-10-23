# Graph Data Visualizations

This project generates and visualizes various datasets such as dice rolls, cubes, random walks, and weather patterns using Python.

## 📁 Project Structure

```
graph_data/
├── classes/       # Core simulation classes (Cube, Die, RandomWalk)
├── data/          # Generated images and visual outputs
├── func/          # Helper functions (plotting utilities)
├── notebooks/     # Markdown notes and experiments
├── scripts/       # Visualization scripts to execute
└── weather_data/  # Weather csv files
```

## ▶️ How to Run

Run any visualization script using the module flag:

```bash
python -m scripts.<script_name>
```

**Example:**

```bash
python -m scripts.dice_visual
```

## ⚙️ Requirements

* Python 3.8+
* matplotlib
* numpy
* pandas
* plotly *(optional, for interactive visualizations)*
* pillow *(for image handling and saving)*
