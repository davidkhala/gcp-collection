from typing import Iterator, Mapping

import pandas
import pyarrow
from davidkhala.gcp.auth import OptionsInterface
from google.cloud.bigquery_storage import (BigQueryReadClient, BigQueryWriteClient, DataFormat, ReadRowsStream,
                                           ReadRowsResponse,
                                           ReadSession as BigQueryReadSession)
from google.cloud.bigquery_storage_v1.reader import ReadRowsIterable

from davidkhala.gcp.bq import BigQueryInterface


class ReadSession:
    session: BigQueryReadSession
    client: BigQueryReadClient

    @property
    def rows(self) -> Iterator[Iterator[ReadRowsResponse] | ReadRowsStream]:
        return (self.client.read_rows(stream.name) for stream in self.session.streams)

    @property
    def count(self): return len(self.session.streams)

    @property
    def arvo(self) -> Iterator[Iterator[Mapping | dict] | ReadRowsIterable]:
        assert self.session.data_format == DataFormat.AVRO
        return (row.rows() for row in self.rows)

    @property
    def data_frame(self) -> Iterator[pandas.DataFrame]:
        return (row.to_dataframe() for row in self.rows)

    @property
    def arrow(self) -> Iterator[pyarrow.Table]:
        assert self.session.data_format == DataFormat.ARROW
        return (row.to_arrow() for row in self.rows)


class Stream(BigQueryInterface):
    read_client: BigQueryReadClient
    write_client: BigQueryWriteClient

    def __init__(self, auth: OptionsInterface):
        super().__init__(auth)
        self.read_client = BigQueryReadClient(credentials=auth.credentials, client_options=auth.client_options)
        self.write_client = BigQueryWriteClient(credentials=auth.credentials, client_options=auth.client_options)

    @property
    def table_path(self):
        r = BigQueryReadClient.table_path(self.project, self.dataset, self.table)
        assert r == BigQueryWriteClient.table_path(self.project, self.dataset, self.table)
        return r

    def create_read_session(self, data_format: DataFormat,
                            *, session_options: dict = None) -> ReadSession:
        """

        :param data_format:
        :param session_options:
        :return:
        """
        if session_options is None:
            session_options = {}
        assert data_format != DataFormat.DATA_FORMAT_UNSPECIFIED
        _ = ReadSession()
        _.session = self.read_client.create_read_session(
            parent=BigQueryReadClient.common_project_path(self.project),
            read_session=BigQueryReadSession({
                "table": self.table_path,
                "data_format": data_format,
                **session_options
            }),
        )
        _.client = self.read_client
        return _
