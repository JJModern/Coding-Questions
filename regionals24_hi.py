from functools import lru_cache

@lru_cache
def rec():
    print("hi")

rec()