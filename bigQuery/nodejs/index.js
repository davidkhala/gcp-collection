import {BigQuery as BQ} from '@google-cloud/bigquery';
import GCPClass from '@davidkhala/gcp-format/index.js'

export class BigQuery extends GCPClass {
    /**
     * @type {BQ}
     */
    client
    constructor(auth) {
        if(auth.apiKey){
            throw Error("BigQuery does not support access via API keys for authentication")
        }
        super(auth);
        this.client = new BQ(this.auth)
    }
    async connect(){
        await this.client.getDatasets()
    }

    async query(sql) {

        const [rows] = await this.client.query(sql)
        return rows
    }
}