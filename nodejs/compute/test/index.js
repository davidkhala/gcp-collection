import {Region} from '../region.js'

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
})