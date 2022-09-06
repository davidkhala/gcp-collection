import {RegionsClient} from "@google-cloud/compute"
import GCPClass from '@davidkhala/gcp-format/index.js'
export class Region extends GCPClass{
    constructor(projectId, client_email, private_key) {
        super(projectId, client_email, private_key)
        this.as(RegionsClient)
    }

    async list() {

        const [res] = await this.client.list({project: this.projectId});
        return res.map(({name}) => name)
    }
}