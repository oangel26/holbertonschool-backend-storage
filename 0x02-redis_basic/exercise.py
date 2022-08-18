#!/usr/bin/env python3
"""
Redis Basic Module
"""

import uuid
import redis
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """  count how many times methods of the Cache class are called """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        method_name = method.__qualname__
        self._redis.incr(method_name)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Method that stores the history of inputs and
    outputs for a particular function.
    Returns:
            Input and output list keys.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        method_name = method.__qualname__
        data = str(args)
        method_result = method(self, data)
        self._redis.rpush("{}:inputs".format(method_name), data)
        self._redis.rpush("{}:outputs".format(method_name), method_result)
        return method_result
    return wrapper


def replay(func: Callable):
    """
    Function to display the history of calls of a particular function.
    """
    r = redis.Redis()
    method_name = func.__qualname__
    inputs = r.lrange("{}:inputs".format(method_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(method_name), 0, -1)
    call_number = len(inputs)
    times_str = 'times'
    if call_number == 1:
        times_str = 'time'
    msg = '{} was called {} {}:'.format(method_name, call_number, times_str)
    print(msg)
    for k, v in zip(inputs, outputs):
        msg = '{}(*{}) -> {}'.format(
            method_name,
            k.decode('utf8'),
            v.decode('utf8')
        )
        print(msg)


class Cache:
    """
    Cache class store an instance of the Redis client as a private
    variable named _redis (using redis.Redis()) and flush the
    instance using flushdb.
    """
    def __init__(self):
        self._redis = redis.Redis(charset="utf-8")
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[int, str, bytes, float]) -> str:
        """
        Ggenerate a random key (e.g. using uuid), store the input
        data in Redis using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] =
            None) -> Union[str, bytes, int, float]:
        """
        Method that take a key string argument and an optional Callable
        argument named fn to onvert the data back to the desired format.
        """
        result = self._redis.get(key)
        if fn:
            return fn(result)
        return result

    def get_str(self, key) -> str:
        """
        Parametrize Cache.get with the str conversion function
        """
        return self.get(key, str)

    def get_int(self, key) -> int:
        """
        Parametrize Cache.get with the str conversion function
        """
        return self.get(key, int)


if __name__ == "__main__":
    cache = Cache()

    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))
