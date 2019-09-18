import unittest
import logging
from models.GiveAway import GiveAway
from datetime import datetime


logging.basicConfig(level=logging.DEBUG)


class GiveAwayTest(unittest.TestCase):

    def test010_save(self):
        self.assertEqual(GiveAway(10000, 'brexbottest', 'test', 'trigger', 10, 1, 1, 1, 1).exists(), None)
        GiveAway(10000, 'brexbottest', 'test', 'trigger', 10, 1, 1, 1, 1).save()
        self.assertEqual(GiveAway(10000, 'brexbottest', 'test', 'trigger', 10, 1, 1, 1, 1).exists(), True)

    def test020_exists(self):
        give_away = GiveAway(10000, 'brexbottest', 'test', 'trigger', 10, 1, 1, 1, 1).load()
        exist_check = give_away.exists()
        self.assertEqual(exist_check, True)

    def test030_load(self):
        give_away = GiveAway(10000, 'brexbottest', 'test', 'trigger', 10, 1, 1, 1, 1).load()
        self.assertIsNotNone(give_away)

    def test040_delete(self):
        give_away = GiveAway(10000, 'brexbottest', 'test', 'trigger', 10, 1, 1, 1, 1).load()
        self.assertIsNotNone(give_away)
        give_away.delete()
        exist_check = give_away.exists()
        self.assertEqual(exist_check, None)
