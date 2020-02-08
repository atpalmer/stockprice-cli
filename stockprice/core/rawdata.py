from ..sources import yahoo
from ..docstore import DocumentStore
from ..folder import Folder


class RawData(object):
    def __init__(self, cache_base):
        self._cache_base = cache_base

    def chart(self, ticker):
        def compare_close(begin, end):
            return (end['close'] / begin['close']) - 1
        def as_percentage(value):
            return '{}%'.format(round(value * 100, 2))

        store = DocumentStore.from_path_segments(self._cache_base, Folder.CHART)
        values = store.get_or_create(ticker, lambda: yahoo.api.chart(ticker), days=1)

        items = yahoo.get_items(values)
        return {
            'day': {
                'previous': items[-2],
                'last': items[-1],
                'change': as_percentage(compare_close(items[-2], items[-1])),
            },
        }


    def summary(self, ticker):
        store = DocumentStore.from_path_segments(self._cache_base, Folder.SUMMARY)
        data = store.get_or_create(ticker, lambda: yahoo.api.summary(ticker), days=1)
        stats = data['quoteSummary']['result'][0]['defaultKeyStatistics']
        return {k: v.get('raw') for k, v in stats.items() if isinstance(v, dict)}
