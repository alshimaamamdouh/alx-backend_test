#!/usr/bin/env python3
""" documentaion """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ documentaion """

    def put(self, key, item):
        """ documentaion """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ documentaion """

        return self.cache_data.get(key) 
