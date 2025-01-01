export class GoogleAuthOptions {
    /**
     * An API key to use, optional. Cannot be used with {@link GoogleAuthOptions.credentials `credentials`}.
     */
    apiKey
    /**
     * An `AuthClient` to use
     */
    authClient
    /**
     * Path to a .json, .pem, or .p12 key file
     */
    keyFilename
    /**
     * Path to a .json, .pem, or .p12 key file
     */
    keyFile
    /**
     * Object containing client_email and private_key properties, or the
     * external account client options.
     * Cannot be used with {@link GoogleAuthOptions.apiKey `apiKey`}.
     */
    credentials
    /**
     * Options object passed to the constructor of the client
     */
    clientOptions
    /**
     * Required scopes for the desired API request
     */
    scopes
    /**
     * Your project ID.
     */
    projectId
    /**
     * The default service domain for a given Cloud universe.
     *
     * This is an ergonomic equivalent to {@link clientOptions}'s `universeDomain`
     * property and will be set for all generated {@link AuthClient}s.
     */
    universeDomain
}

export class OptionsBuilder {
    constructor(projectId) {
        this._ = {}
        if (projectId) {
            this.projectId = projectId
        }
    }

    set apiKey(apiKey) {
        this._.apiKey = apiKey
        delete this._.credentials
    }

    set credentials({client_email, private_key}) {
        this._.credentials = {
            client_email, private_key,
        }
        delete this._.apiKey
    }

    set projectId(projectId) {
        this._.projectId = projectId
    }

    set scope(scope) {
        this._.scopes = scope
    }

    keyFile(serviceAccountJSONFile, globally) {
        this._.keyFilename = serviceAccountJSONFile
        delete this._.apiKey
        delete this._.credentials
        if (globally) {
            process.env.GOOGLE_APPLICATION_CREDENTIALS = serviceAccountJSONFile
        }
    }

    /**
     *
     * @return {GoogleAuthOptions}
     */
    build() {
        return this._
    }
}

