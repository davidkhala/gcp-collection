import google.auth
from google.oauth2 import service_account, credentials


class GoogleAuthOptions:
    credentials: service_account.Credentials | credentials.Credentials
    """
    :type credentials: service_account.Credentials | credentials.Credentials
    being as google.oauth2.credentials.Credentials when get from Application Default Credentials (ADC) 
    """
    projectId: str

    @staticmethod
    def default():
        c = GoogleAuthOptions()
        c.credentials, c.projectId = google.auth.default()
        return c

    @staticmethod
    def from_service_account(info=None, *, client_email, private_key, project_id):
        if not info:
            info = {
                'client_email': client_email,
                'private_key': private_key,
            }
        if project_id:
            info['project_id'] = project_id

        info['token_uri'] = "https://oauth2.googleapis.com/token"

        c = GoogleAuthOptions()
        c.credentials = service_account.Credentials.from_service_account_info(info)
        c.projectId = info['project_id']
        return c
