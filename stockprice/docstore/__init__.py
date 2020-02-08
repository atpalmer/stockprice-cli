from collections import namedtuple
import json
import os
import re
from .cache import JsonFileCache


Document = namedtuple('Document', ('filename', 'contents'))


def ensure_valid_filename(name):
    if re.match(r'[A-Z]+', name) is None:
        raise ValueError(f'Cannot create document for name "{name}"')
    return name


class DocumentStore(object):
    def __init__(self, path):
        self._path = path

    @classmethod
    def from_path_segments(cls, *segments):
        path = os.path.join(*segments)
        return cls(path)

    def folder(self, subfolder):
        return self.from_path_segments(self._path, subfolder)

    def documents(self):
        filenames = os.listdir(self._path)
        for filename in filenames:
            fullpath = os.path.join(self._path, filename)
            with open(fullpath) as f:
                yield Document(filename=filename, contents=json.load(f))

    def get_or_create(self, name, factory, **kwargs):
        filename = '.'.join((ensure_valid_filename(name), 'json'))
        full_path = os.path.join(self._path, filename)
        return JsonFileCache(full_path, **kwargs).get_values(factory)
