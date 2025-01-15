from davidkhala.gcp.auth import OptionsInterface
from google.cloud.bigquery_storage import BigQueryReadClient
from google.cloud.bigquery_storage_v1.types import DataFormat, ReadSession


class BigQuery:
    project: str
    dataset: str
    table: str
    client: BigQueryReadClient

    def __init__(self, auth: OptionsInterface):
        self.client = BigQueryReadClient(credentials=auth.credentials)
        self.project = auth.projectId

    @property
    def table_path(self):
        return BigQueryReadClient.table_path(self.project, self.dataset, self.table)

    def of(self, *, table_path=None, table_id=None):
        if table_path:
            data = BigQueryReadClient.parse_table_path(table_path)
            self.project = data['project']
            self.dataset = data['dataset']
            self.table = data['table']
        elif table_id:
            self.project, self.dataset, self.table = table_id.split('.')

    def create_read_session(self, data_format: DataFormat,
                            *, session_options:dict=None, max_stream_count=1):
        """

        :param data_format:
        :param session_options:
        :param max_stream_count: Each response stream contains one or more table rows, up to a maximum of 10 MiB per response
        :return:
        """
        if session_options is None:
            session_options = {}
        assert data_format != DataFormat.DATA_FORMAT_UNSPECIFIED
        return self.client.create_read_session(
            parent=f"projects/{self.project}",
            read_session=ReadSession({
                "table": self.table_path,
                "data_format": data_format,
                **session_options
            }),
            max_stream_count=max_stream_count,
        )
