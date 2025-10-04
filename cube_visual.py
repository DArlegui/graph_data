import matplotlib.pyplot as plt
from classes.cube import Cube
from func.plotting import plot_cube

"""Simulating Cube"""
plt.style.use("dark_background")
cube = Cube(r=100)
fig, ax = plt.subplots()
plot_cube(cube, ax, linewidth=2)
plt.show()
