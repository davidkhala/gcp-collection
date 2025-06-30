import {API, QueryBuilder} from '../region/api.js'
import {CLI} from '../region/cli.js'
import {execSync} from '@davidkhala/light/devOps.js'
import assert from "assert";

describe('api', function () {
    this.timeout(0)
    const token = execSync('gcloud auth print-access-token').trim()
    const projectId = execSync('gcloud config get-value project').trim()
    const f = new API(token, projectId)
    it('list: in Hongkong', async () => {
        let query = new QueryBuilder()
            .condition('territory_code', '=', 'HK')
        const results = await f.list(query.build())
        console.log(results)
        assert.equal(results.length, 3)
    })
    it('search: source can be region of other cloud', async () => {
        console.debug(await f.search('aws-ap-east-1'))
    })
    it('search: if source and target are the same, return undefined', async () => {
        let query = new QueryBuilder()
            .condition('territory_code', '=', 'HK')
            .condition('cloud_provider', '=', 'gcp')
        assert.equal(await f.search(undefined, query.build()), undefined)

    })
})
describe('cli', function () {
    this.timeout(0)
    it('cloudlocationfinder', async () => {
        const cmd = new CLI()

        console.debug(cmd.search({cloud: 'aws'}))
        console.debug(cmd.search({cloud: 'gcp', source: 'aws-ap-east-1'}))
    })
})