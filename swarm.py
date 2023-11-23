"""
Module used for the whole swarm management
it does a, b, c...
"""

import random
from vector2 import Vector2, random_vector_in_range
from particle import Particle


class Swarm:
    def __init__(self, n_particles=10, position_range=(-4.5, 4.5), velocity_range=()):
        self.boundaries: tuple[float, float] = position_range
        self.particles: list[Particle] = []

        # Generate n particles with random positions and velocities within given boundaries
        for _ in range(n_particles):
            self.particles.append(
                Particle(
                    random_vector_in_range(position_range[0], position_range[1]),
                    # TODO: Think about initial random velocity boundaries
                    random_vector_in_range(velocity_range[0], velocity_range[1])
                )
            )

    def keep_within_boundaries(self):
        pass
