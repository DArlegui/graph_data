from typing import Iterable, List
from func.plotting import get_fig_ax

class Cube:
    def __init__(self, r=5):
        self.r = r

    @property
    def x_values(self) -> Iterable[int]:
        return range(1, self.r)

    @property
    def y_values(self) -> List[int]:
        return [x**3 for x in self.x_values]


def plot_cube(cube, ax=None, **line_kwargs):
    fig, ax = get_fig_ax(ax)

    ax.plot(cube.x_values, cube.y_values, **line_kwargs)
    ax.set_title("Cubed Numbers")
    ax.set_xlabel("Value")
    ax.set_ylabel("Cubed Value")
    ax.tick_params(labelsize=14)

    return fig, ax


# from dataclasses import dataclass
# @dataclass  # automatically makes a constructor that stores r
# class Cube:
#     r: int  # exclusive upper bound

#     @property
#     def x_values(self) -> Iterable[int]:
#         return range(1, self.r)

#     @property
#     def y_values(self) -> List[int]:
#         return [x**3 for x in self.x_values]
