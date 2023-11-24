from unittest import TestCase, main
from vector2 import random_vector_in_range, Vector2


class TestVector2(TestCase):
    def setUp(self):
        self.vector1 = Vector2(-1.0, -1.0)
        self.vector2 = Vector2(1.0, 1.0)

    def test_init(self):
        self.assertEqual(self.vector1.x, -1.0)
        self.assertEqual(self.vector1.y, -1.0)
        self.assertEqual(self.vector2.x, 1.0)
        self.assertEqual(self.vector2.y, 1.0)

    def test_add(self):
        result = self.vector1 + self.vector2
        self.assertEqual(result.x, 0.0)
        self.assertEqual(result.y, 0.0)

    def test_sub(self):
        result = self.vector1 - self.vector2
        self.assertEqual(result.x, -2.0)
        self.assertEqual(result.y, -2.0)

    def test_mul(self):
        result = self.vector1 * 10
        self.assertEqual(result.x, -10.0)
        self.assertEqual(result.y, -10.0)

    def test_eq(self):
        result = Vector2(2.0, 3.0) == Vector2(2.0, 3.0)
        self.assertTrue(result)

    def test_random_vector_in_range(self):
        result = random_vector_in_range(4, 5)
        self.assertTrue(4 <= result.x <= 5)
        self.assertTrue(4 <= result.y <= 5)

    def test_random_vector_in_range_raises_exception(self):
        with self.assertRaises(Exception):
            random_vector_in_range(100, 1)


if __name__ == '__main__':
    main()
