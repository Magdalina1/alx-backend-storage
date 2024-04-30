#!/usr/bin/env python3
"""update school names by topic"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
