#!/usr/bin/env python3
"""
Supplies one function schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic
    """
    results = mongo_collection.find({'topics': topic})
    return list(results)
