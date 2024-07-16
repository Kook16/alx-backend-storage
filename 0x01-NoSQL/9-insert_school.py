#!/usr/bin/env python3
'''a Python function that inserts a
new document in a collection based on kwargs
'''
from pymongo import MongoClient
list_all = __import__('8-all').list_all


def insert_school(mongo_collection, **kwargs):
    '''
    - mongo_collection will be the pymongo collection object
    - Returns the new _id
    '''
    if mongo_collection is None:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(
        school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    schools = list_all(school_collection)
