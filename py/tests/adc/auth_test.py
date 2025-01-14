import unittest

from davidkhala.gcp import AuthOptions


class SyntaxTestCase(unittest.TestCase):
    o2 = AuthOptions.default()
    def test_type(self):
        self.assertEqual(str(type(self.o2.credentials)), "<class 'google.oauth2.credentials.Credentials'>")

if __name__ == '__main__':
    unittest.main()
