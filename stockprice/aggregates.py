import os
from . import cachetools


def pe(cache_base):
    cache_dir = os.path.join(cache_base, cachetools.Folder.SUMMARY)
    return cachetools.readdir(cache_dir)
