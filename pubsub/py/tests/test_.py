import unittest

from davidkhala.gcp.auth.ci import credential

from davidkhala.gcp.pubsub.pub import Pub
from davidkhala.gcp.pubsub.sub import Sub, show
from google.cloud.pubsub_v1.subscriber.message import Message
topic_id = 'databricks'
subscription_id = 'spark'
auth = credential()


class TestCase(unittest.TestCase):
    def test_pubsub(self):
        pub = Pub(topic_id, auth)
        print(pub.get())

        sub = Sub(subscription_id, topic_id, auth)
        message = "hello world"
        def callback(_msg:Message):
            show(_msg)
            self.assertEqual(message, _msg.data.decode('utf-8'))
            promise.cancel()

        promise = sub.listen_async(callback)
        pub.publish_async(message)
        promise.result()


if __name__ == '__main__':
    unittest.main()
