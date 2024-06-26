#!/usr/bin/env python3
"""
Defination of class Cache
"""
import redis
from typing import Union, Callable, Optional
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Counts the number of times a method is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Stores the input and output of class method in a list
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def replay(method: Callable) -> None:
    """
    Replays all method calls
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name)
    calls = calls.decode("utf-8") if calls else 0
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        i = i.decode("utf-8") if i else ""
        o = o.decode("utf-8") if o else ""
        print("{}(*{}) -> {}".format(name, i, o))


class Cache:
    """
    Attributes and methods defining class Cache
    """
    _redis = None

    def __init__(self):
        """
        constructor for the class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        client = self._redis
        key = str(uuid4())
        client.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """
        Get data from the db
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Return a string value associated with key in the db
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str):
        """
        Return a int value associated with key in the db"""
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
