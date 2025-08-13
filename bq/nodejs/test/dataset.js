import {Dataset} from '../dataset.js'
import assert from "assert";
import {getInstance} from "./bq.js";
const bq = getInstance()
describe('syntax', function () {

    it('id convention', async () => {

        assert.throws(() => new Dataset('nodejs-sdk-dev', bq))
        assert.doesNotThrow(() => new Dataset('nodejs_sdk_dev', bq))
    })

});
describe('lifecycle', function () {
    this.timeout(0)

    const dataset = new Dataset('nodejs_sdk_dev', bq)
    it('connect', async () => {
        await dataset.connect()
    })
    it('create', async () => {
        await dataset.create()
    })
    it('delete', async () => {
        await dataset.delete()
    })
})

