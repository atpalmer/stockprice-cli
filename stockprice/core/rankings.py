from collections import namedtuple
import json
import os
from .. import cachetools


File = namedtuple('File', ('filename', 'contents'))


def _filecontents(*args):
    cache_dir = os.path.join(*args)
    filenames = cachetools.readdir(cache_dir)
    for filename in filenames:
        fullpath = os.path.join(cache_dir, filename)
        with open(fullpath) as f:
            yield File(filename=filename, contents=json.load(f))


def _sortby(contents, keys, *, sortkey=None, reverse=False):
    if sortkey is None:
        sortkey = keys[0]
    items = (
        {
            'filename': data.filename,
            **{key: data.contents['quoteSummary']['result'][0]['defaultKeyStatistics'][key].get('raw') for key in keys},
        }
        for data in contents)
    return sorted(
        (item for item in items if item[sortkey] is not None),
        key=lambda x: x[sortkey],
        reverse=reverse)


class Rankings(object):
    def __init__(self, cache_base):
        self._cache_base = cache_base

    def pe(self):
        return _sortby(
            _filecontents(self._cache_base, cachetools.Folder.SUMMARY),
            ['forwardPE', 'earningsQuarterlyGrowth'],
            sortkey='forwardPE')


    def peg(self):
        return _sortby(
            _filecontents(self._cache_base, cachetools.Folder.SUMMARY),
            ['pegRatio', 'forwardPE'],
            sortkey='pegRatio')


    def growth(self):
        return _sortby(
            _filecontents(self._cache_base, cachetools.Folder.SUMMARY),
            ['earningsQuarterlyGrowth'],
            sortkey='earningsQuarterlyGrowth',
            reverse=True)

