import unittest

from google.cloud.bigquery_storage import DataFormat
from davidkhala.gcp.bq.stream import BigQueryStream
from ci import credential
table_id = 'gcp-data-davidkhala.dbt_davidkhala.country_codes'

class StreamTestCase(unittest.TestCase):
    def test_read_stream(self):
        bq = BigQueryStream(credential()).of(table_id=table_id)
        session = bq.create_read_session(DataFormat.ARROW)
        self.assertTrue(session.name.startswith('projects/gcp-data-davidkhala/locations/us/sessions/'))



if __name__ == '__main__':
    unittest.main()
