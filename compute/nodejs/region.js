import {RegionsClient} from "@google-cloud/compute"
import GCPClass from '@davidkhala/gcp-format/index.js'
import {mask} from '@davidkhala/gcp-format/client.js'
import assert from "assert";

export class Region extends GCPClass {
    /**
     * @type RegionsClient
     */
    client

    constructor(auth) {
        if (auth) {
            const {projectId, client_email, private_key} = auth
            super({
                projectId, credentials: {
                    client_email, private_key
                }
            },)
        } else {
            super(undefined)
        }

        this.as(RegionsClient)
    }

    async list() {
        assert.ok(this.projectId, 'this.projectId undefined')
        const project = this.projectId

        const raw = await this.client.list({project}, mask(['name']));
        return raw[0].map(({name, zones, quotas}) => name)
    }
}