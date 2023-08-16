import unittest

from CrossCutting.ErrorHandling import ErrorHandling


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.handling = ErrorHandling()

    def test_something(self, test=True):
        self.assertEqual(True, test)  # add assertion here

    def test_valid_password(self):
        # Arrange
        test_pw = "password"

        # Act
        self.handling.is_valid_password(test_pw)

        # Assert
        self.assertTrue(True, self.handling.response.is_successful)
        self.assertEqual("Valid Password", self.handling.response.message)

    def test_password_contains_space(self):
        # Arrange
        test_pw = "password "
        message = "No spaces. Enter new password"

        # Act
        self.handling.is_valid_password(test_pw)

        # Assert
        self.assertEqual(self.handling.response.message, message)
        self.assertFalse(self.handling.response.is_successful, False)


    def test_invalid_special_characters(self):
        test_pw = "password{"
        message = "Invalid Password. Allowed characters: (@, !, $, ., -)"

        self.handling.is_valid_password(test_pw)

        self.assertFalse(self.handling.response.is_successful, False)
        self.assertEqual(message, self.handling.response.message)

    def test_valid_email(self):
        test_email = "email@yahoo.com"
        message = "Valid email"

        self.handling.is_valid_email(test_email)

        self.assertTrue(self.handling.response.is_successful)
        self.assertEqual(self.handling.response.message, message)

    def test_invalid_email(self):
        test_email = "email@.com"
        message = "Not a valid email"

        self.handling.is_valid_email(test_email)

        self.assertFalse(self.handling.response.is_successful)
        self.assertEqual(self.handling.response.message, message)







if __name__ == '__main__':
    unittest.main()
