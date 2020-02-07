from .sources import yahoo
from .cachetools import yahoo_cache, Folder


class RawData(object):
    def __init__(self, cache_base):
        self._cache_base = cache_base

    def chart(self, ticker):
        def compare_close(begin, end):
            return (end['close'] / begin['close']) - 1
        def as_percentage(value):
            return '{}%'.format(round(value * 100, 2))

        cache = yahoo_cache(self._cache_base, Folder.CHART, ticker, days=1)
        values = cache.get_values(lambda: yahoo.api.chart(ticker))
        items = yahoo.get_items(values)
        return {
            'day': {
                'previous': items[-2],
                'last': items[-1],
                'change': as_percentage(compare_close(items[-2], items[-1])),
            },
        }


    def summary(self, ticker):
        cache = yahoo_cache(self._cache_base, Folder.SUMMARY, ticker, days=1)
        data = cache.get_values(lambda: yahoo.api.summary(ticker))
        stats = data['quoteSummary']['result'][0]['defaultKeyStatistics']
        return {k: v.get('raw') for k, v in stats.items() if isinstance(v, dict)}
