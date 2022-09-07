import {Region} from '../region.js'
import {RegionsClient} from '@google-cloud/compute'

describe('gcp', function () {
    this.timeout(0)
    const projectId = 'freetier-only'
    it('connect', async () => {

        const clientEmail = 'cloud-region@freetier-only.iam.gserviceaccount.com'
        const {private_key} = process.env

        const gcp = new Region(projectId, clientEmail, private_key)
        const result = await gcp.list()
        console.debug(result)

    })
    it('connect default', async () => {
        const client = new Region(projectId);

        const result = await client.list();
        console.debug(result)
    })
})