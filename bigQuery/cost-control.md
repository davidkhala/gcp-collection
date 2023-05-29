# Cost Control
https://cloud.google.com/bigquery/docs/best-practices-costs

## Avoid SELECT *
BigQuery does a full scan of every column in the table.

- Helpless solutions include
  - Apply a `LIMIT` clause
- Helpful solutions
  - use `SELECT * EXCEPT` to exclude one or more columns from the results.
  - Materializing results in a destination table and querying that table instead.
  - [Partitioning your tables](https://cloud.google.com/bigquery/docs/creating-partitioned-tables) and querying the relevant partition. 
    - For example, use `WHERE _PARTITIONDATE="2017-01-01"` to query only the January 1, 2017 partition.
