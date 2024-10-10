import unittest
from unittest import TestCase


from biggestodd import biggest_odd


class TestBigOdd(TestCase):
    def test_that_biggest_odd_function_exists(self):
        biggest_odd("2345988")

    def test_that_biggest_odd_function(self):
        self.assertEqual(biggest_odd("2345988"), 9)

class TestKeyCube(unittest.TestCase):
    def test_that_key_cube_function_exists(self):
        biggest_odd.get_key_cube([1, 2, 3, 4, 5])

    def test_that_get_cube_function_returns_dict(self):
        actual = biggest_odd.get_key_cube([1, 2, 3, 4, 5])
        expected = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125 }
        self.assertEqual(actual, expected)