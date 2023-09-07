from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import json
from pprint import pprint


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


def insert_data_into_mongodb(mongo_client):
    database = mongo_client["testdb"]
    collection = database["fake_data"]
    example = {"name": "John", "lastname": "Doe"}
    collection.insert_one(example)


if __name__ == "__main__":
    mongo_client = set_mongo_client()
    if mongo_client:
        insert_data_into_mongodb(mongo_client)