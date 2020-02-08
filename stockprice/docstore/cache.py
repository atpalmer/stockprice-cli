from datetime import timedelta
import json
import os
from pathlib import Path
from time import time


class CacheFileError(Exception):
    pass


class JsonFileCache(object):
    def __init__(self, filename, **kwargs):
        self._filename = Path(filename)
        self._cache_timeout = timedelta(**kwargs)

    def _try_get_values_from_file(self):
        try:
            file_stat = os.stat(self._filename)
            now = time()
            cache_age = now - file_stat.st_mtime

            if cache_age >= self._cache_timeout.total_seconds():
                raise CacheFileError()

            with open(self._filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise CacheFileError

    def _write_values_to_file(self, data):
        os.makedirs(self._filename.parent, exist_ok=True)
        with open(self._filename, 'w') as f:
            return json.dump(data, f)

    def refresh_values(self, factory):
        data = factory()
        self._write_values_to_file(data)
        return data

    def get_values(self, factory):
        try:
            return self._try_get_values_from_file()
        except CacheFileError:
            return self.refresh_values(factory)
