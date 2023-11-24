from unittest import TestCase, main
from typing import Callable
from particle import Particle
from vector2 import Vector2


class TestVector2(TestCase):
    def setUp(self):
        def f(vector: Vector2) -> float:
            return vector.x * vector.y**2
        self.func1 = f
        self.particle = Particle(Vector2(2.0, 3.0), Vector2(3.0, 2.0))

    def test_init(self):
        self.assertEqual(self.particle.position, Vector2(2.0, 3.0))
        self.assertEqual(self.particle.velocity, Vector2(3.0, 2.0))
        self.assertEqual(self.particle.personal_best, Vector2(2.0, 3.0))

    def test_str(self):
        self.assertEqual(
            self.particle.__str__(),
            f'Particle position: {self.particle.position}, velocity: {self.particle.velocity}'
        )

    def test_is_new_best_given_better_position_update(self):
        # Arrange
        particle = Particle(Vector2(2., 2.), Vector2(2., 2.))

        # Act
        particle.position = Vector2(1., 1.)
        particle.is_new_best(self.func1)

        # Assert
        self.assertEqual(particle.personal_best, Vector2(1., 1.))

    def test_is_new_best_given_worse_position_dont_update(self):
        # Arrange
        particle = Particle(Vector2(2., 2.), Vector2(2., 2.))

        # Act
        particle.position = Vector2(3., 3.)
        particle.is_new_best(self.func1)

        # Assert
        self.assertEqual(particle.personal_best, Vector2(2., 2.))


if __name__ == '__main__':
    main()
