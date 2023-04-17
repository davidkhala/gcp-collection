import {Query} from "../query.js";

describe('query', function () {
    this.timeout(0)
    it('sample:public data', async () => {
        const sql = `SELECT name
              FROM \`bigquery-public-data.usa_names.usa_1910_2013\`
              WHERE state = 'TX'
              LIMIT 100`;
        const query= new Query()
        console.debug(await query.query(sql))
    })
})
