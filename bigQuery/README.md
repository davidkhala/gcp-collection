# BigQuery

[History](https://towardsdatascience.com/bigquery-the-unlikely-birth-of-a-cloud-juggernaut-b5ad476525b7)

[Compete with Redshift](https://aws.amazon.com/cn/blogs/big-data/fact-or-fiction-google-big-query-outperforms-amazon-redshift-as-an-enterprise-data-warehouse/)

Both ETL & ELT strategies can be used very effectively with BigQuery as the primary & final destination data store and GCS as the staging (or ingest) or intermediate data store as required.

Denormalize Design: BigQuery is designed to store one large denormalized table.
- less Join
- No primary key, unique key or index column

# Document Index
- [$bq CLI](./cli/README.md)
- [SQL Translation](./SQL.md)
- [Data Type](./data-type.md)

## Connect
- querying data directly from GCS and Google Drive.
  - AVRO, JSON NL, CSV files
  - Google Cloud Datastore backup 
- Google Sheets (first tab only)
- If native support is not yet available for the BI layer in use, Google has partnered with [Simba Technologies](https://cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers) to provide ODBC and JDBC drivers. This extends connection support including
  - MS Excel (preferred than [bigquery-connector-for-excel](https://cloud.google.com/bigquery/docs/bigquery-connector-for-excel))







  
