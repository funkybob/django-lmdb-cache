
from django.conf import settings
from django.core.cache.backends.base import BaseCache
from django.core.exceptions import ImproperlyConfigured

import lmdb


class LmdbCache(BaseCache):

    def __init__(self, params):
        super(LmdbCache, self).__init__(params)
        # Rip other options out of params
        self.env = lmdb.open(params['LOCATION'])

    def add(self, key, value, timeout=DEFAULT_TIMEOUT, version=None):
        key = self.make_key(key, version=version)
        return self.env.put(key, value, overwrite=False)

    def get(self, key, default=None, version=None):
        key = self.make_key(key, version=version)
        return self.env.get(key, default=default)

    def set(self, key, value, timeout=DEFAULT_TIMEOUT, version=None):
        key = self.make_key(key, version=version)
        self.env.put(key, value, overwrite=True)

    def delete(self, key, version=None):
        key = self.make_key(key, version=version)
        self.env.delete(key)
    def clear(self):

    # Optional
    #def has_key(self, key, version=None):
    #def incr(self, key, delta=1, version=None):
    #def decr(self, key, delta=1, version=None):
    #def get_many(self, keys, version=None):
    #def set_many(self, data, timeout=DEFAULT_TIMEOUT, version=None):
    #def delete_many(self, keys, version=None):

