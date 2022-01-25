/**
 * @typedef {Object} CredentialBody
 * @property {string} client_email
 * @property {string} private_key
 */
/**
 * @typedef GoogleAuthOptions
 * @property {CredentialBody} credentials
 * @property {string} [projectId]
 */

/**
 *
 * @param client_email
 * @param private_key
 * @param projectId
 * @return {GoogleAuthOptions}
 */
export const getOption = (client_email, private_key, projectId) => ({
	credentials: {
		client_email,
		private_key,
	},
	projectId,
})
export const fromFile = (serviceAccountJSONFile) => {
	process.env.GOOGLE_APPLICATION_CREDENTIALS = serviceAccountJSONFile
}

