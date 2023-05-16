import {Query} from "../query/query.js";
import {Export} from '../query/build.js'

describe('sample public data', function () {
    this.timeout(0)
    const publicSetSQL = `SELECT name
              FROM \`bigquery-public-data.usa_names.usa_1910_2013\`
              WHERE state = 'TX'
              LIMIT 100`;

    const privateSetSQL = 'select * from `gcp-data-davidkhala.dbt_davidkhala.country_codes`'
    const query = new Query()
    it('query', async () => {
        console.debug(await query.query(publicSetSQL))
        console.debug(await query.query(privateSetSQL))
    })
    it('export: bug design in query builder', async () => {
        const path = 'bq-migrate/query-builder-*'
        const exportQuery = new Export(privateSetSQL).to(path)
        console.debug(exportQuery)
        await query.query(exportQuery)
    })
})
