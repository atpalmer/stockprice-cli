from datetime import timedelta
import os
from pathlib import Path
from time import time
from ..decimaljson import json


class CacheFileError(Exception):
    pass


class CacheFileTimeout(CacheFileError):
    pass


class CacheFileNotFound(CacheFileError, FileNotFoundError):
    pass


class JsonFileCache(object):
    def __init__(self, filename, **kwargs):
        self._filename = Path(filename)
        self._cache_timeout = timedelta(**kwargs)

    def _ensure_valid_cache_file(self):
        try:
            file_stat = os.stat(self._filename)
            now = time()
            cache_age = now - file_stat.st_mtime
            if cache_age >= self._cache_timeout.total_seconds():
                raise CacheFileTimeout
        except FileNotFoundError:
            raise CacheFileNotFound
        return self._filename

    def _try_get_values_from_file(self):
        filename = self._ensure_valid_cache_file()
        with open(filename, 'r') as f:
            return json.load(f)

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

