import requests

class TvMazeApi():
    _BASE_URL = 'https://api.tvmaze.com'
    _SEARCH_ENDPOINT = '/search/shows?q='

    def search(self, search_text):
        url = self._search_url(search_text)
        return requests.get(url)

    def _search_url(self, search_text):
        return f'{self._BASE_URL}{self._SEARCH_ENDPOINT}{search_text}'
