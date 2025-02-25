import datetime
import unittest
import uuid

from davidkhala.gcp.auth.ci import credential
from google.api_core.exceptions import InvalidArgument
from google.cloud.pubsub_v1.futures import Future
from google.cloud.pubsub_v1.subscriber.message import Message

from davidkhala.gcp.pubsub.pub import Pub
from davidkhala.gcp.pubsub.sub import Sub

topic_id = 'databricks'
id = 'spark'
auth = credential()
pub = Pub(topic_id, auth)


class MessageTestCase(unittest.TestCase):
    sub = Sub(id, topic_id, auth)
    def setUp(self):
        self.sub.create()
    def test_pubsub(self):
        print(pub.get())

        message = "hello world"

        def callback(_msg: Message, _future: Future):
            self.assertEqual(message, _msg.data.decode('utf-8'))
            _msg.ack()
            _future.cancel()

        future = self.sub.listen_async(callback)
        pub.publish_async(message)
        future.result()

    def test_purge(self):
        pub.publish(f"{datetime.datetime.now()}")

        print(self.sub.messages)
        self.sub.purge()
        self.assertEqual(0, len(self.sub.messages))
        self.sub.purge()


class AdminTestCase(unittest.TestCase):
    def sub_lifecycle(self, id):
        print(id)
        sub = Sub(id, topic_id, auth)
        print('start create', datetime.datetime.now())
        sub.create()
        sub.create()
        print('start delete', datetime.datetime.now())
        sub.delete()
        print('end delete', datetime.datetime.now())
        sub.delete()

    def test_sub_lifecycle(self):
        self.sub_lifecycle(f"sub{uuid.uuid4().hex}")
        self.assertRaises(InvalidArgument, lambda: self.sub_lifecycle("Databricks Shell"))


if __name__ == '__main__':
    unittest.main()
