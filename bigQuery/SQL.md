# Dataform: Manage your SQL code project
With Dataform, data teams collaborate on a single repository to manage their SQL code while following software engineering best practices such as version control, environments, testing, and documentation.


# SQL Translation
Currently (26-Feb-2023), following dialects are supported
- Teradata SQL
- AWS Redshift SQL

## Batch SQL Translation
Limit
- Each individual source and metadata file can be up to 10 MB
- The total size of all input files(including source files and metadata files) uploaded to Cloud Storage can be up to 1 GB
- up to 25 other Migration API requests (create/start workflow) per minute, per project


# Snippets
[Creates a dataset.](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_schema_statement)
```
CREATE SCHEMA [IF NOT EXISTS]
[project_name.]dataset_name
[OPTIONS(schema_option_list)]
```


# Data definition language (DDL)
https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language
unsupported schema modifications include the following:
- Changing a column's name.
- Changing a column's data type.
- Changing a column's mode (aside from relaxing REQUIRED columns to NULLABLE).
- Deleting a column.
