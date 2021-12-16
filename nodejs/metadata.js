import gcpMetadata from 'gcp-metadata';

export async function isAvailable() {
	const isAvailable = await gcpMetadata.isAvailable();
	if (!isAvailable) {
		console.log(`
		Instance and Project level metadata will only be available if running inside of a Google Cloud compute environment 
		such as Cloud Functions, App Engine, Kubernetes Engine, or Compute Engine.`)

	}
	return isAvailable
}

