"""
Module responsible for the particle objects, storing its properties
"""

from vector2 import Vector2
from typing import Callable


class Particle:
    def __init__(self, position: Vector2, velocity: Vector2):
        """
        Create new particle with given initial position and velocity.
        Personal best is being set as it's initial position
        :param position: particle initial position
        :param velocity: particle initial velocity
        """
        self.position: Vector2 = position
        self.velocity: Vector2 = velocity
        self.personal_best: Vector2 = position

    def __str__(self) -> str:
        return f'Particle position: {self.position}, velocity: {self.velocity}'

    def is_new_best(self, function: Callable[[Vector2], float]) -> None:
        """
        Method checks if current particle position with provided function gives new personal best.
        If that is the case the personal best is being updated with the current position
        :param function: function evaluating the value in current position
        :return: None
        """
        if function(self.position) < function(self.personal_best):
            self.personal_best = self.position
