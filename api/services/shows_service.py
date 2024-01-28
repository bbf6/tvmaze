from lib.tvmaze_api import TvMazeApi
from contexts.shows_context import ShowsContext
from contexts.comments_context import CommentsContext

class ShowsService():

    def __init__(self):
        self._tvmaze_api = TvMazeApi()
        self._shows_context = ShowsContext()
        self._comments_context = CommentsContext()

    def search(self, search_text):
        response = self._tvmaze_api.search(search_text)
        shows = response.json()
        comments = self._get_comments(shows)
        return self._append_comments(shows, comments)

    def show_by_id(self, id):
        show = self._get_show_by_id(id)
        comments = self._get_comments([show])
        with_comments = self._append_comments([show], comments)
        return with_comments[0]

    def _get_show_id(self, show):
        if 'show' in show:
            return show['show']['id']
        return show['id']

    def _get_comments(self, shows):
        ids = list(map(lambda s: self._get_show_id(s), shows))
        response = self._comments_context.by_ids(ids)
        return list(response)

    def _comments_by_show(self, show_id, comments):
        return [c for c in comments if c['show_id'] == show_id]

    def _append_comments(self, shows, comments):
        for show in shows:
            show_id = self._get_show_id(show)
            show['comments'] = self._comments_by_show(show_id, comments)
        return shows

    def _get_show_by_id(self, id):
        show = self._shows_context.by_id(id)
        if (show):
            return show
        response = self._tvmaze_api.show_by_id(id)
        show = response.json()
        self._shows_context.save(show)
        return show
