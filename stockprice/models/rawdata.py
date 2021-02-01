from datetime import datetime, timezone
from ..sources import yahoo
from ..docstore import DocumentStore
from .folder import Folder


class Chart(object):
    def __init__(self, data):
        self._data = data

    def get_items(self):
        unwrapped_data = self._data['chart']['result'][0]
        indicators = unwrapped_data['indicators']['quote'][0]
        timestamps = (
            datetime.fromtimestamp(ts).replace(tzinfo=timezone.utc).isoformat()
            for ts in unwrapped_data['timestamp'])
        return [
            {k: v  for k, v in zip((*indicators.keys(), 'timestamp'), row)}
            for row in zip(*indicators.values(), timestamps)
        ]


class transformations(object):
    @staticmethod
    def key_statistics(data):
        stats = data['quoteSummary']['result'][0]['defaultKeyStatistics']
        return {k: v.get('raw') for k, v in stats.items() if isinstance(v, dict)}

    @staticmethod
    def profile(data):
        return data['quoteSummary']['result'][0]['summaryProfile']

    @staticmethod
    def financial(data):
        result = data['quoteSummary']['result'][0]['financialData']
        return {k: v.get('raw') if isinstance(v, dict) else v for k, v in result.items()}

    @staticmethod
    def price(data):
        result = data['quoteSummary']['result'][0]['price']
        return {k: v.get('raw') if isinstance(v, dict) else v for k, v in result.items()}


class RawData(object):
    def __init__(self, cache_base):
        self._root_store = DocumentStore(cache_base)

    def documents(self, folder):
        return self._root_store.folder(folder).documents()

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

    def key_statistics(self, ticker):
        data = self._root_store.folder(Folder.KEY_STATISTICS).get_or_create(
            ticker, lambda: yahoo.api.key_statistics(ticker), days=1)
        return transformations.key_statistics(data)

    def profile(self, ticker):
        data = self._root_store.folder(Folder.PROFILE).get_or_create(
            ticker, lambda: yahoo.api.summary_profile(ticker), days=1)
        return transformations.profile(data)

    def financial(self, ticker):
        data = self._root_store.folder(Folder.FINANCIAL).get_or_create(
            ticker, lambda: yahoo.api.financial_data(ticker), days=1)
        return transformations.financial(data)

    def price(self, ticker):
        data = self._root_store.folder(Folder.PRICE).get_or_create(
            ticker, lambda: yahoo.api.price(ticker), days=1)
        return transformations.price(data)

