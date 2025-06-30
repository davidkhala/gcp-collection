// TODO
import assert from "node:assert";
import {execSync} from "@davidkhala/light/devOps.js";
import {cloud_provider} from './const.js'

export class CLI {
    get cmd() {
        return `gcloud alpha cloudlocationfinder cloud-locations`
    }

    /**
     * search best matching cloud regions
     * @param {string} [cloud] target cloud provider
     * @param {string} [source] source cloud region, not limited to gcp. Default: "gcp-asia-east2" (gcp Hongkong)
     * @param {integer} [limit]
     */
    search({cloud, source = "gcp-asia-east2", limit}) {
        const options = ['cloud_location_type=CLOUD_LOCATION_TYPE_REGION']
        if (cloud) {
            const providerEntry = "CLOUD_PROVIDER_" + cloud.toUpperCase()
            assert.ok(cloud_provider.includes(providerEntry));
            options.push(providerEntry)
        }
        let limitOpt = ''
        if (limit > 0 && Number.isInteger(limit)) {
            limitOpt = ` --limit=${limit}`
        }

        const query = options.join(' AND ')

        const cmd = `${this.cmd} search --source-cloud-location=${source} --query="${query}"${limitOpt}`;
        return execSync(cmd)
    }
}


