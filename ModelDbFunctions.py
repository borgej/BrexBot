
from Db import Db


class ModelDbFunctions:
    def __init__(self, model_type, model):
        self.model_type = model_type
        self.model = model

    def filter_values(self):
        values_list = self.model.__dict__
        for i in list(values_list):
            if i.startswith('_'):
                del values_list[i]
        return values_list

    def exists(self):
        media_check = Db().load_all(self.model_type)
        request_data = list(self.model.filter_values().values())
        for i in media_check:
            if i[0] == request_data[0] and i[2] == request_data[2]:
                return True
            else:
                continue
        return None

    def load(self):
        data = Db().load_by_id(self.model_type, self.model.id, self.model.channel)
        current_status = self.filter_values()
        for key, value in enumerate(current_status):
            current_status[value] = data[key]
        return self

    def save(self):
        filtered = str(self.filter_values().values()).replace("None", "'None'")[13:-2]
        Db().save(self.model_type, filtered)
        return self

    def delete(self):
        request_id = list(self.model.__dict__.values())
        Db().delete(self.model_type, request_id[0])
