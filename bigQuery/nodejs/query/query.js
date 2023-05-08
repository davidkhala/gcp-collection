import {BigQuery} from '@google-cloud/bigquery';

export class Query {
    constructor(bigquery = new BigQuery()) {
        this.bigquery = bigquery
    }

    async query(sql) {

        const [rows] = await this.bigquery.query(sql)
        return rows
    }
}
