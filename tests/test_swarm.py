from unittest import TestCase, main
from swarm import Swarm
from sys import float_info


class TestSwarm(TestCase):
    def setUp(self):
        # Create an instances of the swarm class
        self.default_swarm = Swarm()
        self.swarm = Swarm(25, (-20.11, 10.5))

    def test_default_init(self):
        self.assertEqual(len(self.default_swarm.particles), 10)
        self.assertEqual(self.default_swarm.position_range, (-4.5, 4.5))
        self.assertEqual(
            self.default_swarm.max_velocity,
            0.2 * (abs(self.default_swarm.position_range[0]) + abs(self.default_swarm.position_range[1]))
        )
        self.assertEqual(self.default_swarm.global_best, float_info.max)

    def test_parametrized_init(self):
        self.assertEqual(len(self.swarm.particles), 25)
        self.assertEqual(self.swarm.position_range, (-20.11, 10.5))
        self.assertEqual(self.swarm.max_velocity, 0.2 * (abs(self.swarm.position_range[0]) + abs(self.swarm.position_range[1])))
        self.assertEqual(self.swarm.global_best, float_info.max)

    def test_keep_within_boundaries(self):
        # Arrange
        swarm = Swarm(1, (-5, 5), 1, 1, 1)
        swarm.particles[0].position.x = -6
        swarm.particles[0].position.y = 6
        swarm.particles[0].velocity.x = -1
        swarm.particles[0].velocity.y = 1

        # Act
        swarm.keep_within_boundaries(swarm.particles[0])

        # Assert
        self.assertEqual(swarm.particles[0].position.x, -4)
        self.assertEqual(swarm.particles[0].position.y, 4)

        self.assertTrue(swarm.particles[0].velocity.x > 0)
        self.assertTrue(swarm.particles[0].velocity.y < 0)


if __name__ == '__main__':
    main()
