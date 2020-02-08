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


class _requests(object):
    def get(*args, **kwargs):
        response = requests.get(*args, **kwargs)
        response.raise_for_status()
        return response.json()


class api(object):
    def chart(ticker, *, interval='1d', range='30d'):
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}'.format(
            ticker=ensure_valid_ticker(ticker))
        return _requests.get(
            url, params={**DEFAULT_PARAMS, 'interval': interval, 'range': range})

    def summary(ticker):
        url = 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}'.format(
            ticker=ensure_valid_ticker(ticker))
        return _requests.get(
            url, params={'modules': 'defaultKeyStatistics'})

