import {axiosPromise} from '@davidkhala/axios/index.js'

export class LocationFinder {
    constructor(accessToken, projectId) {
        this.accessToken = accessToken;
        this.baseUrl = 'https://cloudlocationfinder.googleapis.com/v1alpha';
        this.projectId = projectId
    }

    async search(filters = '') {
        const {projectId} = this;
        const url = `${this.baseUrl}/projects/${projectId}/locations/global/cloudLocations:search`;
        const params = filters ? {filter: filters} : {};

        return await axiosPromise({
            url, method: 'GET',params
        }, {
            auth: {
                bearer: this.accessToken
            }
        })
    }
}


