from typing import Iterator, Tuple

import pyarrow
import pandas
from davidkhala.gcp.auth import OptionsInterface
from google.cloud.bigquery_storage import (BigQueryReadClient, BigQueryWriteClient, DataFormat, ReadRowsStream,
                                           ReadSession as BigQueryReadSession)
from google.cloud.bigquery_storage_v1.reader import ReadRowsIterable

from davidkhala.gcp.bq import BigQueryInterface


class ReadSession:
    session: BigQueryReadSession

    def read(self, session: BigQueryReadSession) -> Iterator[Tuple[ReadRowsIterable, pyarrow.Table, pandas.DataFrame]]:
        for stream in session.streams:
            reader: ReadRowsStream = self.client.read_rows(stream.name)
            yield (
                reader.rows(session),
                session.data_format == DataFormat.ARROW and reader.to_arrow(session),
                reader.to_dataframe(session)
            )
    # TODO
    # def extract_tables(iterator: Iterator[Tuple[ReadRowsIterable, pa.Table, pd.DataFrame]]) -> Iterator[pa.Table]:
    #     return (item[1] for item in iterator)

class Stream(BigQueryInterface):
    read_client: BigQueryReadClient
    write_client: BigQueryWriteClient

    def __init__(self, auth: OptionsInterface):
        super().__init__(auth)
        self.client = BigQueryReadClient(credentials=auth.credentials)

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
        _.session = self.client.create_read_session(
            parent=BigQueryReadClient.common_project_path(self.project),
            read_session=BigQueryReadSession({
                "table": self.table_path,
                "data_format": data_format,
                **session_options
            }),
        )
        return _
