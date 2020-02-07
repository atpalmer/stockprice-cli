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


def pe(cache_base):
    return sorted((
        dict(
            filename=data.filename,
            pe=data.contents['quoteSummary']['result'][0]['defaultKeyStatistics']['forwardPE']['raw'],
        )
        for data in _filecontents(cache_base, cachetools.Folder.SUMMARY)
    ), key=lambda x: x['pe'])
