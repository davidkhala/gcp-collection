from google.cloud.bigquery_storage import BigQueryReadClient
from google.cloud.bigquery_storage import types
import os

from common import GCP


class Export(GCP):
    def __init__(self, project_id: str, name: str):
        super().__init__(project_id, name)


    def exec(self, dataset:str, table:str):
        table = f"projects/{self.project_id}/datasets/{dataset}/tables/{table}"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='D:\medium\example-apis\key\key_bqsa.json'
project_id = 'medium-sandbox'

#Setting the client
client = BigQueryReadClient()



requested_session = types.ReadSession()
requested_session.table = table

# This API deliver data serialized in Apache Arrow and AVRO format.
requested_session.data_format = types.DataFormat.ARROW

# Selecting the columns and appying a filter
requested_session.read_options.selected_fields = ["country",
                                                  "year_1960",
                                                  "year_1970",
                                                  "year_1980",
                                                  "year_1990",
                                                  "year_2000",
                                                  "year_2010",
                                                  "year_2018"]
requested_session.read_options.row_restriction = 'country_code = "PER"'

parent = "projects/{}".format(project_id)
session = client.create_read_session(
    parent=parent,
    read_session=requested_session,
    # It's possible to have more than one stream
    max_stream_count=1,
)
reader = client.read_rows(session.streams[0].name)

# The rows() method uses the fastavro library to parse these blocks as an iterable of Python
# dictionaries.
# Run pip install google-cloud-bigquery-storage[fastavro]

df = reader.to_dataframe(session)

# Iterating over the rows
print(df.head())