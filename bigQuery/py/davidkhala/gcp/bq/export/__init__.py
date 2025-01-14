import pyarrow
from google.cloud.bigquery_storage import BigQueryReadClient

from google.cloud.bigquery_storage_v1.types import ReadSession, DataFormat

from davidkhala.gcp.bq import BigQuery


class Export(BigQuery):


    def from_table(self, columns: list[str], where: str)->pyarrow.Table:

        client = self.client

        read_options = ReadSession.TableReadOptions(
            selected_fields=columns,
            row_restriction=where
        )
        read_session = ReadSession(
            table=self.table_path,
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
        return reader.to_arrow()
