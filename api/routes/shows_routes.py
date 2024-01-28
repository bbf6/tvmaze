from fastapi import APIRouter
from .responses.shows_responses import search_response, ShowById
from controllers.shows_controller import ShowsController

shows = APIRouter(prefix='/shows')
_controller = ShowsController()

@shows.get('/search', response_model=search_response, tags=['shows'])
def search(search: str):
    return _controller.search(search)

@shows.get('/{id}', response_model=ShowById, tags=['shows'])
def show_by_id(id: int):
    return _controller.by_id(id)
