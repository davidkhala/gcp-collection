import {Dataset} from '../dataset.js'
import assert from "assert";

describe('connect', function () {
    this.timeout(0)
    it('id convention', async () => {

        assert.throws(() => new Dataset('nodejs-sdk-dev'))
        assert.doesNotThrow(() => new Dataset('nodejs_sdk_dev'))
    })

});
describe('lifecycle', function () {

    const dataset = new Dataset('nodejs_sdk_dev')
    it('delete', async () => {
        await dataset.delete()
    })
})

