#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import uuid
import redis
from typing import Union


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
        self._redis.set(key, data)
        return key


if __name__ == "__main__":
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))
