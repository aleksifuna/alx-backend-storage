#!/usr/bin/env python3
"""Supplies on function list_all"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    results = mongo_collection.find()
    if results.count() == 0:
        return []
    return results
