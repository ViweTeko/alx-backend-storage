#!/usr/bin/env python3
""" Inserts new document in collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert new doc"""
    res = mongo_colletion.insert_one(kwargs)
    return res.inserted_id