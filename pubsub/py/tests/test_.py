import datetime
import unittest

from davidkhala.gcp.auth.ci import credential
from google.cloud.pubsub_v1.futures import Future
from google.cloud.pubsub_v1.subscriber.message import Message

from davidkhala.gcp.pubsub.pub import Pub
from davidkhala.gcp.pubsub.sub import Sub

topic_id = 'databricks'
subscription_id = 'spark'
auth = credential()


class TestCase(unittest.TestCase):
    pub = Pub(topic_id, auth)
    sub = Sub(subscription_id, topic_id, auth)

    def test_pubsub(self):
        print(self.pub.get())

        sub = Sub(subscription_id, topic_id, auth)
        message = "hello world"

        def callback(_msg: Message, _future: Future):
            self.assertEqual(message, _msg.data.decode('utf-8'))
            _msg.ack()
            _future.cancel()

        future = sub.listen_async(callback)
        self.pub.publish_async(message)
        future.result()

    def test_purge(self):
        self.pub.publish(f"{datetime.datetime.now()}")

        print(self.sub.messages)
        self.sub.purge()
        self.assertEqual(0, len(self.sub.messages))
        self.sub.purge()


if __name__ == '__main__':
    unittest.main()
