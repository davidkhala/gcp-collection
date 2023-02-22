## Enum
- STRING
- BYTES
- INTEGER
- FLOAT
- NUMERIC
- BIGNUMERIC
- BOOLEAN
- TIMESTAMP
- DATE
- TIME
- DATETIME
- GEOGRAPHY
- RECORD

## Mapping to Standard SQL data types
- `STRUCT`: A `RECORD` can be accessed as a `STRUCT` type in standard SQL
- `ARRAY`: To create a column with repeated data, set the *mode* of the column to `REPEATED` in the schema.

## Use case
- [When the data is denormalized](https://medium.com/@knoldus/bigquery-efficient-data-warehouse-schema-design-b7f53d72444a), BQ facilitate efficient data warehouse schema design which is using the nested (`RECORD`) & repeated (`REPEATED` mode) columns.

[Document](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types)
