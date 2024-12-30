import assert from 'assert'

export class Dataset {
    constructor(id, bigquery) {
        const regExp = /^[a-zA-Z0-9_]*$/
        const msg = 'Dataset IDs must be alphanumeric (plus underscores) and must be at most 1024 characters long.'
        assert.match(id, regExp, msg);
        assert.ok(id.length < 1025, msg)
        this.dataset = bigquery.client.dataset(id);
    }

    get bigquery(){
        return this.dataset.bigQuery
    }
    async connect() {
        const [dataset] = await this.dataset.get()
        this.dataset = dataset
        return dataset
    }

    async create() {
        const opts = {}
        return await this.dataset.create(opts)
    }

    async delete() {
        return await this.dataset.delete()
    }
}

