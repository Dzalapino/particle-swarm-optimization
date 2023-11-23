"""
Module responsible for the particle objects, storing its properties
"""

from vector2 import Vector2
from sys import float_info


class Particle:
    def __init__(self, position: Vector2, velocity: Vector2):
        self.position = position
        self.velocity = velocity
        self.personal_best = Vector2(0, float_info.max)

    def __str__(self) -> str:
        return f'Particle position: {self.position}, velocity: {self.velocity}'
