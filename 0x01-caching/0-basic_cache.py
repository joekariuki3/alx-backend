#!/usr/bin/env python3
"""BasicCache implementation"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache implementation"""
    def __init__(self):
        """initiate our BasicCache using the BaseCaching
        which we inherit from"""
        super().__init__()

    def put(self, key, item):
        """updates value of key with item
        if not available do nothing"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ check if key is in cached data
        if so return the value else return none"""
        available_key = self.cache_data.get(key)
        if available_key:
            return self.cache_data[key]
        return None
