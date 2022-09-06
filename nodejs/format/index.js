export default class GCPClass {
    constructor(projectId, client_email, private_key) {

        this.credentials = {
            client_email,
            private_key,
        }

        this.projectId = projectId
    }

    as(ClientClass) {
        if (this.client) {
            this.disconnect();
        }
        this.client = new ClientClass(this);
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
