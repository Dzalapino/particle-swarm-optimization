"""
Module used for the whole swarm management
it does a, b, c...
"""

from vector2 import random_vector_in_range
from particle import Particle


class Swarm:
    def __init__(self, n_particles=10, position_range=(-4.5, 4.5)):
        if position_range[0] >= position_range[1]:
            raise Exception('first value of position_range parameter should be lower than the second one')

        self.boundaries: tuple[float, float] = position_range
        # Boundary for the velocity. Typically set as a fraction of search space
        self.max_velocity: float = 0.2 * (abs(position_range[0]) + abs(position_range[1]))
        self.particles: list[Particle] = []

        # Generate n particles
        for _ in range(n_particles):
            self.particles.append(
                Particle(
                    # Random position within known range
                    random_vector_in_range(self.boundaries[0], self.boundaries[1]),
                    # Random velocity within range that is fracture of max velocity
                    random_vector_in_range(-0.2 * self.max_velocity, 0.2 * self.max_velocity)
                )
            )

    def keep_within_boundaries(self):
        pass
