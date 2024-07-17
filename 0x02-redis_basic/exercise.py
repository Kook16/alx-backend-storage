#!/usr/bin/env python3
'''Writing strings to Redis
'''
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count calls to the method.
    """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrapper func'''
        # Increment the count for the method key
        self._redis.incr(key)
        # Call the original method
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.
    """

    # Create input and output keys using the method's qualified name
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrapper func'''

        # Log input arguments to the input list in Redis
        self._redis.rpush(input_key, str(args))

        # Call the original method and get the output
        output = method(self, *args, **kwargs)

        # Log output result to the output list in Redis
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable) -> None:
    """display the history of calls of a particular function
    """
    key = method.__qualname__
    data = redis.Redis()
    hist = data.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, hist))
    inputs = data.lrange(key + ":inputs", 0, -1)
    outputs = data.lrange(key + ":outputs", 0, -1)
    for k, v in zip(inputs, outputs):
        print(f"{key}(*{k.decode('utf-8')}) -> {v.decode('utf-8')}")


class Cache:
    '''cache class'''
    def __init__(self):
        '''Initialize the Redis client and flush the database'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''returns a string'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        '''convert the data back to the desired format'''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        '''Use the get method with a conversion function to
        convert to string'''
        return self.get(key, str)

    def get_int(self, key: str) -> Optional[int]:
        '''Use the get method with a conversion function to convert to int'''
        return self.get(key, int)
