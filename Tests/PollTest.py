import unittest
import logging
from models.Poll import Poll

logging.basicConfig(level=logging.DEBUG)


class PollTest(unittest.TestCase):

    def test010_save(self):
        self.assertEqual(Poll(10000, 'brexbottest', 'test', 'www.testpoll.com').exists(), None)
        Poll(10000, 'brexbottest', 'test', 'www.testpoll.com').save()
        self.assertEqual(Poll(10000, 'brexbottest', 'test', 'www.testpoll.com').exists(), True)

    def test020_exists(self):
        poll = Poll(id=10000, channel='brexbottest').load()
        exist_check = poll.exists()
        self.assertEqual(exist_check, True)

    def test030_load(self):
        poll = Poll(id=10000, channel='brexbottest').load()
        self.assertIsNotNone(poll.url)

    def test040_delete(self):
        poll = Poll(id=10000, channel='brexbottest').load()
        self.assertIsNotNone(poll.url)
        poll.delete()
        exist_check = poll.exists()
        self.assertEqual(exist_check, None)

