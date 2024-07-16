#!/usr/bin/python3
'''a Python function that changes all topics of a school document based on the name
'''
from pymongo import MongoClient
list_all = __import__('8-all').list_all


def update_topics(mongo_collection, name, topics):
    '''
    - mongo_collection will be the pymongo collection object
    - name (string) will be the school name to update
    - topics (list of strings) will be the list of topics approached in the school
    '''
    if mongo_collection is None:
        return
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    update_topics(school_collection, "Holberton school",
                  ["Sys admin", "AI", "Algorithm"])