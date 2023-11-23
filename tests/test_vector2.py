from unittest import TestCase
from vector2 import random_vector_in_range, Vector2


class TestVector2(TestCase):
    def setUp(self):
        pass

    def test_random_vector_in_range(self):
        random_vector = random_vector_in_range(4, 5)