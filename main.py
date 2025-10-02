import matplotlib.pyplot as plt
from src.cube import Cube
from src.plotting import plot_cube, plot_randomwalk
from src.random_walk import RandomWalk

"""Simulating Random Walks"""
plt.style.use("classic")
fig, ax = plt.subplots()
rw = RandomWalk(20)
rw.fill_walk()
plot_randomwalk(rw, ax)
plt.show()

"""Simulating Cube"""
plt.style.use("dark_background")
cube = Cube(r=5)
fig, ax = plt.subplots()
plot_cube(cube, ax, linewidth=2)
plt.show()
