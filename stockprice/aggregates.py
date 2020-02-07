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


def _sortby(contents, key):
    return sorted((
        {
            'filename': data.filename,
            key: data.contents['quoteSummary']['result'][0]['defaultKeyStatistics'][key]['raw'],
        }
        for data in contents
    ), key=lambda x: x[key])


def pe(cache_base):
    return _sortby(_filecontents(cache_base, cachetools.Folder.SUMMARY), 'forwardPE')
