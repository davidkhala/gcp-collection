/**
 * Initialize the client.
 * Performs asynchronous operations (such as authentication) and prepares the client.
 * This function will be called automatically when any class method is called for the
 * first time, but if you need to initialize it before calling an actual method,
 * feel free to call initialize() directly.
 *
 * You can await on this method if you want to make sure the client is initialized.
 */
export const connect = async (anyClient) => {
	await anyClient.initialize()
}
export const disconnect = async (anyClient) => {
	/**
	 * Terminate the gRPC channel and close the client.
	 *
	 * The client will no longer be usable and all future behavior is undefined.
	 */
	await anyClient.close()
}