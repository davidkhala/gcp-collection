export default class GCPClass {
    /**
     * @type {GCPClient}
     */
    client
    /**
     * @type {GoogleAuthOptions}
     */
    auth

    /**
     *
     * @param {GoogleAuthOptions} auth
     */
    constructor(auth) {
        this.auth = auth;
    }

    as(ClientClass) {
        this.client = new ClientClass(this.auth);
    }

    get projectId(){
        return this.auth.projectId;
    }
    set projectId(projectId) {
        this.auth.projectId = projectId;
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
