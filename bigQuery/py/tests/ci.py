import os

from davidkhala.gcp.auth.options import from_service_account, default, ADC, _Options


def credential()->_Options:
    private_key = os.environ.get('PRIVATE_KEY')
    r: _Options
    if private_key:
        r = from_service_account(
            client_email=os.environ.get('CLIENT_EMAIL')
                         or 'data-integration@gcp-data-davidkhala.iam.gserviceaccount.com',
            private_key=os.environ.get('PRIVATE_KEY'))
    else:
        print('using ADC')
        r = default()
    _Options.token.fget(r)
    return r
