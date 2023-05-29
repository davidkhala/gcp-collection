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
## Exploring your data
Don't run queries to explore or preview table data.
- Helpful solutions
  - In the Google Cloud console, on the table details page, click the `Preview` tab to sample the data.
  - In the `bq` command-line tool, use the `bq head` command and specify the number of rows to preview.
  - In the API, use `tabledata.list` to retrieve table data from a specified set of rows.

## Cost preview
Before running queries, preview them to estimate costs.
- Helpful solutions
  - The query validator in the Google Cloud console provides an estimate of the number of bytes required to process the query.
    - For example: `This query will process 623.1 KiB when run.`
  - Perform a dry run by using the:
    - `--dry_run` flag in the `bq` command-line tool
    - `dryRun` parameter when submitting a query job using the API
