from google.cloud.client import ClientWithProject

from davidkhala.gcp.auth import OptionsInterface


class Client(ClientWithProject):
    @staticmethod
    def from_options(options: OptionsInterface):
        return Client(
            options.projectId, options.credentials, options.client_options
        )
