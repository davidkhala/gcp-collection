import {API, QueryBuilder} from '../region/api.js'
import {CLI} from '../region/cli.js'
import assert from "assert";
import {OptionsBuilder, printAccessToken} from "../auth.js";
import {GoogleAuth} from "google-auth-library";

describe('api', function () {
    this.timeout(0)

    const projectId = 'freetier-only'

    const builder = new OptionsBuilder(projectId)
    builder.credentials = {
        client_email: process.env.CLIENT_EMAIL || "cloud-region@freetier-only.iam.gserviceaccount.com",
        private_key: process.env.PRIVATE_KEY || "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQCxUa/ZtplSe0zQ\nyrzZ5u3sLAsyvLg++rSYuYVGvVHKYjtaImldcYJNN0UvDVOyv0yMuqjZOCBipWgO\nRkLzce3TuwWbNSk4wwHRgIexYHekj5pAoIIHdynWxsifrOWT1TQ3PUkuyCf0RYbS\nzwG/23jsTDDKELgrAZGGpLImgm2UE+YCK/t1MUJ9D+/Zw+Z+Zi0RcQsKy0Y6zNp+\nZYF2b4BzLFGhtR9bzEQvGlD/7K2NqPj8eHtWyC6KGdGG34sUOqMChH9oat5Zttmv\nDtpmGRUwIm1HAV8/7T4UANxrKqrDHmG4lbztj4IGx9MsDplBHwif0U3Ht9F23bgI\nUp+4i/VxAgMBAAECggEAEO5hmeqBV9qdolclcrIF+FXZSOIzvpG+QlH+m5tSrr4z\n+B6OjIVc4YYcRUqiug/hnZNqMXmWQA0Wszw6wteXU68JMUGBeuHF7+zzp/hz3CL5\nIeAholhaxp8LA5IlBrlmJ7sinISwqfakkccB3gG1GW0KAJVZnIOlE2Pw/dPY5jla\nIapTy/4AWEVbw53optYIdu7fGCOTCM9hvUeX5tbsawDOJorLjix1g/VWmfZdD4Wf\njZPBqQyYheAEoKNtKvJbfC5OpfCTqitmkzafip7pK3ewIFqzw6B76iPxUeTvFKKy\nMKZSRGgwCz5EJaqYAcYedj5SQxgmbIYuRqrN4qtZZQKBgQDzaQdiq2O9uNEo9oYJ\nVpuLtBxvUw+LNOoo8kFSXF7q7Wha+16aWDN0vM2xfpZEtINd6DGak4VWM16ddh99\n8TQ6cGAT8xDceco60bOL+h3B9kAuTnUyiukkJmsuMVFxFngvyZqKLDwhnQD5bisG\ndwzZ2YFptLZKqg5oQx0bd5cxfQKBgQC6fY0kW4+Bv6UUTzmOs672nvIJSFSZ9nn0\nHEWEg00BuwUtQnht7Ar1va49iSHXF9pxMKz6UYsWgGqHuo1aKffmEZfnRTurOAJv\nhym2wDyAjF93JddUkefcqU1/brQCVOCUaJApnOM50XA6yqHwBuh/KsDSG7klp2I+\n1HRm+VhWBQJ/Z6NQgbJ3xU/rvoU4jMFTeSg28y9qbtsY2FZNecPapixvQk3E+fKT\n9iBtdCVx1c8GH/W9KROmsg0tO94PipAorLksL1JO25D/igu/ZtoX0X4H1a+SNvLu\nUXYKLKDTDFOE2NP9+Nbcw3MV9x3xM898qUTy1Q8cjq3ZdIse2ZMRzQKBgHV2ZTM0\nVJSV4GWFbSx78sU14h+Epnz/aVsff43yoctoP999EZuy5Ehae+gYeu8fACDxVtKo\nD+JRakgpcaUL8C/CfxpVWjsDIU2cJeMM/E6/m9XRSOrkp9Ut8jlEwi8BxR7VKZB8\nWAbv6y+suAkWYNTQWfk9KwYTgucuLE872K79AoGBAIuZBlhRaDNe0hxLa1YNPelW\nYDQ36S2rO11pzvqHJc5T9T94QV1avaB2VeayYoV7Ciuk7uLvu3x27VzD+KkJ3Itd\n+1iA0GNJJGPyGxVRHqrjRp25fqkH8ZnezwHSUyjVSvDwFRLEBhuC5XOwQOj1C7WE\n1p0JQieXXpHsL36aQWn/\n-----END PRIVATE KEY-----\n"
    }
    const auth = new GoogleAuth(builder.build())
    let f
    before(async function () {
        const token = await printAccessToken(auth)
        f = new API(token, projectId)
    })


    it('list: in Hongkong', async () => {
        const query = new QueryBuilder().condition('territory_code', '=', 'HK')
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

if (!process.env.CI) {
    describe('cli', function () {
        this.timeout(0)

        it('cloudlocationfinder', async () => {
            const cmd = new CLI()

            console.debug(cmd.search({cloud: 'aws'}))
            console.debug(cmd.search({cloud: 'gcp', source: 'aws-ap-east-1'}))
        })
    })
}
