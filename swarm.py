"""
Module used for the whole swarm management
it does a, b, c...
"""

from vector2 import random_vector_in_range
from particle import Particle
from sys import float_info


class Swarm:
    def __init__(self, n_particles=10, position_range=(-4.5, 4.5), inertia=0.9):
        if position_range[0] >= position_range[1]:
            raise Exception('first value of position_range parameter should be lower than the second one')

        self.boundaries: tuple[float, float] = position_range
        # Inertia parameter will be decreased in every iteration
        self.inertia = inertia
        # Boundary for the velocity. Typically set as a fraction of search space
        self.max_velocity: float = 0.2 * (abs(position_range[0]) + abs(position_range[1]))
        self.global_best = float_info.max
        self.particles: list[Particle] = []

        # Generate n particles
        for _ in range(n_particles):
            particle = Particle(
                # Random position within known range
                random_vector_in_range(self.boundaries[0], self.boundaries[1]),
                # Random velocity within range that is fracture of max velocity
                random_vector_in_range(-0.2 * self.max_velocity, 0.2 * self.max_velocity)
            )
            # Set particle personal best to it's initial position
            particle.personal_best = particle.position
            # Update best known position
            if particle.personal_best.y < self.global_best:
                self.global_best = particle.personal_best.y

            self.particles.append(particle)

    def keep_within_boundaries(self):
        pass

    def update(self):
        # Decrease inertia

        # Update velocities

        # Update positions

        # Check if particles stay within boundaries, if not -> position = limit - amount_exceeding_limit

        # Check if particle found new best personal and if that's new global best

        pass
