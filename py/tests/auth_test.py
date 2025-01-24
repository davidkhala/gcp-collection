import os
import unittest
from datetime import datetime

from google.cloud.language import LanguageServiceClient, Document

from davidkhala.gcp.auth.options import from_service_account, from_api_key


class SyntaxTestCase(unittest.TestCase):

    def test_from_service_account(self):
        o = from_service_account(
            client_email=os.environ.get('CLIENT_EMAIL')
                         or 'data-integration@gcp-data-davidkhala.iam.gserviceaccount.com',
            private_key=os.environ.get('PRIVATE_KEY'),
        )
        credentials = o.credentials
        self.assertEqual(str(type(credentials)), "<class 'google.oauth2.service_account.Credentials'>")
        self.assertFalse(credentials.valid)
        self.assertIsNone(credentials.expiry)
        o.token
        self.assertIsNotNone(credentials.expiry)
        self.assertIsInstance(credentials.expiry, datetime)

    def test_from_api_key(self):
        api_key = os.environ.get('API_KEY')
        client = LanguageServiceClient(
            client_options=from_api_key(api_key),
        )
        text = "Hello, world!"

        # Make a request to analyze the sentiment of the text.
        sentiment = client.analyze_sentiment(
            document=Document({
                "content": text,
                "type_": Document.Type.PLAIN_TEXT
            }),
        ).document_sentiment

        self.assertEqual(sentiment.score, sentiment.magnitude)


if __name__ == '__main__':
    unittest.main()
