import {GoogleAuth} from 'google-auth-library';


describe('based on Application Default Credentials (ADC)', function () {
    this.timeout(0)
    it('raw http request: use context projectId', async () => {
        const auth = new GoogleAuth({
            scopes: 'https://www.googleapis.com/auth/cloud-platform'
        });

        const client = await auth.getClient();
        const projectId = await auth.getProjectId();
        const url = `https://storage.googleapis.com/storage/v1/b/?project=${projectId}`;
        const res = await client.request({url});
        console.log(res.data);
    })
})
