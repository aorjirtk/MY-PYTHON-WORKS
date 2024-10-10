
from passwordGenerator import PasswordGenerator
import unittest
PasswordGenerator()
class TestPasswordGenerator(unittest.TestCase):
    def test_that_length_of_characters_six(self):
        expected = PasswordGenerator.get_length_of_characters_in_password(length= 6)
        actual = 6
        self.assertEqual(expected, actual)

    def test_that_length_of_digits_in_password_six(self):
        expected = PasswordGenerator.get_length_of_digits_in_password(length=6)
        actual = 6
        self.assertEqual(expected, actual)

    def test_that_length_of_punctuation_in_password_four(self):
        expected = PasswordGenerator.get_length_of_punctuations_password(length=4)
        actual = 4
        self.assertEqual(expected, actual)
    def test_that_length_of_password_sixteen(self):
        expected = PasswordGenerator.get_length_of_passwords()
        actual = 16
        self.assertEqual(expected, actual)
