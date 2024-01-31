#!/usr/bin/python3
"""LFUCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """least requency used caching"""
    frequency = {}

    def __init__(self):
        """initialize LFUCache class using BaseCaching
        that we inherit from"""
        super().__init__()

    def put(self, key, item):
        """update or add item  with key to
        the cache i.e cache_data using least frequently used
        (LFU) principle"""
        if key and item:
            # if not full
            if not (len(self.cache_data) == super().MAX_ITEMS):
                self.cache_data[key] = item
                # start to keep count of frequency from start
                if key in self.frequency:
                    self.frequency[key] += 1
                else:
                    self.frequency[key] = 1
            else:
                # if Full and key in dict update value
                # updated key should be the recent in now
                if key in self.cache_data:
                    # delete the key and add it again to make
                    # it most recent used
                    self.cache_data.pop(key)
                    self.cache_data[key] = item
                    # increase the frequency also
                    self.frequency[key] += 1
                else:
                    # if full and key is new remove least frequent used
                    # check for the one with least frequency in frequency h-map
                    # and delete it
                    least_f_u_key = min(self.frequency, key=self.frequency.get)

                    # look if we have more than 1 least frequent value
                    least_f_u_value = self.frequency[least_f_u_key]
                    least_f_u_keys = [key for key, value in
                                      self.frequency.items()
                                      if value == least_f_u_value]

                    if len(least_f_u_keys) > 1:
                        # we have more than one LFU keys
                        # now use LRU as least_f_u_key
                        # look for index of each LFU keys in cache_data,
                        # one with lowest index is LRU, so we delete that one
                        index = 0
                        lruDict = {}
                        for leastKey in least_f_u_keys:
                            for k, v in self.cache_data.items():
                                if leastKey == k:
                                    lruDict[k] = index
                                index += 1
                            index = 0
                        if lruDict:
                            least_f_u_key = min(lruDict, key=lruDict.get)

                    # delete
                    self.cache_data.pop(least_f_u_key)
                    print("DISCARD: {}".format(least_f_u_key))
                    # remove from freqency h-map
                    self.frequency.pop(least_f_u_key)

                    # add current/new key and item to cache
                    self.cache_data[key] = item

                    # add to frequency h-map
                    self.frequency[key] = 1

    def get(self, key):
        """ retrieve the key if it exists"""
        if key and key in self.cache_data:

            # get value
            value = self.cache_data.get(key)

            # delete the key and add it again to make it most recent used
            self.cache_data.pop(key)
            self.cache_data[key] = value

            # increase frequency
            self.frequency[key] += 1
            return value
        return None
