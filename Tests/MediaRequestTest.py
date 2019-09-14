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
        self.assertIsNotNone(song_request.length)

    #Test requires a database connection
    def test_load(self):
        channel = 'brexbottest'
        _id = 19
        media_data = Db().load_('media_request',_id, channel)
        self.id = media_data[0]
        self.channel = media_data[1]
        self.title = media_data[2]
        self.video_id = media_data[3]
        self.url = media_data[4]
        self.requested_by = media_data[5]
        self.created = media_data[6]
        self.length = media_data[7]
        self.thumbnail_url = media_data[8]
        self.deleted = media_data[9]

        self.assertNotEqual(self.url, None)
        self.assertEqual(self.channel, channel)
        self.assertEqual(self.video_id, _id)

    #Test requires database connection
    def test_save(self):
        song_requset = MediaRequest('Barbie Girl')
        request = MediaRequestHandler().search_request(song_requset)
        media_check = Db().load_all('media_request')
        request_data = list(request.__dict__.values())
        for i in media_check:
            if i[1] == request_data[1] and i[3] == request_data[3]:
                print("This request already exists")
            else:
                continue





