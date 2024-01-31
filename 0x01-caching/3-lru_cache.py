#!/usr/bin/python3
"""LRUCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """least recent used caching"""

    def __init__(self):
        """initialize LRUCache class using BaseCaching
        that we inherit from"""
        super().__init__()

    def put(self, key, item):
        """update or add item  with key to
        the cache i.e cache_data using least recent used
        (LRU) principle"""
        if key and item:
            # if not full
            if not (len(self.cache_data) == super().MAX_ITEMS):
                self.cache_data[key] = item
            else:
                # if Full and key in dict update value
                # updated key should be the recent in now
                if key in self.cache_data:
                    # delete the key and add it again to make
                    # it most recent used
                    self.cache_data.pop(key)
                    self.cache_data[key] = item
                else:
                    # if full and key is new remove least urecent used
                    # get all keys and select 1st one it is LRU one
                    # and delete it
                    all_keys = list(self.cache_data.keys())
                    least_r_u_key = all_keys[0]
                    self.cache_data.pop(least_r_u_key)
                    print("DISCARD: {}".format(least_r_u_key))

                    # add current/new key and item to cache
                    self.cache_data[key] = item

    def get(self, key):
        """ retrieve the key if it exists"""
        if key and key in self.cache_data:
            # get value
            value = self.cache_data.get(key)
            # delete the key and add it again to make it most recent used
            self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
