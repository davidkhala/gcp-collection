import unittest

from google.cloud.bigquery_storage_v1 import BigQueryReadClient
from google.cloud.bigquery_storage_v1.types import DataFormat

from davidkhala.gcp.bq import BigQuery
from tests.ci import credential


class SyntaxTestCase(unittest.TestCase):
    def test_parse_path(self):
        _parseFunc = BigQueryReadClient.parse_table_path
        project = 'bigquery-public-data'
        dataset = 'baseball'
        table = 'schedules'
        table_id = f'{project}.{dataset}.{table}'
        print(table_id)
        not_right = _parseFunc(table_id)
        self.assertFalse(not_right)
        _parseFunc(BigQueryReadClient.table_path(project, dataset, table))

    def test_credential(self):
        credential()

    def test_BigQuery(self):
        bq = BigQuery(credential())

        table_id = 'gcp-data-davidkhala.dbt_davidkhala.country_codes'
        bq.of(table_id=table_id)
        session = bq.create_read_session(DataFormat.ARROW)
        print(session.name)


if __name__ == '__main__':
    unittest.main()
