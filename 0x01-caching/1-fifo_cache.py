#!/usr/bin/env python3
""" FIFO caching module.
"""


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ Caching system that inherits from parent class,
    BaseCaching. Using self.cache_data dictionary.
    """
    def __init__(self):
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        Does nothing if key/item is None.
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_item = self.key_indexes.pop(0)
                del self.cache_data[discarded_item]
                print("DISCARD:", discarded_item)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
