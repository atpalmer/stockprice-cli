from datetime import datetime, timezone
from ..sources import yahoo
from ._schemas import schemas


class _Chart(object):
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


def documents(folder):
    return schemas.folder(folder).documents()


def chart(ticker):
    def compare_close(begin, end):
        return (end['close'] / begin['close']) - 1
    def as_percentage(value):
        return '{}%'.format(round(value * 100, 2))

    values = schemas.chart.get_or_create(
        ticker, lambda: yahoo.api.chart(ticker), days=1)

    items = _Chart(values).get_items()
    return {
        'day': {
            'previous': items[-2],
            'last': items[-1],
            'change': as_percentage(compare_close(items[-2], items[-1])),
        },
    }


def key_statistics(ticker):
    data = schemas.key_statistics.get_or_create(
        ticker, lambda: yahoo.api.key_statistics(ticker), days=1)
    stats = data['quoteSummary']['result'][0]['defaultKeyStatistics']
    return {k: v.get('raw') for k, v in stats.items() if isinstance(v, dict)}


def profile(ticker):
    data = schemas.profile.get_or_create(
        ticker, lambda: yahoo.api.summary_profile(ticker), days=1)
    return data['quoteSummary']['result'][0]['summaryProfile']


def financial(ticker):
    data = schemas.financial.get_or_create(
        ticker, lambda: yahoo.api.financial_data(ticker), days=1)
    result = data['quoteSummary']['result'][0]['financialData']
    return {k: v.get('raw') if isinstance(v, dict) else v for k, v in result.items()}


def price(ticker):
    data = schemas.price.get_or_create(
        ticker, lambda: yahoo.api.price(ticker), days=1)
    result = data['quoteSummary']['result'][0]['price']
    return {k: v.get('raw') if isinstance(v, dict) else v for k, v in result.items()}

