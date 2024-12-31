import {getInstance} from "./bq.js";

describe('bq', function () {
    this.timeout(0)
    it('connect', async () => {
        const bq = getInstance()
        await bq.connect()
    })
})