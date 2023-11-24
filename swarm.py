"""
Module used for the whole swarm management
it does a, b, c...
"""

from vector2 import random_vector_in_range, Vector2
from particle import Particle
from typing import Callable
from sys import float_info
import random


class Swarm:
    def __init__(
            self, function: Callable[[Vector2], float], n_particles=30, position_range=(-4.5, 4.5),
            init_inertia=1, min_inertia=0.2, inertia_step=0.05, c1=3, c2=3
    ):
        if n_particles < 1:
            raise Exception('There have to be at least one particle to spawn')
        if position_range[0] >= position_range[1]:
            raise Exception('First value of position_range parameter should be lower than the second one')

        self.function: Callable[[Vector2], float] = function
        self.position_range: tuple[float, float] = position_range
        # Inertia parameter will be decreased in every iteration
        self.inertia: float = init_inertia
        self.min_inertia: float = min_inertia
        self.inertia_step: float = inertia_step
        # Cognitive and social coefficients. These parameters control the ratio of exploration and exploitation
        self.cognitive_coefficient = c1
        self.social_coefficient = c2
        # Boundary for the velocity. Typically set as a fraction of search space
        self.max_velocity: float = 0.2 * (abs(position_range[0]) + abs(position_range[1]))
        self.global_best: Vector2 = Vector2(0, float_info.max)
        self.particles: list[Particle] = []

        # Generate first particle
        self.generate_particle(True)

        # Generate n-1 remaining particles
        for _ in range(n_particles - 1):
            self.generate_particle()

    def generate_particle(self, first_particle = False) -> None:
        if first_particle:
            particle = Particle(
                # Random position within known range
                random_vector_in_range(self.position_range[0], self.position_range[1]),
                # Random velocity within range that is fracture of max velocity
                random_vector_in_range(-0.2 * self.max_velocity, 0.2 * self.max_velocity)
            )
            # Init global best as first particle position
            self.global_best = particle.position
            self.particles.append(particle)
        else:
            particle = Particle(
                # Random position within known range
                random_vector_in_range(self.position_range[0], self.position_range[1]),
                # Random velocity within range that is fracture of max velocity
                random_vector_in_range(-0.2 * self.max_velocity, 0.2 * self.max_velocity)
            )
            # Check if that's new global best
            if self.function(particle.personal_best) < self.function(self.global_best):
                self.global_best = particle.personal_best
            self.particles.append(particle)

    def check_best(self, particle: Particle) -> None:
        """
        Check if particle found it's new personal best and if it is the new global best. If so, update those values
        :param particle: particle to check
        :return: None
        """
        particle.is_new_best(self.function)
        if self.function(particle.position) < particle.personal_best.y:  # Personal check
            particle.personal_best = particle.position

        if self.function(particle.position) < self.function(self.global_best):  # Global check
            self.global_best = particle.position

    def keep_position_within_range(self, particle: Particle) -> None:
        """
        Check if particle is within boundaries. If not, move it into boundaries and inverse it's velocity
        :param particle: particle to keep within boundaries
        :return: None
        """
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

    def keep_velocity_within_range(self, particle: Particle) -> None:
        """
        Check if velocity is not exceeding it's given max value and update if it is
        :param particle: particle to check
        :return: None
        """
        # Check for horizontal velocity
        if particle.velocity.x > self.max_velocity:
            particle.velocity.x = self.max_velocity
        elif particle.velocity.x < -1 * self.max_velocity:
            particle.velocity.x = -1 * self.max_velocity

        # Check for vertical velocity
        if particle.velocity.y > self.max_velocity:
            particle.velocity.y = self.max_velocity
        elif particle.velocity.y < -1 * self.max_velocity:
            particle.velocity.y = -1 * self.max_velocity

    def update_particles(self) -> None:
        """
        Updating all particles in the swarm with new velocities, positions, checking new personal and global best
        :return: None
        """
        # TODO: Think about stopping criteria (all particles scattered around minimum in given bounds)
        #  and inertia decreasing amount

        # Decrease inertia
        if self.inertia > self.min_inertia:
            self.inertia -= self.inertia_step

        for particle in self.particles:
            # Update velocities
            particle.velocity += particle.velocity * self.inertia
            particle.velocity += (particle.personal_best - particle.position) * self.cognitive_coefficient * random.random()
            particle.velocity += (self.global_best - particle.position) * self.social_coefficient * random.random()

            # Update positions
            self.keep_velocity_within_range(particle)  # Limit the speed if needed
            particle.position += particle.velocity
            self.keep_position_within_range(particle)  # Check for particles that left the range

            self.check_best(particle)  # Find personal and global best

    def get_x_positions(self) -> list[float]:
        return [particle.position.x for particle in self.particles]

    def get_y_positions(self) -> list[float]:
        return [particle.position.y for particle in self.particles]
