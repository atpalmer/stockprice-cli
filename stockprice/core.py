import os
from . import yahoo
from .cache import JsonFileCache
from . import validation


def cache_file(base, folder, ticker, extension):
    if not validation.is_valid_filename(ticker):
        raise ValueError(f'Cannot create cache file for ticker "{ticker}"')
    return os.path.join(base, folder, f'{ticker}.{extension}')


def yahoo_cache(cache_base, folder, ticker, *, days):
    return JsonFileCache(
        cache_file(cache_base, folder, ticker, 'json'), days=days)


class Folder(object):
    CHART = 'chart'
    SUMMARY = 'summary'


def get_chart_data(*, ticker, cache_base):
    def compare_close(begin, end):
        return (end['close'] / begin['close']) - 1
    def as_percentage(value):
        return '{}%'.format(round(value * 100, 2))

    cache = yahoo_cache(cache_base, Folder.CHART, ticker, days=1)
    values = cache.get_values(lambda: yahoo.api.chart(ticker))
    items = yahoo.get_items(values)
    return {
        'day': {
            'previous': items[-2],
            'last': items[-1],
            'change': as_percentage(compare_close(items[-2], items[-1])),
        },
    }


def get_summary(*, ticker, cache_base):
    cache = yahoo_cache(cache_base, Folder.SUMMARY, ticker, days=1)
    data = cache.get_values(lambda: yahoo.api.summary(ticker))
    stats = data['quoteSummary']['result'][0]['defaultKeyStatistics']
    return {k: v.get('raw') for k, v in stats.items() if isinstance(v, dict)}
