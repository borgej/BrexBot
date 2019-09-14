__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

from Db import Db

class MediaRequest():
    def __init__(self, title=None, id = None, channel = None, video_id = None, url = None, requested_by = None, created = None, length = None, thumbnail_url = None, deleted = None):
        self.id = id
        self.channel = channel
        self.title = title
        self.video_id = video_id
        self.url = url
        self.requested_by = requested_by
        self.created = created
        self.length = length
        self.thumbnail_url = thumbnail_url
        self.deleted = deleted

    def load(self, _id, channel):
        media_data = Db().load_media(_id, channel)
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
        return self

    def save(self, media_request):
        # Create one variable to hold the keys of media_request dictionary
        # and one to hold the values.
        object_keys = str(media_request.__dict__.keys()).replace("'", "")
        object_values = str(media_request.__dict__.values()).replace("None", "'None'")

        # Trim both of the above variables to make them suitable to pass
        # into the SQL function
        trim_keys = object_keys[11:-2]
        trim_values = object_values[13:-2]
        Db().save_media(trim_keys, trim_values)

    def delete(self, media_request):
        request_id = str(media_request.__dict__.values())[13:14]
        Db().delete_media(request_id)
