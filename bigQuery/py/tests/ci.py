import os

from davidkhala.gcp.auth.options import from_service_account, default


def credential():
    private_key = os.environ.get('PRIVATE_KEY')
    if private_key:
        return from_service_account(
            client_email=os.environ.get('CLIENT_EMAIL')
                         or 'data-integration@gcp-data-davidkhala.iam.gserviceaccount.com',
            private_key=os.environ.get('PRIVATE_KEY'))
    else:
        print('using ADC')
        return default()
