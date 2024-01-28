import os
from dotenv import load_dotenv

load_dotenv()
_version = os.getenv('VERSION')

_tags_metadata = [
    {
        'name': 'shows',
        'description': 'Access to Tv Maze shows library'
    }
]

metadata = {
    'title': 'Tv Maze API',
    'description': 'This is an API that allows you to add ranks and comments \
    about tv shows',
    'version': _version,
    'openapi_tags': _tags_metadata
}
