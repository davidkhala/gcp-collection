# Export data
https://cloud.google.com/bigquery/docs/exporting-data#export_limitations
- The only supported export location is Google Cloud Storage
- You can export up to 1 GB of table data to a single file
https://cloud.google.com/bigquery/docs/exporting-data#export_formats_and_compression_types
- format support
  - CSV:  raw, GZIP
  - JSON: raw, GZIP
  - Avro: DEFLATE, SNAPPY	
  - Parquet:  SNAPPY, GZIP
- Move to Autonomous DB: https://qiita.com/RexZheng/items/d3e5cfed0bd579b4c4d2
## Method
https://cloud.google.com/bigquery/docs/exporting-data#exporting_data_stored_in
- Cloud Console
- command line `bq extract`
  > `bq extract <project_id>:<dataset>.<table> gs://<bucket>/<filename.ext>`
- API or client lib
- SQL Statment [EXPORT DATA](https://cloud.google.com/bigquery/docs/reference/standard-sql/other-statements#export_data_statement)
  > EXPORT DATA OPTIONS(
  uri='gs://bucket/folder/*.csv',
  format='CSV',
  overwrite=true,
  header=true,
  field_delimiter=';') AS
SELECT field1, field2 FROM mydataset.table1 ORDER BY field1 LIMIT 10
