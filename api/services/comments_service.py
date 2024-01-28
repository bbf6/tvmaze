from contexts.comments_context import CommentsContext

class CommentsService():

    def __init__(self):
        self._context = CommentsContext()

    def create(self, comment):
        self._context.save(comment)
