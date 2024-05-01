#!/usr/bin/env python3
"""Module declares a rides class and methods"""
import rides
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count how many times methods of Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrap the decorated function and return the wrapper'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper
