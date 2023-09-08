"""
This module exposes lru_cache decorator, trying import it from

* https://github.com/pbrady/fastcache;
* functools.lru_cache in standard library;
* https://pypi.python.org/pypi/backports.functools_lru_cache

Also, it provides a caching decorator for functions with a single argument.
"""
import functools


def memoized_with_single_argument(cache):
    """
    Basic caching decorator. It assumes a function only accepts
    a single argument, which is used as a cache key.

    >>> cache = {}
    >>> @memoized_with_single_argument(cache)
    ... def func(x):
    ...     return x*2
    >>> func(2)
    4
    >>> cache
    {2: 4}
    >>> cache[2] = 6
    >>> func(2)
    6
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            if arg in cache:
                return cache[arg]
            res = func(arg)
            cache[arg] = res
            return res
        return wrapper
    return decorator
