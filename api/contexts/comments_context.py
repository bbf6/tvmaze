from lib.mongodb import Connection

class CommentsContext():

    def __init__(self):
        connection = Connection.get_instance()
        self._collection = connection['comments']

    def by_ids(self, ids):
        query = {'show_id': {'$in': ids}}
        return self._collection.find(query)

    def save(self, comment):
        return self._collection.insert_one(comment.dict())
