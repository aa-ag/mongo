from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import json
from pprint import pprint
import requests


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
    with open("inputs/fake_data.json") as jsonfile:
        contents = json.load(jsonfile)
        collection.insert_many(contents)


def query_mongo_db(mongo_client):
    database = mongo_client["testdb"]
    collection = database["fake_data"]
    for record in collection.find():
        print(record)


if __name__ == "__main__":
    mongo_client = set_mongo_client()
    if mongo_client:
        # insert_data_into_mongodb(mongo_client)
        # query_mongo_db(mongo_client)
        insert_response_into_mongodb(mongo_client)