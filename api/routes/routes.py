from .shows_routes import shows

def cofigure_routes(app):
    app.include_router(shows)
