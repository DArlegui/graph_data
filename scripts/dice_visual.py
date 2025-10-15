from classes.die import Die
import plotly.express as px

die_1 = Die(6)
die_2 = Die(6)

# Storing roll results
results = [die_1.roll() * die_2.roll() for _ in range(1000)]

# Analyze the results
max_result = die_1.size_of_die() * die_2.size_of_die()
poss_results = range(2, max_result + 1)

# counts how many # times appeared
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = f"Results of (Multiply) Rolling Two D{die_1.size_of_die()} Dice 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
