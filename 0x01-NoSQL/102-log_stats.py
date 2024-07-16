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
    """Prints stats on top 10 IPs collected"""
    req_logs = server_collection.aggregate(
            [
                {
                    '$group': {'_id': "$ip", 'totalRequests': {'sum': 1}}
                },
                {
                    '$sort': {'totalRequests': -1}
                },
                {
                    '$limit': 10
                },
            ]
    )
    for req_log in req_logs:
        ip = req_log['_id']
        ip_req = req_log['totalRequests']
        print(f'\t{ip}: {ip_req}')


def run():
    """Runs Nginx stats stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(clients.logs.nginx)
    print_top_ips(client.logs.nginx)


if __name__ == '__main__':
    run()
