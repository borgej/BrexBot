__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

from Db import Db
import Config


class MediaRequest:
    def __init__(self, title=None, id=None, channel=Config.CHANNEL_NAME, video_id=None, url=None, requested_by=None, created=None, length=None, thumbnail_url=None, deleted=None):
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

    def filter_values(self):
        values_list = self.__dict__
        for i in list(values_list):
            if i.startswith('_'):
                del values_list[i]
        return values_list

    def exists(self):
        db_data = Db().load_all('media_request')
        request_data = list(self.filter_values().values())
        for i in db_data:
            if i[0] == request_data[0] and i[2] == request_data[2]:
                return True
            else:
                continue
        return None

    def load(self):
        data = Db().load_by_id('media_request', self.id, self.channel)
        current_status = self.filter_values()
        for key, value in enumerate(current_status):
            current_status[value] = data[key]
        return self

    def save(self):
        filtered = str(self.filter_values().values()).replace("None", "'None'")[13:-2]
        Db().save('media_request', filtered)
        return self

    def delete(self):
        request_id = list(self.__dict__.values())
        Db().delete('media_request', request_id[0])



