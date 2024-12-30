import {BigQuery as BQ} from '@google-cloud/bigquery';
import GCPClass from '@davidkhala/gcp-format/index.js'

export class BigQuery extends GCPClass {
    /**
     * @type {BQ}
     */
    client
    constructor(auth) {
        super(auth);
        this.client = new BQ(this.auth)
    }

    async query(sql) {

        const [rows] = await this.client.query(sql)
        return rows
    }
}