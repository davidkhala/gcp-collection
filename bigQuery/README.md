# BigQuery

[History](https://towardsdatascience.com/bigquery-the-unlikely-birth-of-a-cloud-juggernaut-b5ad476525b7)

[Compete with Redshift](https://aws.amazon.com/cn/blogs/big-data/fact-or-fiction-google-big-query-outperforms-amazon-redshift-as-an-enterprise-data-warehouse/)

Index
- [$bq CLI](./bq.md)
- [SQL Translation](./SQL.md)
- [Data Type](./data-type.md)

## Connect
If native support is not yet available for the BI layer in use, Google has partnered with [Simba Technologies](https://cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers) to provide ODBC and JDBC drivers


# Dataset
Datasets are top-level containers that are used to organize and control access to your tables and views. 


## Table
- **No Primary Key, unique key or index column**. BigQuery is designed to store one large denormalized table. It is basically a data lake solution. [Reference](https://nl.devoteam.com/expert-view/creating-anonymized-primary-keys-for-google-bigquery/)
### [partitioned tables](https://cloud.google.com/bigquery/docs/partitioned-tables)
dividing a large table into smaller partitions
- [Pruning](https://cloud.google.com/bigquery/docs/querying-partitioned-tables):  BigQuery can scan the partitions that match the filter and skip the remaining partitions
- Benefits:
  - improve the query performance: by only scanning a portion of a table.
  - When your table operation exceeds a quota, you can scope the table operations to specific partition column values.
  - You want to determine query costs before a query runs. Calculate a query cost estimate by pruning a partitioned table, then you can issue a query dry run to estimate query costs.
  - Control costs by reducing the number of bytes read by a query
- Types of partitioning
  - Integer range partitioning: based on ranges of values in a `INTEGER` column, such as an auto-incremental index column
  - Time-unit column partitioning: based on a `DATE`,`TIMESTAMP`, or `DATETIME` column in the table
  - Ingestion time partitioning: BQ automatically assigns rows to partitions per ingestion time with hourly, daily, monthly, or yearly granularity

## View

### [materialized-views](https://cloud.google.com/bigquery/docs/materialized-views-intro)

  
