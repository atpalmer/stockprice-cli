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


def _sortby(contents, key, *, reverse=False):
    items = (
        {
            'filename': data.filename,
            key: data.contents['quoteSummary']['result'][0]['defaultKeyStatistics'][key].get('raw'),
        }
        for data in contents)
    return sorted(
        (item for item in items if item[key] is not None),
        key=lambda x: x[key],
        reverse=reverse)


def pe(cache_base):
    return _sortby(_filecontents(cache_base, cachetools.Folder.SUMMARY), 'forwardPE')


def peg(cache_base):
    return _sortby(_filecontents(cache_base, cachetools.Folder.SUMMARY), 'pegRatio')


def growth(cache_base):
    return _sortby(_filecontents(cache_base, cachetools.Folder.SUMMARY), 'earningsQuarterlyGrowth', reverse=True)
