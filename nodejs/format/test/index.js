import {GoogleAuth} from 'google-auth-library';
import {RegionsClient} from '@google-cloud/compute'
import GCPClass from '../index.js'

describe('', function () {
    this.timeout(0)
    it('auth', async () => {
        const auth = new GoogleAuth({
            scopes: 'https://www.googleapis.com/auth/cloud-platform'
        });

        const client = await auth.getClient();
        const projectId = await auth.getProjectId();
        const url = `https://storage.googleapis.com/storage/v1/b/?project=${projectId}`;
        const res = await client.request({url});
        console.log(res.data);
    })
    it('GCPClass: with explicit project id', async () => {
        const gcp = new GCPClass('gcp-api-davidkhala')
        gcp.as(RegionsClient)
        await gcp.connect()

    })
    it('GCPClass: use context projectId, need `gcloud init`', async () => {
        const gcp = new GCPClass()
        gcp.as(RegionsClient)
        await gcp.connect()
    })
})