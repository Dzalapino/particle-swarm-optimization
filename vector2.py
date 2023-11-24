"""
Custom two-dimensional vector module
"""

import random


class Vector2:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __str__(self) -> str:
        return f'Vector2({self.x, self.y})'


def random_vector_in_range(range_min: float, range_max: float) -> Vector2:
    """
    Generate random vector in given range
    :param range_min: lower limit for the vector values
    :param range_max: upper limit for the vector values
    :return: Vector2(x, y)
    """
    # Check if min range is lower than max range
    if range_min >= range_max:
        raise Exception('range_min should be lower than range_max')

    return Vector2(random.uniform(range_min, range_max), random.uniform(range_min, range_max))
