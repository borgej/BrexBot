import unittest
import logging
from MediaRequestHandler import MediaRequestHandler
from models.MediaRequest import MediaRequest
from Db import Db

logging.basicConfig(level=logging.DEBUG)


class MediaRequestTest(unittest.TestCase):
    def test010_search_request(self):
        handler = MediaRequestHandler()
        song_request = MediaRequest("Aqua Barbie Girl")

        song_request = handler.search_request(song_request)

        self.assertIsNotNone(song_request)
        self.assertIsNotNone(song_request.video_id)
        self.assertIsNotNone(song_request.url)

    def test020_get_video_details(self):
        handler = MediaRequestHandler()
        song_request = MediaRequest("I Built A Giant House Using Only Legos")
        song_request.video_id = "9vB-48kHbBU"

        song_request = handler.get_video_details(song_request)

        self.assertIsNotNone(song_request)
        self.assertIsNotNone(song_request.title)
        self.assertEqual(829, song_request.length)

    def test030_save(self):
        self.assertEqual(MediaRequest(id=10000, channel='brexbottest', title='test', video_id='j09hpp3AxIE').exists(), None)
        MediaRequest(id=10000, channel='brexbottest', title='test', video_id='j09hpp3AxIE').save()
        self.assertEqual(MediaRequest(id=10000, channel='brexbottest', title='test', video_id='j09hpp3AxIE').exists(), True)

    def test040_exists(self):
        media = MediaRequest(id=10000, channel='brexbottest', title='test', video_id='j09hpp3AxIE').load()
        exist_check = media.exists()
        self.assertEqual(exist_check, True)

    def test050_load(self):
        media = MediaRequest(id=10000, channel='brexbottest', title='test', video_id='j09hpp3AxIE').load()
        self.assertIsNotNone(media)

    def test060_delete(self):
        media = MediaRequest(id=10000, channel='brexbottest', title='test', video_id='j09hpp3AxIE').load()
        self.assertIsNotNone(media)
        media.delete()
        exist_check = media.exists()
        self.assertEqual(exist_check, None)






