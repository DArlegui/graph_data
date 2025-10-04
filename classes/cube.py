from typing import Iterable, List


class Cube:
    def __init__(self, r=5):
        self.r = r

    @property
    def x_values(self) -> Iterable[int]:
        return range(1, self.r)

    @property
    def y_values(self) -> List[int]:
        return [x**3 for x in self.x_values]


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
