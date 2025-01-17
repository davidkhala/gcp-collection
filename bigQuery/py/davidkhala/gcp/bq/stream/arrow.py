from typing import Iterator

from google.cloud.bigquery.client import pyarrow
from google.cloud.bigquery_storage import ReadSession, DataFormat, ReadRowsStream

from davidkhala.gcp.bq.stream import BigQueryStream


class ArrowStream(BigQueryStream):
    def as_arrow(
        self, *, read_options: ReadSession.TableReadOptions = None
    ) -> Iterator[pyarrow.Table]:
        session = self.create_read_session(
            DataFormat.ARROW,
            max_stream_count=None,
            session_options={"read_options": read_options},
        )

        def _map(name: str):
            _: ReadRowsStream = self.client.read_rows(name)
            return _.to_arrow()

        for stream in session.streams:
            yield _map(stream.name)