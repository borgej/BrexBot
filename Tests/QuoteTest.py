import unittest
import logging
from models.Quote import Quote

logging.basicConfig(level=logging.DEBUG)


class QuoteTest(unittest.TestCase):

    def test010_save(self):
        self.assertEqual(Quote(10000, 'brexbottest', 1000, 'Test Quote', 'Test Viewer').exists(), None)
        Quote(10000, 'brexbottest', 1000, 'Test Quote', 'Test Viewer').save()
        self.assertEqual(Quote(10000, 'brexbottest', 1000, 'Test Quote', 'Test Viewer').exists(), True)

    def test020_exists(self):
        quote = Quote(10000, 'brexbottest', 1000, 'Test Quote', 'Test Viewer').load()
        exist_check = quote.exists()
        self.assertEqual(exist_check, True)

    def test030_load(self):
        quote = Quote(10000, 'brexbottest', 1000, 'Test Quote', 'Test Viewer').load()
        self.assertIsNotNone(quote)

    def test040_delete(self):
        quote = Quote(10000, 'brexbottest', 1000, 'Test Quote', 'Test Viewer').load()
        self.assertIsNotNone(quote)
        quote.delete()
        exist_check = quote.exists()
        self.assertEqual(exist_check, None)
