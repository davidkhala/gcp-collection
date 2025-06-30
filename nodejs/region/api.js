import {axiosPromise} from '@davidkhala/axios/index.js'
import assert from 'assert'
import {cloud_provider, cloud_location_type} from './const.js'

export class API {
    /**
     *
     * @param accessToken got by `gcloud auth print-access-token`
     * @param projectId
     */
    constructor(accessToken, projectId) {
        this.options = {
            auth: {
                bearer: accessToken
            },
        }
        this.baseUrl = `https://cloudlocationfinder.googleapis.com/v1alpha/projects/${projectId}/locations/global/cloudLocations`;
        this.projectId = projectId
    }

    /**
     *
     * @param {string} filter can also be built by SearchQueryBuilder
     */
    async list(filter) {
        const params = {
            filter
        }
        const {cloudLocations} = await axiosPromise({url: this.baseUrl, method: 'GET',params}, this.options)
        return cloudLocations
    }

    async search(source = "gcp-asia-east2", query = '') {
        const url = `${this.baseUrl}:search`;

        const sourceCloudLocation = `projects/${this.projectId}/locations/global/cloudLocations/${source}`
        const params = {
            sourceCloudLocation, query
        }

        const {cloudLocations} = await axiosPromise({url, method: 'GET', params}, this.options)
        // source will be excluded automatically from the result list
        return cloudLocations
    }

}

export class QueryBuilder {
    constructor() {
        this._ = []
        this.condition('cloud_location_type', '=', 'REGION')
    }

    condition(field, operator, value) {
        switch (field) {
            case 'carbon_free_energy_percentage':
                assert.ok(['>', '<'].includes(operator))
                assert.ok(Number.isInteger(value))
                break;
            case 'cloud_location_type':
                assert.ok(['=', '!='].includes(operator))
                value = 'CLOUD_LOCATION_TYPE_' + value.toUpperCase()
                assert.ok(cloud_location_type.includes(value))
                break;
            case 'cloud_provider':
                assert.ok(['=', '!='].includes(operator))
                value = 'CLOUD_PROVIDER_' + value.toUpperCase()
                assert.ok(cloud_provider.includes(value))
                break;
            case 'display_name':
                assert.ok(['=', '!='].includes(operator))
                assert.ok(typeof value === 'string')
                value = `"${value}"`
                break;
            case 'latency':
                assert.ok(['>', '<'].includes(operator))
                assert.ok(value > 0 && Number.isInteger(value))
                break;
            case 'territory_code':
                assert.ok(['=', '!='].includes(operator))
                assert.ok(typeof value === 'string')
                value = `"${value}"`
                break;
            default:
                assert.fail('Unknown field: ' + field);
        }
        const entry = `${field}${operator}${value}`
        const foundIndex = this._.indexOf(entry)
        foundIndex < 0 ? this._.push(entry) : this._[foundIndex] = entry

        return this
    }

    build(separator = ' AND ') {
        // By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly.
        return this._.join(separator)
    }
}

