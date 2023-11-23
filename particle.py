"""
Module responsible for the particle objects, storing its properties
"""

from vector2 import Vector2


class Particle:
    def __init__(self, position: Vector2, velocity: Vector2):
        self.position = position
        self.velocity = velocity
        self.particle_best = None

    def __str__(self) -> str:
        return f'Particle position: {self.position}, velocity: {self.velocity}'
