#!/usr/bin/env python3
"""
Insert a document in Python
"""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
     """
     Function that inserts a new document in a collection based on kwargs
     """
     if mongo_collection is None:
          return []
     return mongo_collection.insert_one(kwargs)


if __name__ == "__main__":
     list_all = __import__('8-all').list_all

     client = MongoClient('mongodb://127.0.0.1:27017')
     school_collection = client.my_db.school
     new_school_id = insert_school(school_collection, name="UCSF",
                                   address="505 Parnassus Ave")
     print("New school created: {}".format(new_school_id))

     schools = list_all(school_collection)
     for school in schools:
          print("[{}] {} {}".format(school.get('_id'), school.get('name'),
                                    school.get('address', "")))
