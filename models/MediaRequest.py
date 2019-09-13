__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class MediaRequest():
    def __init__(self, title, id = None, channel = None, video_id = None, url = None, requested_by = None, created = None, length = None, thumbnail_url = None, deleted = None):
        self.id = id
        self.channel_id = channel
        self.title = title
        self.video_id = video_id
        self.url = url
        self.requested_by = requested_by
        self.created = created
        self.length = length
        self.thumbnail_url = thumbnail_url
        self.deleted = deleted
