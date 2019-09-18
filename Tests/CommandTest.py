import unittest
import logging
from models.Command import Command


logging.basicConfig(level=logging.DEBUG)


class CommandTest(unittest.TestCase):

    def test010_save(self):
        self.assertEqual(Command(1, 'brexbottest', 'test', 'test command', 1, 'It is a test command', 1, 1, 1, 1, 1, 1).exists(), None)
        Command(1, 'brexbottest', 'test', 'test command', 1, 'It is a test command', 1, 1, 1, 1, 1, 1).save()
        self.assertEqual(Command(1, 'brexbottest', 'test', 'test command', 1, 'It is a test command', 1, 1, 1, 1, 1, 1).exists(), True)

    def test020_exists(self):
        command = Command(1, 'brexbottest', 'test', 'test command', 1, 'It is a test command', 1, 1, 1, 1, 1, 1).load()
        exist_check = command.exists()
        self.assertEqual(exist_check, True)

    def test030_load(self):
        command = Command(1, 'brexbottest', 'test', 'test command', 1, 'It is a test command', 1, 1, 1, 1, 1, 1).load()
        self.assertIsNotNone(command)

    def test040_delete(self):
        command = Command(1, 'brexbottest', 'test', 'test command', 1, 'It is a test command', 1, 1, 1, 1, 1, 1).load()
        self.assertIsNotNone(command)
        command.delete()
        exist_check = command.exists()
        self.assertEqual(exist_check, None)
