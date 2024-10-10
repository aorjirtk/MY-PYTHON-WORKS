import unittest

from tuple import listortuple


class tuple(unittest.TestCase):
    def test_28_function(self):
        tuple.listortuple("34,67,55,33,12,98")

    def test_tuple_returns_list(self):
        expected = tuple.listortuple("34,67,55,33,12,98")
        self.assertEqual(expected, "['34', '67', '55', '33', '12', '98']('34', '67', '55', '33', '12', '98')")