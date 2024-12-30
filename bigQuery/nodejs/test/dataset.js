import {Dataset} from '../dataset.js'
import assert from "assert";
import {BigQuery} from "../index.js";

describe('syntax', function () {

    it('id convention', async () => {

        assert.throws(() => new Dataset('nodejs-sdk-dev'))
        assert.doesNotThrow(() => new Dataset('nodejs_sdk_dev'))
    })

});
describe('lifecycle', function () {
    this.timeout(0)
    const bq = new BigQuery({apiKey: process.env.API_KEY})
    const dataset = new Dataset('nodejs_sdk_dev', bq)
    it('connect', async () => {
        console.debug(await dataset.connect())
    })
    it('create', async () => {
        console.debug(await dataset.create())
    })
    it('delete', async () => {
        await dataset.delete()
    })
})

