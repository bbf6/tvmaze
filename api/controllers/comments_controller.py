from services.comments_service import CommentsService

class CommentsController():

    def __init__(self):
        self._service = CommentsService()

    def create(self, comment):
        self._service.create(comment)
