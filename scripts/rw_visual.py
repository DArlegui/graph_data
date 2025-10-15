# Random Walks.py
import matplotlib.pyplot as plt
from classes.random_walk import RandomWalk
from func.plotting import plot_randomwalk

"""Simulating Random Walks"""

while True:
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    rw = RandomWalk(5000)
    rw.fill_walk()

    """ Using random walk """
    plot_randomwalk(rw, ax)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
