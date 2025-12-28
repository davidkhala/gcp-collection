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

        message = f"{datetime.datetime.now()}"

        def callback(_msg: Message, _future: Future):
            if message == _msg.data.decode('utf-8'):
                _msg.ack()
                _future.cancel()

        future = self.sub.listen_async(callback)
        pub.publish_async(message)
        future.result(timeout=5)

    def test_purge(self):
        message = f"purge-{datetime.datetime.now()}"
        pub.publish(message)

        print(self.sub.messages)
        self.sub.purge()
        remaining = [m.message.data for m in self.sub.messages]
        if len(remaining) > 0:
            self.assertNotIn(message, remaining)
        self.sub.purge()  # purge on empty should be allowed


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
        sub.delete()  # delete on empty should be allowed

    def test_sub_lifecycle(self):
        self.sub_lifecycle(f"sub{uuid.uuid4().hex}")
        self.assertRaises(InvalidArgument, lambda: self.sub_lifecycle("Databricks Shell"))


if __name__ == '__main__':
    unittest.main()
