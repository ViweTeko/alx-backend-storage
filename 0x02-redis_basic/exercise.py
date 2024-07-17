#!/usr/bin/env python3
""" This script uses the Redis NoSQL database to store data"""
from redis import Redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    """Counts calls to Cache class methods"""
    @wraps(method)
    def invoker(self, *args, **kwargs):
        """Invokes the method"""
        if isinstance(self.__redis, redis.Redis)
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker

def call_history(method: Callable) -> Callable:
    """Tracks call history in Cache class"""
    @wraps(method)
    def invoker(self, *args, **kwargs):
        """Invokes the method's output"""
        key_in = f'{method.__qualname__}:inputs'
        key_out = f'{method.__qualname__}:outputs'
        if isinstance(self.__redis, Redis):
            self._redis.rpush(key_in, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self.__redis, Redis):
            self._redis.rpush(key_out, str(output))
        return output
    return invoker


def replay(fn: Callable) -> None:
    """ Displays call history of Cache"""
    if fn is None or not hasattr(fn, '__self__'):
        return
    store_re = getattr(fn.__self__, '_redis', None)
    if not isinstance(store_re, Redis):
        return
    fname = fn.__qualname__
    key_in = f'{fname}:inputs'
    key_out = f'{fname}:outputs'
    fcount = 0
    if store_re.exists(fname) != 0:
        fcount = int(store_re.get(fname))
    print(f'{fname} was called {fcount} times:')
    f_inputs = store_re.lrange(key_in, 0, -1)
    f_outputs = store_re.lrange(key_out, 0, -1)
    for f_input, f_output in zip(f_inputs, f_outputs):
        print(f'{fname}(*{f_input.decode()}) -> {f_output}')

class Cache:
    """Redis caching class"""

    def __init__(self) -> None:
        """Initializes Cache instance"""
        self._redis = Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Gets data from Redis"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: bytes) -> str:
        """Converts bytes to str"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Converts bytes to int"""
        return self.get(key, lambda x: int(x))