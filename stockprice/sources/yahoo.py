from datetime import datetime, timezone
import re
import requests
from ..jsonwebapi import jsonwebapi


def ensure_valid_ticker(ticker):
    if re.match(r'[A-Z]+', ticker) is None:
        raise ValueError(f'Symbol "{ticker}" is not a valid ticker')
    return ticker


class api(object):
    def chart(ticker, *, interval='1d', range='30d'):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
            'params': {
                'region': 'US',
                'lang': 'en-US',
                'includePrePost': 'false',
                '.tsrc': 'finance',
                'interval': interval,
                'range': range,
            },
        }
        return jsonwebapi.get(**opts)

    def summary(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
            'params': {
                'modules': 'defaultKeyStatistics'
            },
        }
        return jsonwebapi.get(**opts)

    def quote_type(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v1/finance/quoteType/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
        }
        return jsonwebapi.get(**opts)

