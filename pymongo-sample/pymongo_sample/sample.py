import typing

from pymongo import MongoClient


def connect():
    return MongoClient("mongodb://root:root@localhost:27017").test.my_collection


def insert(document: dict, connection: typing.Any):
    connection.insert_one(document)
    pass


def upsert(key: str, connection: typing.Any, document: dict):
    connection.update_one(
        {
            "_id": key
        },
        {
            "$set": document
        },
        upsert=True
    )
    pass


def find(key: str, connection: typing.Any) -> dict:
    return connection.find_one({"_id": key})
