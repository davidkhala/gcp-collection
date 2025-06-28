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
     * @param {GoogleAuthOptions} [auth] if not specified, context credential will be used as default
     */
    constructor(auth) {
        this.auth = auth;
    }

    as(ClientClass) {
        this.client = new ClientClass(this.auth);
    }

    get projectId() {
        if (!this.auth) {
            return
        }
        return this.auth.projectId;
    }

    set projectId(projectId) {
        if (!this.auth) {
            this.auth = {}
        }
        this.auth.projectId = projectId;
    }

    async connect() {
        if (!this.projectId) {
            this.projectId = await this.client.getProjectId()
        }

        await this.client.initialize() // assert-like. Will not throw if no projectId in context


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
