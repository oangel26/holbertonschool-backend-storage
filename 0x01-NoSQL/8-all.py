#!/usr/bin/env python3
"""
 List all documents in Python
"""

def list_all(mongo_collection):
    """ Function that lists all documents in a collection """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({}))


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
