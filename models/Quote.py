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

    def filter_values(self):
        values_list = self.__dict__
        for i in list(values_list):
            if i.startswith('_'):
                del values_list[i]
        return values_list

    def exists(self):
        db_data = Db().load_all('quote')
        request_data = list(self.filter_values().values())
        for i in db_data:
            if i[0] == request_data[0] and i[2] == request_data[2]:
                return True
            else:
                continue
        return None

    def load(self):
        data = Db().load_by_id('quote', self.id, self.channel)
        current_status = self.filter_values()
        for key, value in enumerate(current_status):
            current_status[value] = data[key]
        return self

    def save(self):
        filtered = str(self.filter_values().values()).replace("None", "'None'")[13:-2]
        Db().save('quote', filtered)
        return self

    def delete(self):
        request_id = list(self.__dict__.values())
        Db().delete('quote', request_id[0])



