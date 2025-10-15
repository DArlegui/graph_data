# Molecular Motion.py
import matplotlib.pyplot as plt
from classes.random_walk import RandomWalk
from func.plotting import plot_molecular

"""Simulating Molecular Motion"""
plt.style.use("classic")
fig, ax = plt.subplots()
rw = RandomWalk(1000)
rw.fill_walk()
plot_molecular(rw, ax)  # sets molecular=True
plt.show()
