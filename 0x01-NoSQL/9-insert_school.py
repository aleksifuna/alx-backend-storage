#!/usr/bin/env python3
"""
Supplies one function insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection
    """
    results = mongo_collection.insert_one(kwargs)
    return results.inserted_id
