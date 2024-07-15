#!/usr/bin/env python3
""" Write a script that prints log stats"""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """Prints Nginx stats request logs"""
    print(f'{nginx_collections.count_documents({})} logs')
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        re_count = len(list(nginx_collection.find({'method: method'})))
        print(f'\tmethod {method}: {re_count}')
    stat_check = len(list(nginx_collection.find({
        'method': 'GET',
        'path': '/status'
        })
    ))
    print(f'{stat_check} status check')


def run():
    """Stores Nginx logs in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()