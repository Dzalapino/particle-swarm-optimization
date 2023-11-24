"""
Module used for the whole swarm management
it does a, b, c...
"""
import random

from vector2 import random_vector_in_range, Vector2
from particle import Particle
from sys import float_info


class Swarm:
    def __init__(self, n_particles=10, position_range=(-4.5, 4.5), inertia=0.9, c1=1.5, c2=1.5):
        if position_range[0] >= position_range[1]:
            raise Exception('first value of position_range parameter should be lower than the second one')

        self.position_range: tuple[float, float] = position_range
        # Inertia parameter will be decreased in every iteration
        self.inertia: float = inertia
        # Cognitive and social coefficients. These parameters control the ratio of exploration and exploitation
        self.cognitive_coefficient = c1
        self.social_coefficient = c2
        # Boundary for the velocity. Typically set as a fraction of search space
        self.max_velocity: float = 0.2 * (abs(position_range[0]) + abs(position_range[1]))
        self.global_best: Vector2 = Vector2(0, float_info.max)
        self.particles: list[Particle] = []

        # Generate n particles
        for _ in range(n_particles):
            particle = Particle(
                # Random position within known range
                random_vector_in_range(self.position_range[0], self.position_range[1]),
                # Random velocity within range that is fracture of max velocity
                random_vector_in_range(-0.2 * self.max_velocity, 0.2 * self.max_velocity)
            )
            # Set particle personal best to it's initial position
            particle.personal_best = particle.position
            # Check if that's new global best
            if particle.position.y < self.global_best.y:
                self.global_best = particle.position

            self.particles.append(particle)

    def check_best(self, particle: Particle) -> None:
        """
        Check if particle found it's new personal best and if it is the new global best. If so, update those values
        :param particle: particle to check
        :return: None
        """
        if particle.position.y < particle.personal_best.y:  # Personal check
            particle.personal_best = particle.position

        if particle.position.y < self.global_best.y:  # Global check
            self.global_best = particle.position

    def keep_within_boundaries(self, particle: Particle) -> None:
        # Calculate separation values
        left = self.position_range[0] - particle.position.x
        right = self.position_range[1] - particle.position.x
        bottom = self.position_range[0] - particle.position.y
        top = self.position_range[1] - particle.position.y

        # Make boundary checks and apply separation if needed
        if left > 0:  # Left range check
            particle.position.x = self.position_range[0] + left
            particle.velocity.x *= -1
        elif right < 0:  # Right range check
            particle.position.x = self.position_range[1] + right
            particle.velocity.x *= -1
        if bottom > 0:  # Left range check
            particle.position.y = self.position_range[0] + bottom
            particle.velocity.y *= -1
        elif top < 0:  # Right range check
            particle.position.y = self.position_range[1] + top
            particle.velocity.y *= -1

    def update_particles(self) -> None:
        # Decrease inertia
        for particle in self.particles:
            # Update velocities
            particle.velocity += particle.velocity * self.inertia
            particle.velocity += self.cognitive_coefficient * random.random() * (particle.personal_best - particle.position)
            particle.velocity += self.social_coefficient * random.random() * (self.global_best - particle.position)

            # Update positions
            particle.position += particle.velocity

            # Check if particles stay within boundaries, if not -> position = limit - amount_exceeding_limit
            self.keep_within_boundaries(particle)

            # Check if particle found new best personal and if that's new global best
            self.check_best(particle)
