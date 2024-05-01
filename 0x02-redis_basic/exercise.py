#!/usr/bin/env python3
"""
Defination of class Cache
"""
import redis
from typing import Union
from uuid import uuid4


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        client = self._redis
        key = str(uuid4())
        client.set(key, data)
        return key
