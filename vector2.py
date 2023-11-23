"""
Custom two-dimensional vector module
"""

import random


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Vector2({self.x, self.y})'


def random_vector_in_range(range_min: float, range_max: float) -> Vector2:
    return Vector2(random.uniform(range_min, range_max), random.uniform(range_min, range_max))
