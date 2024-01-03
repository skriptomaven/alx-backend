#!/usr/bin/env python3
""" basic dictionary module.
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system that inherits from BaseCaching
        Uses self.cache_data dict from parent class,
        BaseCaching
    This caching system does not have limit.
    """

    def put(self, key, item):
        """
        Assigns to the dict self.cache_data the item
        value for the key key.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
