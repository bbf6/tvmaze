from lib.tvmaze_api import TvMazeApi
from services.shows_service import ShowsService
from serializers.shows_serializer import search_format

class ShowsController():

    def __init__(self):
        self._tvmaze_api = TvMazeApi()
        self._service = ShowsService()

    def search(self, search_text):
        response = self._service.search(search_text)
        return search_format(response)

    def by_id(self, id):
        return self._service.show_by_id(id)
