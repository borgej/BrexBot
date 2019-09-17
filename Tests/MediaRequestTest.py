import unittest
import logging
from MediaRequestHandler import MediaRequestHandler
from models.MediaRequest import MediaRequest
from Db import Db

logging.basicConfig(level=logging.DEBUG)


class MediaRequestTest(unittest.TestCase):
    def test_search_request(self):
        handler = MediaRequestHandler()
        song_request = MediaRequest("Aqua Barbie Girl")

        song_request = handler.search_request(song_request)

        self.assertIsNotNone(song_request)
        self.assertIsNotNone(song_request.video_id)
        self.assertIsNotNone(song_request.url)

    def test_get_video_details(self):
        handler = MediaRequestHandler()
        song_request = MediaRequest("I Built A Giant House Using Only Legos")
        song_request.video_id = "9vB-48kHbBU"

        song_request = handler.get_video_details(song_request)

        self.assertIsNotNone(song_request)
        self.assertIsNotNone(song_request.title)
        self.assertEqual(829, song_request.length)

    # Test requires a database connection
    def test_load(self):
        media = MediaRequest(id=1, channel='brexbottest').load()
        self.assertIsNotNone(media.video_id)

    def test_exist(self):
        media = MediaRequest(id=1, title=None).exists()
        self.assertEqual(media, True)

    def test_delete(self):
        media = MediaRequest(id=1, channel='brexbottest').load()
        self.assertIsNotNone(media.channel)
        media.delete()
        test_exists = MediaRequest(id=1, title=None).exists()
        self.assertIsNone(test_exists)

    def test_save(self):
        MediaRequest(id=1, channel='brexbottest', title=None, video_id='j09hpp3AxIE').save()
        test_exists = MediaRequest(id=1, title=None).exists()
        self.assertEqual(test_exists, True)






