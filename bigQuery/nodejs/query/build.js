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
    constructor(...uris) {
        this.uris = uris
    }

    to(table_name, dataset_name, project_name) {
        const target = [table_name]
        dataset_name && target.unshift(dataset_name)
        project_name && target.unshift(project_name)

        return `LOAD DATA ${this.overwrite ? 'OVERWRITE' : 'INTO'} ${target.join('.')}
FROM FILES(
    format='CSV',
    uris=[${this.uris.map(uri => `gs://${uri}.csv`)}]
)`
    }
}
