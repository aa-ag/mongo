from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import json


load_dotenv()
uri=os.environ.get("URI")


def set_mongo_client():
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        return client
    except Exception as e:
        print(e)
        return 


if __name__ == "__main__":
    set_mongo_client()