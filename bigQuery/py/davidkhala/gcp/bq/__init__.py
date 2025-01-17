import re
from abc import abstractmethod
from typing import Dict

from davidkhala.gcp.auth import OptionsInterface
from google.cloud.bigquery import Client, DatasetReference


class BigQueryInterface:
    project: str
    dataset: str
    table: str

    def __init__(self, auth: OptionsInterface):
        self.project = auth.projectId
    @staticmethod
    def parse_table_path(path: str) -> Dict[str, str]:
        """Parses a table path into its component segments."""
        m = re.match(
            r"projects/(?P<project>.+?)/datasets/(?P<dataset>.+?)/tables/(?P<table>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @property
    @abstractmethod
    def table_path(self):
        pass

    def of(self, *, table_path=None, table_id=None):
        if table_path:
            data = BigQueryInterface.parse_table_path(table_path)
            self.project = data['project']
            self.dataset = data['dataset']
            self.table = data['table']
        elif table_id:
            self.project, self.dataset, self.table = table_id.split('.')
        return self


class BigQuery(BigQueryInterface):
    client: Client

    def __init__(self, auth: OptionsInterface):
        super().__init__(auth)
        self.client = Client(auth.projectId, auth.credentials)

    @property
    def table_path(self):
        return DatasetReference(self.project, self.dataset).table(self.table).path



