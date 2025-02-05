from typing import Callable, Any

from davidkhala.gcp.auth import OptionsInterface
from google.cloud.pubsub import SubscriberClient
from google.cloud.pubsub_v1.futures import Future
from google.cloud.pubsub_v1.subscriber.message import Message
from google.pubsub import Subscription

from davidkhala.gcp.pubsub import TopicAware


def show(message: Message, future: Future):
    print(message.data)
    message.ack()
    future.cancel()


class Sub(TopicAware):
    subscription: str

    def __init__(self, subscription: str, topic: str, auth: OptionsInterface):
        super().__init__(topic, auth)
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

    def get(self) -> Subscription:
        return self.client.get_subscription(subscription=self.subscription_path)

    def delete(self):
        self.client.delete_subscription(subscription=self.subscription_path)

    @property
    def subscription_path(self):
        return SubscriberClient.subscription_path(self.project, self.subscription)

    def listen_async(self, callback: Callable[[Message, Future], Any]) -> Future:
        # Cancelling the future will signal the process to shut down gracefully and exit.
        future = self.client.subscribe(self.subscription_path, lambda message: callback(message, future))
        return future

    def listen(self, callback: Callable[[Message, Future], Any] = show):
        """
        Waiting on the future
        This will block forever or until a non-recoverable error is encountered (such as loss of network connectivity, cancelling the future)
        """
        future = self.listen_async(callback)
        future.result()
