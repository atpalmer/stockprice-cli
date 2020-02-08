from datetime import datetime, timezone
import re
import requests


def ensure_valid_ticker(ticker):
    if re.match(r'[A-Z]+', ticker) is None:
        raise ValueError(f'Symbol "{ticker}" is not a valid ticker')
    return ticker


DEFAULT_PARAMS = {
    'region': 'US',
    'lang': 'en-US',
    'includePrePost': 'false',
    'interval': '1d',
    'range': '30d',
    '.tsrc': 'finance',
}


class api(object):
    def chart(ticker, *, interval='1d', range='30d'):
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}'.format(
            ticker=ensure_valid_ticker(ticker))
        response = requests.get(
            url, params={**DEFAULT_PARAMS, 'interval': interval, 'range': range})
        response.raise_for_status()
        return response.json()

    def summary(ticker):
        url = 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}'.format(
            ticker=ensure_valid_ticker(ticker))
        response = requests.get(
            url, params={'modules': 'defaultKeyStatistics'})
        response.raise_for_status()
        return response.json()


def get_items(data):
    unwrapped_data = data['chart']['result'][0]
    indicators = unwrapped_data['indicators']['quote'][0]
    timestamps = (
        datetime.fromtimestamp(ts).replace(tzinfo=timezone.utc).isoformat()
        for ts in unwrapped_data['timestamp'])
    return [
        {k: v  for k, v in zip((*indicators.keys(), 'timestamp'), row)}
        for row in zip(*indicators.values(), timestamps)
    ]

