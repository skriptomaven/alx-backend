#!/usr/bin/env python3
"""
LRU caching module.
"""


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    Caching system that inherits from class, BaseCaching.
    """

    def __init__(self):
        """
        Init instance.
        """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        Assigns to the dict self.cache_data the item
        value for the key.
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    discarded_item = self.key_indexes.pop(self.MAX_ITEMS - 1)
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
