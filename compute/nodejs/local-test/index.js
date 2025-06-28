import {RegionsClient} from "@google-cloud/compute";
import assert from "assert";
import {Region} from "../region.js";

describe('gcp: use context credential', function () {
    this.timeout(0)

    if (process.env.CI) {
        return
    }
    it('raw RegionsClient', async () => {

        const region = new RegionsClient();
        assert.ok(await region.getProjectId(), 'default projectId should not be empty')
    })
    it('region: connect', async () => {
        const region = new Region()
        try {
            await region.connect()
            console.info('connected')
        } catch (e) {
            assert.equal(e.message, 'Could not load the default credentials. Browse to https://cloud.google.com/docs/authentication/getting-started for more information.')
        }

    })
})