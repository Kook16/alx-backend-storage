#!/usr/bin/env python3
'''a Python function that lists all documents in a collection:'''
from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    
    :param mongo_collection: pymongo collection object
    :return: List of documents in the collection, or an empty list if no documents are found
    """
    if mongo_collection is None:
        return []
    
    return list(mongo_collection.find())

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
