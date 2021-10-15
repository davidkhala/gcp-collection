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

[Document](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types)
