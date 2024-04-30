#!/usr/bin/env python3
"""
Write a Python function that changes all topics of a school document based on the name"""

import pymongo

def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})
