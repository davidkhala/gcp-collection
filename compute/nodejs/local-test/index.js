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
    it('region: connect', async()=>{
        const region = new Region()
        await region.connect()
        // FIXME cannot catch error
        // Error: Could not load the default credentials. Browse to https://cloud.google.com/docs/authentication/getting-started for more information.
        //     at GoogleAuth.getApplicationDefaultAsync (node_modules\google-auth-library\build\src\auth\googleauth.js:284:15)
        //     at processTicksAndRejections (node:internal/process/task_queues:105:5)
        //     at runNextTicks (node:internal/process/task_queues:69:3)
        //     at listOnTimeout (node:internal/timers:549:9)
        //     at process.processTimers (node:internal/timers:523:7)
        //     at async #determineClient (node_modules\google-auth-library\build\src\auth\googleauth.js:732:36)
        //     at async GoogleAuth.getClient (node_modules\google-auth-library\build\src\auth\googleauth.js:709:20)
        //     at async GrpcClient.createStub (node_modules\google-gax\build\src\fallback.js:259:35)
        await region.list()

    })
})