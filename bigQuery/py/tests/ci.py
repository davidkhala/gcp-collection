import os

from davidkhala.gcp.auth import OptionsInterface
from davidkhala.gcp.auth.options import from_service_account, default, _Options, from_api_key


def credential() -> OptionsInterface:
    private_key = os.environ.get('PRIVATE_KEY')
    api_key = os.environ.get('API_KEY')
    r = OptionsInterface()
    if api_key:
        r.client_options = from_api_key(api_key, {})
    else:
        if private_key:
            r = from_service_account(
                client_email=os.environ.get('CLIENT_EMAIL')
                             or 'data-integration@gcp-data-davidkhala.iam.gserviceaccount.com',
                private_key=os.environ.get('PRIVATE_KEY'))
        else:
            print('using ADC')
            r = default()
        r.client_options = None
        _Options.token.fget(r)
    return r
