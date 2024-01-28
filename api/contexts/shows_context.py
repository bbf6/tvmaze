from lib.mongodb import Connection
from helpers.time import now

class ShowsContext():

    def __init__(self):
        connection = Connection.get_instance()
        self._collection = connection['shows']

    def by_id(self, id):
        return self._collection.find_one({'id': id})

    def save(self, show):
        show['saved_at'] = now()
        return self._collection.insert_one(show)
