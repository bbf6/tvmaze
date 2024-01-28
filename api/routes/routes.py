from .shows_routes import shows
from .comments_routes import comments

def cofigure_routes(app):
    app.include_router(shows)
    app.include_router(comments)
