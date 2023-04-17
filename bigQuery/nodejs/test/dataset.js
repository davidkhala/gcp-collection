import {Dataset} from '../dataset.js'
import {Query} from '../query.js'
import assert from "assert";

describe('syntax', function () {

    it('id convention', async () => {

        assert.throws(() => new Dataset('nodejs-sdk-dev'))
        assert.doesNotThrow(() => new Dataset('nodejs_sdk_dev'))
    })

});
describe('lifecycle', function () {
    this.timeout(0)
    const dataset = new Dataset('nodejs_sdk_dev')
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

