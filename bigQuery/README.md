# BigQuery

[History](https://towardsdatascience.com/bigquery-the-unlikely-birth-of-a-cloud-juggernaut-b5ad476525b7)

[Compete with Redshift](https://aws.amazon.com/cn/blogs/big-data/fact-or-fiction-google-big-query-outperforms-amazon-redshift-as-an-enterprise-data-warehouse/)

Both ETL & ELT strategies can be used very effectively with BigQuery as the primary & final destination data store and GCS as the staging (or ingest) or intermediate data store as required.

## Design and limit
https://www.youtube.com/watch?v=Vj6ksosHdhw
- No Join
- No primary key, unique key or index column
- Denormalize tables


# Document Index
- [$bq CLI](./bq.md)
- [SQL Translation](./SQL.md)
- [Data Type](./data-type.md)

## Connect
- querying data directly from GCS and Google Drive.
  - AVRO, JSON NL, CSV files
  - Google Cloud Datastore backup 
- Google Sheets (first tab only)
- If native support is not yet available for the BI layer in use, Google has partnered with [Simba Technologies](https://cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers) to provide ODBC and JDBC drivers







  
