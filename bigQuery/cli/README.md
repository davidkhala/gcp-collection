# \$bq CLI

## global options
`--format=FORMAT`

Specifies the format of the command's output. Use one of the following values:

* `pretty`: formatted table output
* `sparse`: simpler table output
* `prettyjson`: easy-to-read JSON format
* `json`: maximally compact JSON
* `csv`: csv format with header
* `none`: the command produces no output

`pretty`, `sparse`, and `prettyjson` are intended to be human-readable.

`json` and `csv` are intended to be used by another program.

If the `--format` flag is absent, then an appropriate output format is chosen based on the command.

## Run query
Pre-requisite
- Replace any single quotes (') in the query with double quotes (").
- Remove comments from the query.

command flag
- `--destination_table` to create a permanent table based on the query results
  - It is required if you plan to run a query that return larger than quota `maximum response size`
  - + `--append_table`: the query results are appended to existing destination table (if any)
  - + `--replace`: overwrite with the query results to existing destination table (if any)
- `--allow_large_results` is required if `--use_legacy_sql=true`
### Running parameterized queries
only available with GoogleSQL syntax
- Query parameters can be used as substitutes for expressions (in where clause), excluding identifiers, column names, table names, etc.


`bq query <query-statement>`


## Create interactive shell
`bq shell`