from lib.tvmaze_api import TvMazeApi
from serializers.shows_serializer import search_format

class ShowsController():

    def __init__(self):
        self._tvmaze_api = TvMazeApi()

    def search(self, search_text):
        response = self._tvmaze_api.search(search_text)
        return search_format(response.json())

    def by_id(self, id):
        response = self._tvmaze_api.show_by_id(id)
        return response.json()
