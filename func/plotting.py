#plotting.py
import matplotlib.pyplot as plt
from classes.random_walk import RandomWalk

""" DRY Principle """
def get_fig_ax(ax=None):
    """Return a (fig, ax) tuple, creating a new subplot if ax is None."""
    return plt.subplots() if ax is None else (ax.figure, ax)

def set_ax_fig_randomplot(ax, rw):
    ax.set_aspect("equal")
    ax.set_xlabel("x_direction")
    ax.set_ylabel("y_direction")

    # Emphasize the first and last points.
    ax.scatter(0, 0, c="#00e676", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="#ef5350", edgecolors="none", s=100)

    # Remove the axes.
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    return ax

"""Plotting Functions"""
def plot_cube(cube, ax=None, **line_kwargs):
    fig, ax = get_fig_ax(ax)

    ax.plot(cube.x_values, cube.y_values, **line_kwargs)
    ax.set_title("Cubed Numbers")
    ax.set_xlabel("Value")
    ax.set_ylabel("Cubed Value")
    ax.tick_params(labelsize=14)

    return fig, ax

def plot_molecular(rw: RandomWalk, ax=None):
    fig, ax = get_fig_ax(ax)
    ax.plot(rw.x_values, rw.y_values, color='green', linewidth=1)
    ax.set_title("Molecular Motion")

    set_ax_fig_randomplot(ax, rw)

    return fig, ax


def plot_randomwalk(rw: RandomWalk, ax=None, molecular=False):
    fig, ax = get_fig_ax(ax)

    point_numbers = range(rw.num_points) #generate a list of n == n of points
    """ Lower values (earlier steps in the walk) → lighter color
        Higher values (later steps) → darker color   """
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Grays, edgecolors='none', s=3)
    ax.set_title("Random Walk Simulator")

    set_ax_fig_randomplot(ax, rw)

    return fig, ax
