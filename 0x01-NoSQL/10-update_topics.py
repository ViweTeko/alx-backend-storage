#!/usr/bin/env python3
""" Change all topics of collections based on name"""


def update_topics(mongo_collection, name, topics):
    """Change all topics"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )