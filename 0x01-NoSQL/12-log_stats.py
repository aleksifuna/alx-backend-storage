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
    print(f"{total_logs} logs")
    print('methods:')
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")
    status_count = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_count} status check")
