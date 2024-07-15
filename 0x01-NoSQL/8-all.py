#!/usr/bin/env python3
"""List all documents in collection"""


def list_all(mongo_collection):
    """Lists all docs"""
    return [doc for doc in mongo_colletion.find()]