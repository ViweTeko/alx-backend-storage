#!/usr/bin/env python3
""" This script tracks and caches requests"""
from redis import Redis
import requests
from functools import wraps
from typing import Callable

store_re = Redis()
"""Module-level Redis instance"""


def data_cacher(method: Callable) -> Callable:
    """Caches output of fetched data"""
    @wraps(method)
    def invoker(url: str) -> str:
        """Wrapper funtion to cache output"""
        store_re.incr(f'count:{url}')

        cached_res = store_re.get(f'result:{url}')
        if chached_res:
            return cached_res.decode('utf-8')
        result = method(url)
        store_re.setex(f'result:{url}', 10, result)

        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Returns url content after caching"""
    return requests.get(url).text
