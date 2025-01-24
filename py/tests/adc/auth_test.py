import datetime
import unittest

from google.auth.credentials import TokenState
from google.oauth2.credentials import Credentials

from davidkhala.gcp.auth.options import default


class SyntaxTestCase(unittest.TestCase):

    def test_type(self):
        o2 = default()
        credentials = o2.credentials
        self.assertIsInstance(credentials, Credentials)
        self.assertEqual(credentials.token_state, TokenState.INVALID)
        self.assertIsInstance(credentials.expiry, datetime.datetime)
        self.assertIsNotNone(credentials.expiry)
        print(o2.token)


if __name__ == '__main__':
    unittest.main()
