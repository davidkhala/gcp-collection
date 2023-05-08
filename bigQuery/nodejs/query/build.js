export class Export {

    constructor(selectStatement) {
        this.sql = selectStatement
    }

    /**
     *
     * @param path can be a Single wildcard URI. See in https://cloud.google.com/bigquery/docs/exporting-data#exporting_data_into_one_or_more_files
     * @returns {string}
     */
    to(path) {
        return `EXPORT DATA
OPTIONS (
    uri='gs://${path}.csv',
    format='CSV',
    header=${(!!this.header)},
    overwrite=${(!!this.overwrite)}
) AS
${this.sql}`

    }
}

export class Load {
    // TODO
    to(path) {
        return `LOAD DATA {OVERWRITE|INTO} [[project_name.]dataset_name.]table_name
[(
  column[, ...]
)]
[PARTITION BY partition_expression]
[CLUSTER BY clustering_column_list]
[OPTIONS (table_option_list)]
FROM FILES(load_option_list)
[WITH PARTITION COLUMNS
  [(partition_column_list)]
]
[WITH CONNECTION connection_name]

column_list: column[, ...]

partition_column_list: partition_column_name, partition_column_type[, ...]`
    }
}
