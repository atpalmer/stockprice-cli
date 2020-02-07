from collections import namedtuple
import json
import os
from . import cachetools


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


def pe(cache_base):
    return _sortby(
        _filecontents(cache_base, cachetools.Folder.SUMMARY),
        ['forwardPE', 'earningsQuarterlyGrowth'],
        sortkey='forwardPE')


def peg(cache_base):
    return _sortby(
        _filecontents(cache_base, cachetools.Folder.SUMMARY),
        ['pegRatio', 'forwardPE'],
        sortkey='pegRatio')


def growth(cache_base):
    return _sortby(
        _filecontents(cache_base, cachetools.Folder.SUMMARY),
        ['earningsQuarterlyGrowth'],
        sortkey='earningsQuarterlyGrowth',
        reverse=True)

