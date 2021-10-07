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
