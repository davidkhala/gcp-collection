import assert from 'assert'

export class Dataset {
    constructor(id, bigquery) {
        const regExp = /^[a-zA-Z0-9_]*$/
        const msg = 'Dataset IDs must be alphanumeric (plus underscores) and must be at most 1024 characters long.'
        assert.match(id, regExp, msg);
        assert.ok(id.length < 1025, msg)
        this.dataset = bigquery.client.dataset(id);
    }

    get bigquery() {
        return this.dataset.bigQuery
    }

    async connect() {
        await this.exist()
    }

    async exist() {
        const [exist] = await this.dataset.exists()
        return exist
    }

    async get() {
        if (!await this.exist()) {
            return
        }
        const [dataset] = await this.dataset.get()
        this.dataset = dataset
        return dataset
    }

    async ensure() {
        const [dataset] = await this.dataset.get({autoCreate: true})
        this.dataset = dataset
    }

    async create() {
        if (await this.exist()) {
            return
        }
        const [dataset] = await this.dataset.create({})
        this.dataset = dataset
    }

    async delete() {
        if (await this.exist()) {
            return await this.dataset.delete()
        }

    }
}

