import os
from . import yahoo
from .cache import JsonFileCache
from . import validation


def cache_file(base, ticker, extension):
    if not validation.is_valid_filename(ticker):
        raise ValueError(f'Cannot create cache file for ticker "{ticker}"')
    return os.path.join(base, f'{ticker}.{extension}')


def compare_close(begin, end):
    return (end['close'] / begin['close']) - 1


def as_percentage(value):
    return '{}%'.format(round(value * 100, 2))


def get_chart_data(*, ticker, cache_base):
    cache = JsonFileCache(
        cache_file(cache_base, ticker, 'json'),
        days=1,
    )
    values = cache.get_values(lambda: yahoo.api.chart(ticker))
    items = yahoo.get_items(values)

    return {
        'day': {
            'previous': items[-2],
            'last': items[-1],
            'change': as_percentage(compare_close(items[-2], items[-1])),
        },
    }
