import unittest
import logging
from MediaRequestHandler import MediaRequestHandler
from models.MediaRequest import MediaRequest

logging.basicConfig(level=logging.DEBUG)

class MediaRequestTest(unittest.TestCase):
    def test_search_request(self):
        handler = MediaRequestHandler()
        song_request = MediaRequest("Aqua Barbie Girl")

        song_request = handler.search_request(song_request)

        self.assertIsNotNone(song_request.url)

    def test_get_video_details(self):
        handler = MediaRequestHandler()
        song_request = MediaRequest("Aqua Barbie Girl")

        song_request = handler.search_request(song_request)
        song_request = handler.get_video_details(song_request)

        self.assertIsNotNone(song_request.title)
        self.assertIsNotNone(song_request.length)

