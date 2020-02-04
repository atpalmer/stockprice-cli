from datetime import datetime, timezone
import requests
from . import validation


DEFAULT_PARAMS = {
    'region': 'US',
    'lang': 'en-US',
    'includePrePost': 'false',
    'interval': '1d',
    'range': '30d',
    '.tsrc': 'finance',
}


def yahoo_url(ticker):
    if not validation.ticker_is_valid(ticker):
        raise ValueError(f'Symbol "{ticker}" is not a valid ticker')
    return f'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}'


def get_values_from_internet(ticker, *, interval='1d', range='30d'):
    response = requests.get(
        yahoo_url(ticker),
        params={**DEFAULT_PARAMS, 'interval': interval, 'range': range})
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
