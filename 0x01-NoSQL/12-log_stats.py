#!/usr/bin/python3
'''A Python script that provides some stats about Nginx logs stored in MongoDB'''
from pymongo import MongoClient


def print_nginx_stats():
    '''Database: logs
    Collection: nginx
    '''
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    collection = db.nginx

    # Total number of log entries
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Number of entries for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"{method}: {count}")

    # Number of GET requests with path "/status"
    num_status_gets = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{num_status_gets} status check")


if __name__ == "__main__":
    print_nginx_stats()

