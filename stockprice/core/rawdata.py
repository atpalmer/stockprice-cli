from ..sources import yahoo
from ..docstore import DocumentStore
from ..models.yahoo import Chart
from . import Folder


class RawData(object):
    def __init__(self, cache_base):
        self._root_store = DocumentStore(cache_base)

    def chart(self, ticker):
        def compare_close(begin, end):
            return (end['close'] / begin['close']) - 1
        def as_percentage(value):
            return '{}%'.format(round(value * 100, 2))

        values = self._root_store.folder(Folder.CHART).get_or_create(
            ticker, lambda: yahoo.api.chart(ticker), days=1)

        items = Chart(values).get_items()
        return {
            'day': {
                'previous': items[-2],
                'last': items[-1],
                'change': as_percentage(compare_close(items[-2], items[-1])),
            },
        }

    def summary(self, ticker):
        data = self._root_store.folder(Folder.SUMMARY).get_or_create(
            ticker, lambda: yahoo.api.summary(ticker), days=1)
        stats = data['quoteSummary']['result'][0]['defaultKeyStatistics']
        return {k: v.get('raw') for k, v in stats.items() if isinstance(v, dict)}

    def profile(self, ticker):
        data = self._root_store.folder(Folder.PROFILE).get_or_create(
            ticker, lambda: yahoo.api.summary_profile(ticker), days=1)
        return data['quoteSummary']['result'][0]['summaryProfile']

    def financial(self, ticker):
        data = self._root_store.folder(Folder.FINANCIAL).get_or_create(
            ticker, lambda: yahoo.api.financial_data(ticker), days=1)
        result = data['quoteSummary']['result'][0]['financialData']
        return {k: v.get('raw') if isinstance(v, dict) else v for k, v in result.items()}

