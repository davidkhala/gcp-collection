import unittest

from davidkhala.data.format.arrow.gcp import GCS
from davidkhala.data.format.arrow.local_fs import LocalFS
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
    gcs = GCS(auth_options=auth_options)

    def test_write_stream(self):
        table_id = 'gcp-data-davidkhala.dbt_davidkhala.country_codes'
        bq = Stream(auth_options).of(table_id=table_id)
        session = bq.create_read_session(DataFormat.ARROW)

        local = LocalFS()
        local.write_stream(f"artifacts/{table_id}.arrow", session.arrow)


class PublicDatasetTestCase(unittest.TestCase):

    def test_read_directly(self):
        bq = Stream(auth_options).of(table_id="bigquery-public-data.baseball.games_wide")
        self.assertRaisesRegex(PermissionDenied,
                               "403 request failed: the user does not have 'bigquery.readsessions.create' permission for 'projects/bigquery-public-data'",
                               lambda: bq.create_read_session(DataFormat.ARROW)
                               )

    def test_arrow_write_stream(self):
        table_id = "gcp-data-davidkhala.baseball.games_post_wide"
        bq = Stream(auth_options).of(table_id=table_id)
        session = bq.create_read_session(DataFormat.ARROW)
        file_name = f"{table_id}.arrow"
        self.assertEqual(1, session.count)

        # it consumes 7sec
        uri = f"gs://davidkhala-data/{file_name}"
        gcs = GCS(auth_options=auth_options)
        gcs.write_stream(uri, session.arrow)


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
