import {BigQuery} from '@google-cloud/bigquery';
import assert from 'assert'

const bigquery = new BigQuery();

export class Dataset {
    constructor(id) {
        const regExp = /^[a-zA-Z0-9_]*$/
        const msg = 'Dataset IDs must be alphanumeric (plus underscores) and must be at most 1024 characters long.'
        assert.match(id, regExp, msg);
        assert.ok(id.length < 1025, msg)
        this.dataset = bigquery.dataset(id);
    }

    async connect() {
        const [dataset] = await this.dataset.get()
        this.dataset = dataset
        return dataset
    }
    async delete(){
        return await this.dataset.delete()
    }
}

