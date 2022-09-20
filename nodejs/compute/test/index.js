import {Region} from '../region.js'

describe('gcp', function () {
    this.timeout(0)

    it('connect: explicit params', async () => {
        const projectId = 'freetier-only'
        const clientEmail = 'cloud-region@freetier-only.iam.gserviceaccount.com'
        const {private_key} = process.env

        const gcp = new Region(projectId, clientEmail, private_key)
        const result = await gcp.list()
        console.debug(result)

    })
    it('connect: get by connect', async () => {
        const client = new Region();

        await client.connect()
        const result = await client.list();
        console.debug(result)
    })
})