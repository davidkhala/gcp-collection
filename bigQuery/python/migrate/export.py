from google.cloud.bigquery_storage import BigQueryReadClient

from google.cloud.bigquery_storage_v1.types import ReadSession, DataFormat

from common import GCP


class Export(GCP):
    def __init__(self, dataset: str, project_id: str):
        super().__init__(project_id)
        self._arrow = None
        self.dataset = dataset

    def from_table(self, table: str, columns: list[str], where: str):
        table = f"projects/{self.project_id}/datasets/{self.dataset}/tables/{table}"
        client = BigQueryReadClient()

        read_options = ReadSession.TableReadOptions(
            selected_fields=columns,
            row_restriction=where
        )
        read_session = ReadSession(
            table=table,
            data_format=DataFormat.ARROW,
            read_options=read_options,
        )
        parent = f"projects/{self.project_id}"
        session = client.create_read_session(
            parent=parent,
            read_session=read_session,
            # It's possible to have more than one stream
            max_stream_count=1,
        )
        # Each response contains one or more table rows, up to a maximum of 10 MiB per response
        reader = client.read_rows(session.streams[0].name)
        self._arrow = reader.to_arrow()

    def print(self):
        print(self._arrow)
    def to_json(self):
        return self._arrow.to_pydict()
