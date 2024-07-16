#!/usr/bin/python3
'''a Python function that returns the list of school having a specific topic
'''
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school



def schools_by_topic(mongo_collection, topic):
    '''
    - mongo_collection will be the pymongo collection object
    - topic (string) will be topic searched
    '''
    if mongo_collection is None:
        return None
    return mongo_collection.find(
        {'topics': topic}
    )


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    j_schools = [
        {'name': "Holberton school", 'topics': [
            "Algo", "C", "Python", "React"]},
        {'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
        {'name': "UCLA", 'topics': ["C", "Python"]},
        {'name': "UCSD", 'topics': ["Cassandra"]},
        {'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    ]
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'),
              school.get('name'), school.get('topics', "")))