import assert from "assert";

export class Export {

    constructor(selectStatement) {
        this.sql = selectStatement
    }

    /**
     *
     * @param uri
     * @returns {string}
     */
    to(uri) {
        assert.ok(uri.includes('*'), 'The uri option must be a single-wildcard URI.\nSee in https://cloud.google.com/bigquery/docs/reference/standard-sql/other-statements#export_option_list')
        return `EXPORT DATA
OPTIONS (
    uri='gs://${uri}.csv',
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
