import os
import unittest

from davidkhala.gcp import GoogleAuthOptions


class SyntaxTestCase(unittest.TestCase):
    def test_type(self):
        o = GoogleAuthOptions.from_service_account(
            client_email=os.environ['CLIENT_EMAIL'],
            project_id='freetier-only',
            private_key=os.environ['PRIVATE_KEY'],
        )
        self.assertEqual(str(type(o.credentials)), "<class 'google.oauth2.service_account.Credentials'>")
        o2 = GoogleAuthOptions.default()
        self.assertEqual(str(type(o2.credentials)), "<class 'google.oauth2.credentials.Credentials'>")


if __name__ == '__main__':
    unittest.main()
