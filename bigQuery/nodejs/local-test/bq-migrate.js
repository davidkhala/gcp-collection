import {Export, Import} from "../query/build.js";

describe('', function (){
    this.timeout(0);
    const privateSetSQL = 'select * from `gcp-data-davidkhala.dbt_davidkhala.country_codes`'
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