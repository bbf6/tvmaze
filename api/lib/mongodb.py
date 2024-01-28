import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class Connection():
    _connection = None

    @classmethod
    def get_instance(cls):
        if cls._connection is None:
            cls._connection = cls._get_connection()
        return cls._connection

    @classmethod
    def _connection_string(cls):
        host     = os.getenv('DB_HOST')
        db_name  = os.getenv('DB_NAME')
        user     = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        port     = os.getenv('DB_PORT')
        return f'mongodb+srv://{user}:{password}@{host}/{db_name}'

    @classmethod
    def _get_connection(cls):
        db_name  = os.getenv('DB_NAME')
        client = MongoClient(cls._connection_string())
        return client[db_name]
