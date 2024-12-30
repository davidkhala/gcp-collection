import {Export, Import} from '../query/build.js'
import {BigQuery} from "../index.js";

describe('sample public data', function () {
    this.timeout(0)
    const publicSetSQL = `SELECT name
              FROM \`bigquery-public-data.usa_names.usa_1910_2013\`
              WHERE state = 'TX'
              LIMIT 100`;

    const privateSetSQL = 'select * from `gcp-data-davidkhala.dbt_davidkhala.country_codes`'
    const bq = new BigQuery({apiKey: process.env.API_KEY})
    it('query', async () => {
        console.debug(await bq.query(publicSetSQL))
        console.debug(await bq.query(privateSetSQL))
    })
    it('export: buggy single-wildcard-uri design in query builder', async () => {
        const path = 'bq-migrate/query-builder/*'
        const exportQuery = new Export(privateSetSQL).to(path)
        console.debug(exportQuery)
        await bq.query(exportQuery)
    })

    it('import', async () => {
        const path =`bq-migrate/query-builder/000000000000`
        const importQuery = new Import(path).to('country_codes2', 'dbt_davidkhala', 'gcp-data-davidkhala')
        console.debug(importQuery)
        await bq.query(importQuery)
    })
})
