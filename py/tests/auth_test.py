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
        from google.cloud.language import LanguageServiceClient, Document
        api_key = os.environ.get('API_KEY')
        client = LanguageServiceClient(
            client_options=AuthOptions.from_api_key(api_key)
        )
        text = "Hello, world!"
        document = Document(
            content=text, type_=Document.Type.PLAIN_TEXT
        )

        # Make a request to analyze the sentiment of the text.
        sentiment = client.analyze_sentiment(
            request={"document": document}
        ).document_sentiment

        self.assertEqual(sentiment.score, sentiment.magnitude)


if __name__ == '__main__':
    unittest.main()
