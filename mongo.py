from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import json
from pprint import pprint
import requests


load_dotenv()
uri=os.environ.get("URI")
apikey=os.environ.get("APIKEY")


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


def get_data_from_api():
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term":"nope"}
    headers = {
        "X-RapidAPI-Key": "5c7216f484msh56565761e802c49p1e6e56jsnc82ebfad10ef",
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


if __name__ == "__main__":
    response_from_api = get_data_from_api()
    print(response_from_api)
    # mongo_client = set_mongo_client()
    # if mongo_client:
        # insert_data_into_mongodb(mongo_client)
        # query_mongo_db(mongo_client)
        