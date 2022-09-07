import {Region} from '../region.js'
import {RegionsClient} from '@google-cloud/compute'

describe('gcp', function () {
    this.timeout(0)

    it('connect', async () => {
        const projectId = 'freetier-only'
        const clientEmail = 'cloud-region@freetier-only.iam.gserviceaccount.com'
        const {private_key} = process.env

        const gcp = new Region(projectId, clientEmail, private_key)
        const result = await gcp.list()
        console.debug(result)

    })
    it('connect default', async () => {
        const client = new Region();

        const result = await client.list();
        console.debug(result)
    })
    it('raw connect', async () => {
        const client = new RegionsClient()
        const _project = await client.getProjectId()
        console.info(_project)
        const asyncResults = await client.list()
        // console.info(asyncResults)


    })
})