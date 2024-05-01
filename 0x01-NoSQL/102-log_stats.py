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

    top_ips = logs_collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
                }},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
            }}
        ])
    print("IPs:")
    for top_ip in top_ips:
        ip = top_ip.get("ip")
        count = top_ip.get("count")
        print("\t{}: {}".format(ip, count))
