from lib.tvmaze_api import TvMazeApi
from contexts.shows_context import ShowsContext

class ShowsService():

    def __init__(self):
        self._tvmaze_api = TvMazeApi()
        self._context = ShowsContext()

    def search(self, search_text):
        response = self._tvmaze_api.search(search_text)
        return response.json()

    def show_by_id(self, id):
        show = self._context.by_id(id)
        if (show):
            return show
        response = self._tvmaze_api.show_by_id(id)
        show = response.json()
        self._context.save(show)
        return show
