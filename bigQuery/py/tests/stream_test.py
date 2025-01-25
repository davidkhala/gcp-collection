import unittest

import pyarrow
from davidkhala.data.format.arrow.gcp import GCS
from google.cloud.bigquery_storage import DataFormat, ReadSession
from google.cloud.bigquery_storage_v1.reader import ReadRowsIterable

from ci import credential
from davidkhala.gcp.bq.stream import BigQueryStream

auth_options = credential()


class ArrowTestCase(unittest.TestCase):
    gcs = GCS(credentials=auth_options.credentials)

    def test_stream(self):
        bq = BigQueryStream(auth_options).of(table_id='gcp-data-davidkhala.dbt_davidkhala.country_codes')
        session = bq.create_read_session(DataFormat.ARROW)
        self.assertIsInstance(session, ReadSession)
        self.assertTrue(session.name.startswith('projects/gcp-data-davidkhala/locations/us/sessions/'))

        uri = "gs://davidkhala-data/gcp-data-davidkhala.dbt_davidkhala.country_codes.arrow"
        for index, [rows, _arrow, _] in enumerate(bq.read(session)):
            self.assertIsInstance(rows, ReadRowsIterable)
            for row in rows:
                self.assertIsInstance(row, dict)
                self.assertIsInstance(row['country_code'], pyarrow.StringScalar)
                self.assertIsInstance(row['country_name'], pyarrow.StringScalar)
            self.assertIsInstance(_arrow, pyarrow.Table)
            self.gcs.write(f"{uri}/{index}.arrow", _arrow)


from google.api_core.exceptions import PermissionDenied


class PublicDatasetTestCase(unittest.TestCase):
    def test_read_session(self):
        bq = BigQueryStream(auth_options).of(table_id="bigquery-public-data.baseball.games_wide")
        self.assertRaisesRegex(PermissionDenied,
                               "403 request failed: the user does not have 'bigquery.readsessions.create' permission for 'projects/bigquery-public-data'",
                               lambda: bq.create_read_session(DataFormat.ARROW)
                               )


class AvroTestCase(unittest.TestCase):

    def test_avro_stream(self):
        bq = BigQueryStream(auth_options).of(table_id='gcp-data-davidkhala.dbt_davidkhala.country_codes')
        session = bq.create_read_session(DataFormat.AVRO)
        for rows, _arrow, _ in bq.read(session):
            self.assertIsInstance(rows, ReadRowsIterable)
            self.assertFalse(_arrow)
            for row in rows:
                self.assertIsInstance(row, dict)
                print(row)
                self.assertIsInstance(row['country_code'], str)
                self.assertIsInstance(row['country_name'], str)


if __name__ == '__main__':
    unittest.main()
