from unittest import TestCase, main
from swarm import Swarm
from vector2 import Vector2
import numpy as np


class TestSwarm(TestCase):
    def setUp(self):
        def f(vector: Vector2) -> float:
            return (
                    np.power((1.5 - vector.x - vector.x * vector.y), 2) +
                    np.power((2.25 - vector.x + vector.x * np.power(vector.y, 2)), 2) +
                    np.power((2.625 - vector.x + vector.x * np.power(vector.y, 3)), 2)
            )

        def g(vector: Vector2) -> float:
            return vector.x**2 + vector.x*vector.y

        self.function1 = f
        self.function2 = g

        # Create an instances of the swarm class
        self.default_swarm = Swarm(self.function1)
        self.swarm = Swarm(self.function1, 25, (-3.75, 3.75), 0.7, 0.4, 0.05, 1.5, 1.5)

    def test_default_init(self):
        self.assertEqual(len(self.default_swarm.particles), 30)
        self.assertEqual(self.default_swarm.position_range, (-4.5, 4.5))
        self.assertEqual(self.default_swarm.max_velocity, 0.2 * 9.0)
        self.assertEqual(self.default_swarm.inertia, 1)
        self.assertEqual(self.default_swarm.min_inertia, 0.2)
        self.assertEqual(self.default_swarm.inertia_step, 0.05)

    def test_parametrized_init(self):
        self.assertEqual(len(self.swarm.particles), 25)
        self.assertEqual(self.swarm.position_range, (-3.75, 3.75))
        self.assertEqual(self.swarm.max_velocity, 0.2 * 7.5)
        self.assertEqual(self.swarm.inertia, 0.7)
        self.assertEqual(self.swarm.min_inertia, 0.4)

    def test_check_best(self):
        # Arrange
        swarm = Swarm(self.function2, 1)
        swarm.particles[0].position = Vector2(2.0, 2.0)
        swarm.global_best = Vector2(3.0, 3.0)

        # Act
        swarm.check_best(swarm.particles[0])

        # Arrange
        self.assertEqual(swarm.global_best, Vector2(2.0, 2.0))

    def test_keep_position_within_range(self):
        # Arrange
        swarm = Swarm(self.function1, 1, (-1, 1), 1, 1, 1)
        swarm.particles[0].position.x = -2
        swarm.particles[0].position.y = 2
        swarm.particles[0].velocity.x = -1
        swarm.particles[0].velocity.y = 1

        # Act
        swarm.keep_position_within_range(swarm.particles[0])

        # Assert
        self.assertEqual(swarm.particles[0].position, Vector2(0, 0))
        self.assertTrue(swarm.particles[0].velocity.x > 0)
        self.assertTrue(swarm.particles[0].velocity.y < 0)

    def test_keep_velocity_within_range(self):
        # Arrange
        swarm = Swarm(self.function1, 1)
        swarm.max_velocity = 10
        swarm.particles[0].velocity.x = -12
        swarm.particles[0].velocity.y = 13

        # Act
        swarm.keep_velocity_within_range(swarm.particles[0])

        # Assert
        self.assertEqual(swarm.particles[0].velocity.x, -10)
        self.assertEqual(swarm.particles[0].velocity.y, 10)


if __name__ == '__main__':
    main()
