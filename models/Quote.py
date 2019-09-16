__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

from Db import Db


class Quote:
    def __init__(self, id, channel, nr, quote, viewer, created):
        self.id = id
        self.channel = channel
        self.nr = nr
        self.quote = quote
        self.viewer = viewer
        self.created = created

    def exists(self):
        media_check = Db().load_all('quote')
        request_data = list(self.__dict__.values())

        for i in media_check:
            if i[0] == request_data[0] and i[2] == request_data[2]:
                return True
            else:
                continue
        return None

    def load(self):
        loyalty_data = Db().load_all('quote', self.channel)
        current_status = self.__dict__
        for key, value in enumerate(current_status):
            current_status[value] = loyalty_data[key]
        return self

    def save(self):
        object_values = str(self.__dict__.values()).replace("None", "'None'")[13:-2]
        Db().save('quote', object_values)
        return self

    def delete(self):
        request_id = str(self.__dict__.values())[13:14]
        Db().delete('quote', request_id)


