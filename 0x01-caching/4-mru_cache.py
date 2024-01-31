#!/usr/bin/python3
"""MRUCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Most recent used caching"""

    def __init__(self):
        """initialize MRUCache class using BaseCaching
        that we inherit from"""
        super().__init__()

    def put(self, key, item):
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
                    # if full and key is new remove Most urecent used
                    # get all keys and select last one it is MRU one
                    # and delete it
                    all_keys = list(self.cache_data.keys())
                    most_r_u_key = all_keys[-1]
                    self.cache_data.pop(most_r_u_key)
                    print("DISCARD: {}".format(most_r_u_key))

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
