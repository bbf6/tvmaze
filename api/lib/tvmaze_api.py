import requests

class TvMazeApi():
    _BASE_URL = 'https://api.tvmaze.com'
    _SEARCH_ENDPOINT = '/search/shows?q='
    _SHOW_BY_ID = '/shows/'

    def search(self, search_text):
        url = self._search_url(search_text)
        return requests.get(url)

    def show_by_id(self, id):
        url = self._show_by_id_url(id)
        return requests.get(url)

    def _search_url(self, search_text):
        return f'{self._BASE_URL}{self._SEARCH_ENDPOINT}{search_text}'

    def _show_by_id_url(self, id):
        return f'{self._BASE_URL}{self._SHOW_BY_ID}{id}'
