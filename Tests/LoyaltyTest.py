import unittest
import logging
from models.Loyalty import Loyalty

logging.basicConfig(level=logging.DEBUG)


class LoyaltyTest(unittest.TestCase):

    def test010_save(self):
        self.assertEqual(Loyalty(10000, 'brexbottest', 'test', 1, 1, 2).exists(), None)
        Loyalty(10000, 'brexbottest', 'test', 1, 1, 2).save()
        self.assertEqual(Loyalty(10000, 'brexbottest', 'test', 1, 1, 2).exists(), True)

    def test020_exists(self):
        loyalty = Loyalty(10000, 'brexbottest', 'test', 1, 1, 2).load()
        exist_check = loyalty.exists()
        self.assertEqual(exist_check, True)

    def test030_load(self):
        loyalty = Loyalty(10000, 'brexbottest', 'test', 1, 1, 2).load()
        self.assertIsNotNone(loyalty)

    def test040_delete(self):
        loyalty = Loyalty(10000, 'brexbottest', 'test', 1, 1, 2).load()
        self.assertIsNotNone(loyalty)
        loyalty.delete()
        exist_check = loyalty.exists()
        self.assertEqual(exist_check, None)
