#!/usr/bin/env python3
"""
Supplies one function get_page
"""
from functools import wraps
import redis
import requests
from typing import Callable

client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    Counts number of times a url has been requested
    """
    @wraps(method)
    def wrapper(url):
        """
        Wrapper for decorator
        """
        client.incr(f"count:{url}")
        cached_results = client.get(f"cached:{url}")
        if cached_results:
            return cached_results.decode('utf-8')
        html = method(url)
        client.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Sends a html request for to url
    """
    req = requests.get(url)
    return req.text
