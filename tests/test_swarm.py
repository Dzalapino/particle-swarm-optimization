from unittest import TestCase
from swarm import Swarm


class TestSwarm(TestCase):
    def setUp(self):
        # Create an instances of the swarm class
        self.default_swarm = Swarm()
        self.swarm = Swarm(25, (-20.11, 10.5))

    def test_default_init(self):
        self.assertEqual(len(self.default_swarm.particles), 10)
        self.assertEqual(self.default_swarm.boundaries, (-4.5, 4.5))
        self.assertEqual(
            self.default_swarm.max_velocity,
            0.2 * (abs(self.default_swarm.boundaries[0]) + abs(self.default_swarm.boundaries[1]))
        )

    def test_parametrized_init(self):
        self.assertEqual(len(self.swarm.particles), 25)
        self.assertEqual(self.swarm.boundaries, (-20.11, 10.5))
        self.assertEqual(self.swarm.max_velocity, 0.2 * (abs(self.swarm.boundaries[0]) + abs(self.swarm.boundaries[1])))

    def test_keep_within_boundaries(self):
        self.fail()
