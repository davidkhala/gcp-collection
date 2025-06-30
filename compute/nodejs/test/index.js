import {Region} from '../region.js'

describe('gcp', function () {
    this.timeout(0)
    const client_email = 'cloud-region@freetier-only.iam.gserviceaccount.com'
    const {PRIVATE_KEY:private_key} = process.env
    it('region: explicit params', async () => {
        const projectId = 'freetier-only'
        const region = new Region({projectId, client_email, private_key})
        const result = await region.list()
        console.debug(result)
    })


})