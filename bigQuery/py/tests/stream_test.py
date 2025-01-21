import unittest

import pyarrow
from google.cloud.bigquery_storage import DataFormat, ReadSession
from google.cloud.bigquery_storage_v1.reader import ReadRowsIterable

from davidkhala.gcp.bq.stream import BigQueryStream
from ci import credential
from davidkhala.data.format.arrow.gcp import GCS
table_id = 'gcp-data-davidkhala.dbt_davidkhala.country_codes'


class StreamTestCase(unittest.TestCase):
    bq = BigQueryStream(credential()).of(table_id=table_id)

    def test_arrow_stream(self):
        session = self.bq.create_read_session(DataFormat.ARROW)
        self.assertIsInstance(session, ReadSession)
        self.assertTrue(session.name.startswith('projects/gcp-data-davidkhala/locations/us/sessions/'))
        for rows, _arrow, _ in self.bq.read(session):
            self.assertIsInstance(rows, ReadRowsIterable)
            for row in rows:
                self.assertIsInstance(row, dict)
                print(row)
                self.assertIsInstance(row['country_code'], pyarrow.StringScalar)
                self.assertIsInstance(row['country_name'], pyarrow.StringScalar)
            self.assertIsInstance(_arrow, pyarrow.Table)
            GCS(False).write()
            _arrow.to_batches()

    def test_avro_stream(self):
        session = self.bq.create_read_session(DataFormat.AVRO)
        for rows, _arrow, _ in self.bq.read(session):
            self.assertIsInstance(rows, ReadRowsIterable)
            self.assertFalse(_arrow)
            for row in rows:
                self.assertIsInstance(row, dict)
                print(row)
                self.assertIsInstance(row['country_code'], str)
                self.assertIsInstance(row['country_name'], str)


if __name__ == '__main__':
    unittest.main()
