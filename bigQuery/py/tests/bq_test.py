import unittest

from google.cloud.bigquery_storage import BigQueryReadClient, DataFormat

from davidkhala.gcp.bq import BigQuery
from davidkhala.gcp.bq.stream import BigQueryStream
from tests.ci import credential

table_id = 'gcp-data-davidkhala.dbt_davidkhala.country_codes'


class SyntaxTestCase(unittest.TestCase):
    def test_credential(self):
        credential()

    def test_build_path(self):
        bq = BigQuery(credential()).of(table_id=table_id)
        self.assertEqual("/" + BigQueryReadClient.table_path(bq.project, bq.dataset, bq.table),
                         bq.table_path)


class CoreTestCase(unittest.TestCase):
    bq = BigQuery(credential()).of(table_id=table_id)

    def test_query(self):
        rows = self.bq.query(f"select * from {table_id}")

        for row in rows:
            print(row)


class StreamTestCase(unittest.TestCase):
    def test_read_stream(self):
        bq = BigQueryStream(credential()).of(table_id=table_id)
        session = bq.create_read_session(DataFormat.ARROW)
        print(session.name)


if __name__ == '__main__':
    unittest.main()
