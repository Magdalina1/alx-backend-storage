#!/usr/bin/env python3
"""Write a Python script that provides some stats about Nginx logs stored in MongoDB"""

import pymongo
from pymongo import MongoClient

def log_nginx_stats(mongo_collection):
    """provides some stats about Nginx logs"""
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    number_of_gets = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{number_of_gets} status check")
