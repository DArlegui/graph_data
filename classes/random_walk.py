from random import choice, randint
# np.random.normal() generates random numbers that follow a bell curve
import numpy as np

class RandomWalk:

    def __init__(self, num_points=10):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self, always_pos=False, max_range=4):
        direction = 1 if always_pos else choice([1, -1])
        distance = randint(0, max_range)
        return direction * distance

    def fill_walk(self):
        """Calculate all the points in the walk"""
        # Keep taking steps until the walk reaches
        while len(self.x_values) < self.num_points:
            # Decide which direction to go, and how far to go.
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
