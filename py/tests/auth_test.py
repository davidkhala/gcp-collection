import os
import unittest

from davidkhala.gcp import AuthOptions


class SyntaxTestCase(unittest.TestCase):

    def test_from_service_account(self):
        o = AuthOptions.from_service_account(
            client_email=os.environ.get(
                'CLIENT_EMAIL') or 'data-integration@gcp-data-davidkhala.iam.gserviceaccount.com',
            project_id='freetier-only',
            private_key=os.environ.get('PRIVATE_KEY'),
        )
        self.assertEqual(str(type(o.credentials)), "<class 'google.oauth2.service_account.Credentials'>")
    def test_always_green(self):
        pass

if __name__ == '__main__':
    unittest.main()
