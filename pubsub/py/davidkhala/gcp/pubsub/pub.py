from davidkhala.gcp.auth import OptionsInterface
from google.cloud.pubsub import PublisherClient
from google.cloud.pubsub_v1.publisher.futures import Future

from davidkhala.gcp.pubsub import TopicAware


class Pub(TopicAware):
    client: PublisherClient

    def __init__(self, auth: OptionsInterface):
        super().__init__(auth)
        self.client = PublisherClient(
            credentials=auth.credentials,
            client_options=auth.client_options,
        )


    def create(self):
        self.client.create_topic(name=self.name)

    def publish_async(self, message: str, **attrs) -> Future:
        """

        :param message: Message body
        :param attrs: Message attributes
        :return:
        """
        return self.client.publish(self.name, message.encode(), **attrs)

    def publish(self, message: str, **attrs) -> str:
        promise = self.publish_async(message, **attrs)
        return promise.result()
