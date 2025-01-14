from davidkhala.gcp import AuthOptions
from google.cloud.bigquery_storage import BigQueryReadClient


class BigQuery:
    project: str
    dataset: str
    table: str
    client: BigQueryReadClient

    def __init__(self, auth: AuthOptions):
        self.client = BigQueryReadClient(credentials=auth.credentials)
        self.project = auth.projectId

    @property
    def table_path(self):
        return BigQueryReadClient.table_path(self.project, self.dataset, self.table)

    def of(self, *, table_path, table_id):
        if table_path:
            data = BigQueryReadClient.parse_table_path(table_path)
            self.project = data['project']
            self.dataset = data['dataset']
            self.table = data['table']
        elif table_id:
            self.project, self.dataset, self.table = table_id.split('.')
