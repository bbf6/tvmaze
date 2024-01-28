from lib.mongodb import Connection

class CommentsContext():

    def __init__(self):
        connection = Connection.get_instance()
        self._collection = connection['comments']

    def save(self, comment):
        return self._collection.insert_one(comment.dict())
