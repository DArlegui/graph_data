import matplotlib.pyplot as plt


def get_fig_ax(ax=None):
    """Return a (fig, ax) tuple, creating a new subplot if ax is None."""
    return plt.subplots() if ax is None else (ax.figure, ax)


def plot_cube(cube, ax=None, **line_kwargs):
    fig, ax = get_fig_ax(ax)

    ax.plot(cube.x_values, cube.y_values, **line_kwargs)
    ax.set_title("Cubed Numbers")
    ax.set_xlabel("Value")
    ax.set_ylabel("Cubed Value")
    ax.tick_params(labelsize=14)

    return fig, ax


def plot_randomwalk(rw, ax=None):
    fig, ax = get_fig_ax(ax)

    ax.scatter(rw.x_values, rw.y_values, color=(0, 0.8, 0), s=15)
    ax.set_aspect("equal")

    return fig, ax
