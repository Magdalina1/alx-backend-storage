#!/usr/bin/env python3
"""In this tasks, we will implement a get_page function
(prototype: def get_page(url: str) -> str:). The core of
the function is very simple. It uses the requests module
to obtain the HTML content of a particular URL and returns it.

Start in a new file named web.py and do not reuse the code
written in exercise.py.

Inside get_page track how many times a particular URL was
accessed in the key "count:{url}" and cache the result with
an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate
a slow response and test your caching."""


import requests
import redis
import time
from functools import wraps
from typing import Callable

def cache_page(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(url: str) -> str:
        cache_key = f"page:{url}"
        count_key = f"count:{url}"

        cached_content = redis_client.get(cache_key)
        if cached_content:
            redis_client.incr(count_key)
            return cached_content.decode('utf-8')

        content = func(url)
        redis_client.setex(cache_key, 10, content)
        redis_client.setex(count_key, 10, 1)
        return content

    return wrapper

@cache_page
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    redis_client = redis.Redis()
    url = "http://slowwly.robertomurray.co.uk/delay/10000/url/http://www.example.com"
    start_time = time.time()
