import {RegionsClient} from "@google-cloud/compute"
import GCPClass from '@davidkhala/gcp-format/index.js'
import {mask} from '@davidkhala/gcp-format/client.js'
import assert from "assert";

export class Region extends GCPClass {
    constructor(projectId, client_email, private_key) {
        super(projectId, client_email, private_key)
        this.as(RegionsClient)
    }

    async list() {
        assert.ok(this.projectId, 'this.projectId undefined')

        const raw = await this.client.list({
            project: this.projectId,
        }, mask(['name']));
        return raw[0].map(({name, zones, quotas}) => name)
    }
}