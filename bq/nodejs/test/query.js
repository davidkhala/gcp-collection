import {getInstance} from "./bq.js";
const bq = getInstance()
describe('sample public data', function () {
    this.timeout(0)
    const publicSetSQL = `SELECT name
              FROM \`bigquery-public-data.usa_names.usa_1910_2013\`
              WHERE state = 'TX'
              LIMIT 100`;

    it('query', async () => {
        console.debug(await bq.query(publicSetSQL))
    })

})
