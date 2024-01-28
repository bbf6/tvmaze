from fastapi import APIRouter
from .responses.shows_responses import search_response
from controllers.shows_controller import ShowsController

shows = APIRouter(prefix='/shows')
controller = ShowsController()

@shows.get('/search', response_model=search_response, tags=['shows'])
def search(search: str):
    return controller.search(search)
