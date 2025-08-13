# Table
## External table
- No clustering and partitioning
- Lower Performance
  - Since your file are parsed on the fly (with type casting) -> the processing time is slower
  - You can't control/limit the volume of data that your process.
- possible errors in file that will break your query
- [Compare with native table](https://stackoverflow.com/questions/71261259/bigquery-pricing-comparison-loading-data-into-bigquery-vs-using-create-externa)

## [Object table (preview)](https://cloud.google.com/bigquery/docs/object-table-introduction)
read-only tables over unstructured data objects that reside in Cloud Storage

## Limit
- **No Primary Key, unique key or index column**. 
  - [If we do want anonymized primary keys, we need to generate them on our own](https://nl.devoteam.com/expert-view/creating-anonymized-primary-keys-for-google-bigquery/)
  - Workaround: You can create indexes in BQ table using `CLUSTER BY` while creating table

- Does not support row level or column level security at a table level.
  - Workaround 1: control user access at a dataset level using ACLs and IAM Policies.
  - Workaround 2: implement data control structures joined in for every query at the database level. This approach can be quite flexible, but can also be a very complex and administratively intense undertaking.

## [Partitioned tables](https://cloud.google.com/bigquery/docs/partitioned-tables)
dividing a large table into smaller partitions

Benefits:
  - improve the query performance: by only scanning a portion of a table.
  - When your table operation exceeds a quota, you can scope the table operations to specific partition column values.
  - You want to determine query costs before a query runs. Calculate a query cost estimate by pruning a partitioned table, then you can issue a query dry run to estimate query costs.
  - Control costs by reducing the number of bytes read by a query
- [Pruning](https://cloud.google.com/bigquery/docs/querying-partitioned-tables):  BigQuery can scan the partitions that match the filter and skip the remaining partitions

Types of partitioning
  - Integer range partitioning: based on ranges of values in a `INTEGER` column, such as an auto-incremental index column
  - Time-unit column partitioning: based on a `DATE`,`TIMESTAMP`, or `DATETIME` column in the table
  - Ingestion time partitioning: BQ automatically assigns rows to partitions per ingestion time with hourly, daily, monthly, or yearly granularity

## [Clustered tables](https://cloud.google.com/bigquery/docs/clustered-tables)


