#!/usr/bin/python3
"""LIFOCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Last in first out caching"""

    def __init__(self):
        """initialize Lifocache class using BaseCaching
        that we inherit from"""
        super().__init__()

    def put(self, key, item):
        """update or add item  with key to
        the cache i.e cache_data using LIFO principle"""
        if key and item:
            # if not full
            if not (len(self.cache_data) == super().MAX_ITEMS):
                self.cache_data[key] = item
            else:
                # if Full and key in dict update value
                # updated key should be the last in now
                if key in self.cache_data:
                    # delete the key
                    self.cache_data.pop(key)
                    # add the key to make it last one in
                    self.cache_data[key] = item
                else:
                    # if full and new key remove last item
                    # dict.popitem()- returns last in key and value
                    last_key, last_value = self.cache_data.popitem()
                    print("DISCARD: {}".format(last_key))

                    # add current/new key and item to cache
                    self.cache_data[key] = item

        def get(self, key):
            """ retrieve the key if it exists"""
            if key and key in self.cache_data:
                value = self.cache_data[key]
                self.cache_data.pop(key)
                self.cache_data[key] = item
                return value
            return None
