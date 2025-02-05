from typing import Callable, Any

from davidkhala.gcp.auth import OptionsInterface
from google.cloud.pubsub import SubscriberClient
from google.cloud.pubsub_v1.futures import Future
from google.cloud.pubsub_v1.subscriber.message import Message

from davidkhala.gcp.pubsub import TopicAware


def show(message: Message):
    print(message.data)
    message.ack()


class Sub(TopicAware):
    def __init__(self, subscription, auth: OptionsInterface):
        super().__init__(auth)
        self.client = SubscriberClient(
            credentials=auth.credentials,
            client_options=auth.client_options,
        )
        self.subscription = subscription

    def disconnect(self):
        self.client.close()

    def create(self, subscription: str):
        self.client.create_subscription(
            name=self.subscription_path,
            topic=self.name,
        )

    @property
    def subscription_path(self):
        return SubscriberClient.subscription_path(self.project, self.subscription)

    def listen_async(self, callback: Callable[[Message], Any] = show) -> Future:
        # Cancelling the future will signal the process to shutdown gracefully and exit.
        return self.client.subscribe(self.subscription, callback)

    def listen(self, callback: Callable[[Message], Any]):
        """
        Waiting on the future
        This will block forever or until a non-recoverable error is encountered (such as loss of network connectivity)
        """
        promise = self.listen_async(callback)
        promise.result()
        # TODO: how to cancel in callback?

