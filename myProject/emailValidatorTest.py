from emailValidator import EmailValidator
import re
import unittest
class TestEmailValidator(unittest.TestCase):
    def test_emailValidator(self):
        EmailValidator.emailValidatorChecker(aorjirtk2017@gmail.com)

    def test_emailValidator(self):
        expected = 'aorjirtk2017@gmail.com'
        actual = emailValidator.emailValidatorChecker(userEmail)
        self.assertTrue(expected, actual)