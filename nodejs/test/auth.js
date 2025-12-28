import {OptionsBuilder, printAccessToken} from '../auth.js'
import {RegionsClient} from '@google-cloud/compute'
import GCPClass from '../index.js'
import { GoogleAuth } from 'google-auth-library';

describe('auth', function (){
    this.timeout(0)
    it('get token', async ()=>{
        const builder = new OptionsBuilder('gcp-data-davidkhala')
        builder.credentials = {
            client_email:process.env.CLIENT_EMAIL,
            private_key:process.env.PRIVATE_KEY
        }
        const auth = new GoogleAuth(builder.build())
        printAccessToken(auth)
    })
    it('API key', async ()=>{
        const builder = new OptionsBuilder('gcp-data-davidkhala')
        builder.apiKey = process.env.API_KEY
        const gcp = new GCPClass(builder.build())
        gcp.as(RegionsClient)
        await gcp.connect()
    })
})