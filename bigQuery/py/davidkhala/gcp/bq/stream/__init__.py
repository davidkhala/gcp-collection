from davidkhala.gcp.auth.options import AuthOptions
from google.cloud.bigquery_storage import BigQueryReadClient, BigQueryWriteClient, DataFormat, ReadSession

from davidkhala.gcp.bq import BigQueryInterface


class BigQueryStream(BigQueryInterface):
    read: BigQueryReadClient
    write: BigQueryWriteClient

    def __init__(self, auth: AuthOptions):
        super().__init__(auth)
        self.client = BigQueryReadClient(credentials=auth.credentials)

    @property
    def table_path(self):
        r = BigQueryReadClient.table_path(self.project, self.dataset, self.table)
        assert r == BigQueryWriteClient.table_path(self.project, self.dataset, self.table)
        return r

    def create_read_session(self, data_format: DataFormat,
                            *, session_options: dict = None, max_stream_count=1):
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
            parent=BigQueryReadClient.common_project_path(self.project),
            read_session=ReadSession({
                "table": self.table_path,
                "data_format": data_format,
                **session_options
            }),
            max_stream_count=max_stream_count,
        )
