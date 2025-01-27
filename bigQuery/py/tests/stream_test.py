import unittest

import pyarrow
from davidkhala.data.format.arrow.gcp import GCS
from google.api_core.exceptions import PermissionDenied
from google.cloud.bigquery_storage import DataFormat
from google.cloud.bigquery_storage_v1.reader import ReadRowsIterable

from ci import credential
from davidkhala.gcp.bq.stream import Stream

auth_options = credential()


class SyntaxTestCase(unittest.TestCase):
    def test_type(self):
        bq = Stream(auth_options).of(table_id='gcp-data-davidkhala.dbt_davidkhala.country_codes')
        session = bq.create_read_session(DataFormat.ARROW)

        self.assertTrue(session.session.name.startswith('projects/gcp-data-davidkhala/locations/us/sessions/'))


class ArrowTestCase(unittest.TestCase):
    gcs = GCS(credentials=auth_options.credentials)

    def test_stream(self):
        bq = Stream(auth_options).of(table_id='gcp-data-davidkhala.dbt_davidkhala.country_codes')
        session = bq.create_read_session(DataFormat.ARROW)

        uri = "gs://davidkhala-data/gcp-data-davidkhala.dbt_davidkhala.country_codes.arrow"
        for arrowTable in session.arrow:
            self.assertIsInstance(arrowTable, pyarrow.Table)

        # TODO WIP
        # self.gcs.write_stream(uri, _arrow)


class PublicDatasetTestCase(unittest.TestCase):
    def test_read_session(self):
        bq = Stream(auth_options).of(table_id="bigquery-public-data.baseball.games_wide")
        self.assertRaisesRegex(PermissionDenied,
                               "403 request failed: the user does not have 'bigquery.readsessions.create' permission for 'projects/bigquery-public-data'",
                               lambda: bq.create_read_session(DataFormat.ARROW)
                               )


class AvroTestCase(unittest.TestCase):

    def test_avro_stream(self):
        bq = Stream(auth_options).of(table_id='gcp-data-davidkhala.dbt_davidkhala.country_codes')
        session = bq.create_read_session(DataFormat.AVRO)
        for rows in session.arvo:
            self.assertIsInstance(rows, ReadRowsIterable)
            for row in rows:
                self.assertIsInstance(row, dict)
                print(row)
                self.assertIsInstance(row['country_code'], str)
                self.assertIsInstance(row['country_name'], str)


if __name__ == '__main__':
    unittest.main()
