#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

if __name__ == "__main__":
    client = MongoClient()
    logs_collection = client.logs.nginx
    total_logs = logs_collection.count_documents({})
    print("{} logs".format(total_logs))
    print('methods:')
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    status_count = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print("{} status check".format(status_count))
