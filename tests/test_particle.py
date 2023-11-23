from unittest import TestCase, main
from particle import Particle
from vector2 import Vector2


class TestVector2(TestCase):
    def setUp(self):
        # Create an instance of the Particle class
        self.particle = Particle(Vector2(2.0, 3.0), Vector2(3.0, 2.0))

    def test_init(self):
        self.assertEqual(self.particle.position.x, 2.0)
        self.assertEqual(self.particle.position.y, 3.0)
        self.assertEqual(self.particle.velocity.x, 3.0)
        self.assertEqual(self.particle.velocity.y, 2.0)
        self.assertIsNone(self.particle.particle_best)

    def test_str(self):
        self.assertEqual(
            self.particle.__str__(),
            f'Particle position: {self.particle.position}, velocity: {self.particle.velocity}'
        )


if __name__ == '__main__':
    main()
