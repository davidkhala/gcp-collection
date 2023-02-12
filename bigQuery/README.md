# BigQuery

[History](https://towardsdatascience.com/bigquery-the-unlikely-birth-of-a-cloud-juggernaut-b5ad476525b7)

[Compete with Redshift](https://aws.amazon.com/cn/blogs/big-data/fact-or-fiction-google-big-query-outperforms-amazon-redshift-as-an-enterprise-data-warehouse/)





## Table
- **No Primary Key**. BigQuery is designed to store one large denormalized table. It is basically a data lake solution. [Reference](https://nl.devoteam.com/expert-view/creating-anonymized-primary-keys-for-google-bigquery/)
### [partitioned tables](https://cloud.google.com/bigquery/docs/partitioned-tables)
dividing a large table into smaller partitions
- [Pruning](https://cloud.google.com/bigquery/docs/querying-partitioned-tables):  BigQuery can scan the partitions that match the filter and skip the remaining partitions
- Benefits:
  - improve the query performance: by only scanning a portion of a table.
  - When your table operation exceeds a quota, you can scope the table operations to specific partition column values.
  - You want to determine query costs before a query runs. Calculate a query cost estimate by pruning a partitioned table, then you can issue a query dry run to estimate query costs.
  - Control costs by reducing the number of bytes read by a query



  
