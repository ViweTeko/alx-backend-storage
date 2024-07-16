#!/usr/bin/env python3
""" Prints Nginx stats"""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """ Print Ngxinx stats"""
    print(f'{nginx_collection.count_documents({})} logs')
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print(f'\tmethod {method}: {req_count}')
    stat_check = len(list(nginx_collection.find({'method': 'GET',
                                                 'path': '/status'})))
    print(f'{stat_check} status check')


def print_top_ips(server_collection):
