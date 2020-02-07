import os
from .cache import JsonFileCache
from . import validation


def _cache_file(base, folder, ticker, extension):
    if not validation.is_valid_filename(ticker):
        raise ValueError(f'Cannot create cache file for ticker "{ticker}"')
    return os.path.join(base, folder, f'{ticker}.{extension}')


def yahoo_cache(cache_base, folder, ticker, *, days):
    return JsonFileCache(
        _cache_file(cache_base, folder, ticker, 'json'), days=days)


class Folder(object):
    CHART = 'chart'
    SUMMARY = 'summary'
