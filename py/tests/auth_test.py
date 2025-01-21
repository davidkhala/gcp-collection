import os
import unittest

from davidkhala.gcp.auth.options import AuthOptions


class SyntaxTestCase(unittest.TestCase):

    def test_from_service_account(self):
        o = AuthOptions.from_service_account(
            client_email=os.environ.get(
                'CLIENT_EMAIL') or 'data-integration@gcp-data-davidkhala.iam.gserviceaccount.com',
            private_key=os.environ.get('PRIVATE_KEY'),
        )
        self.assertEqual(str(type(o.credentials)), "<class 'google.oauth2.service_account.Credentials'>")

    def test_from_api_key(self):
        from google.cloud.compute import RegionsClient
        api_key = os.environ.get('API_KEY')
        client = RegionsClient(
            client_options=AuthOptions.from_api_key(api_key)
        )
        for region in client.list(project='gcp-data-davidkhala'):
            print(region.name)


if __name__ == '__main__':
    unittest.main()
