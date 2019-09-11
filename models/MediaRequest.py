__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class MediaRequest():
    def __init__(self, id, channel, title, video_id, url, requested_by, request_date, duration = None, Deleted = None):
        self.id = id
        self.channel = channel
        self.title = title
        self.video_id = video_id
        self.url = url
        self.requested_by = requested_by
        self.request_date = request_date
        self.duration = duration
        self.Deleted = Deleted
