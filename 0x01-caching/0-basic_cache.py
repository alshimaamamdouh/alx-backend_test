#!/usr/bin/env python3

"""Task 0
"""

from importlib import import_module

# Assuming 'base_caching' is the module you want to import
module_name = 'base_caching'
module = import_module(module_name)
BaseCaching = module.BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache  """

    def put(self, key, item):
        """put
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get
        """

        return self.cache_data.get(key, None)
