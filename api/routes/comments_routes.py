from fastapi import APIRouter
from .params.comments_params import CreateComment
from controllers.comments_controller import CommentsController

comments = APIRouter(prefix='/comments')
_controller = CommentsController()

@comments.post('/', tags=['comments'])
def create(comment: CreateComment):
    return _controller.create(comment)
