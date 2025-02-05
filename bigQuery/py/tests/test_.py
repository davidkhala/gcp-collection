import unittest

from google.cloud.bigquery import DestinationFormat, DatasetReference
from google.cloud.bigquery_storage import BigQueryReadClient

from davidkhala.gcp.bq import BigQuery
from davidkhala.gcp.auth.ci import credential

table_id = 'gcp-data-davidkhala.dbt_davidkhala.country_codes'


class SyntaxTestCase(unittest.TestCase):
    def test_credential(self):
        credential()

    def test_build_path(self):
        bq = BigQuery(credential()).of(table_id=table_id)
        self.assertEqual("/" + BigQueryReadClient.table_path(bq.project, bq.dataset, bq.table),
                         bq.table_path)
        self.assertNotEqual(DatasetReference(bq.project, bq.dataset).table(bq.table).table_id, bq.table_id)


class CoreTestCase(unittest.TestCase):
    bq = BigQuery(credential()).of(table_id=table_id)

    def test_query(self):
        rows = self.bq.query(f"select * from {table_id}")

        for row in rows:
            print(row)

    def test_export(self):
        bucket = 'davidkhala-data'
        self.bq.export(bucket=bucket)
        self.bq.export(DestinationFormat.AVRO, bucket=bucket)
        self.bq.export(DestinationFormat.PARQUET, bucket=bucket)


if __name__ == '__main__':
    unittest.main()
