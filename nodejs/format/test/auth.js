import pkg from 'google-auth-library/build/src/auth/googleauth.js';
import {OptionsBuilder} from '../auth.js'
import * as assert from "node:assert";
import {RegionsClient} from '@google-cloud/compute'
import GCPClass from '../index.js'
const {GoogleAuthOptions} = pkg;


describe('auth', function (){
    this.timeout(0)
    it('GoogleAuthOptions not exist', ()=>{
        assert.ok(!GoogleAuthOptions)
    })
    it('API key', async ()=>{
        const builder = new OptionsBuilder('freetier-only')
        builder.apiKey = process.env.API_KEY
        const gcp = new GCPClass(builder.build())
        gcp.as(RegionsClient)
        await gcp.connect()
    })
})