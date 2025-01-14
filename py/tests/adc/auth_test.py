import unittest

from davidkhala.gcp.auth.options import AuthOptions


class SyntaxTestCase(unittest.TestCase):

    def test_type(self):
        o2 = AuthOptions.default()
        self.assertEqual(str(type(o2.credentials)), "<class 'google.oauth2.credentials.Credentials'>")

if __name__ == '__main__':
    unittest.main()
