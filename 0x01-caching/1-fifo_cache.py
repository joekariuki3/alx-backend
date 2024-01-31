#!/usr/bin/python3
"""FIFOCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """first in first out caching"""

    def __init__(self):
        """initialize fifocache class using BaseCaching
        that we inherit from"""
        super().__init__()

    def put(self, key, item):
        """update or add item  with key to
        the cache i.e cache_data using FIFO principle"""
        if key and item:
            # if not full
            if not (len(self.cache_data) == super().MAX_ITEMS):
                self.cache_data[key] = item
            else:
                # if full and key is present update key value
                # delete the key then add it again
                if key in self.cache_data:
                    self.cache_data.pop(key)
                    self.cache_data[key] = item
                else:
                    # if full and key is new  remove 1st item
                    # get list of keys and get 1st one to delete
                    all_keys = list(self.cache_data.keys())
                    first_key = all_keys[0]
                    self.cache_data.pop(first_key)
                    print("DISCARD: {}".format(first_key))

                    # add current/new key and item to cache
                    self.cache_data[key] = item

        def get(self, key):
            """ retrieve the key if it exists"""
            return self.cache_data.get(key)
