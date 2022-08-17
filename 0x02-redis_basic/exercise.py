#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import uuid
import redis
from typing import Union, Optional, Callable


class Cache:
    """
    Cache class store an instance of the Redis client as a private
    variable named _redis (using redis.Redis()) and flush the
    instance using flushdb.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, bytes, float]) -> str:
        """
        Ggenerate a random key (e.g. using uuid), store the input
        data in Redis using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, str(data))
        return key

    """
    def get(self, key: str, fn):
        Optional[Callable[[Union[str]], ]]
        Method that take a key string argument and an optional Callable
        argument named fn to onvert the data back to the desired format.

    def get_str(self):
        Parametrize Cache.get with the str conversion function
    """
