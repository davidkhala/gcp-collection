
# SQL Translation
Currently (26-Feb-2023), following dialects are supported
- Teradata SQL
- AWS Redshift SQL

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
