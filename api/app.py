from fastapi import FastAPI
from routes.routes import cofigure_routes
from config.app_metadata import metadata

app = FastAPI(**metadata)
cofigure_routes(app)
