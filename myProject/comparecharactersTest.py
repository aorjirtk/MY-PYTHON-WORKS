import unittest
from unittest import TestCase

from comparecharacters import compare_characters

class TestCompareCharacters(TestCase):
    def test_that_function_compares_characters(self):
       self.assertTrue(compare_characters("love", "evol"))

    def test_that_function_compares_characters2(self):
        self.assertTrue(compare_characters("love", "love"), True)
        if__name ==  '__main__':
        unittest.main()





