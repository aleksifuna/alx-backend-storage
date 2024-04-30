#!/usr/bin/env python3
"""
Supplies one function update_topics
"""


def update_topics(mongo_collection, name, topics):
    """Updates all topics of a school document"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
