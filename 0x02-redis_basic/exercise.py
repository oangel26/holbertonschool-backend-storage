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
        self._redis = redis.Redis(charset="utf-8")
        self._redis.flushdb()

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
        Optional[Callable[[Union[str]], ]]
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

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
