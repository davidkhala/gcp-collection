export default class GCPClass {
    /**
     *
     * @param [projectId]
     * @param [client_email]
     * @param [private_key]
     */
    constructor(projectId, client_email, private_key) {

        if (client_email && private_key) {
            this.credentials = {
                client_email,
                private_key,
            }
        }

        this.projectId = projectId
    }

    as(ClientClass) {
        this.client = new ClientClass(this);
        return this
    }

    async connect() {
        if (this.projectId) {
            await this.client.initialize() // assert-like. Will not prompt if no projectId in context
        } else {
            this.projectId = await this.client.getProjectId()
        }

        return this.client;
    }

    async ping() {
        try {
            await this.client.initialize()
            return true
        } catch (e) {
            return false
        }
    }

    async disconnect() {
        await this.client.close()
        delete this.client;
    }
}
