from datetime import datetime, timezone
import re
import requests
from ..jsonwebapi import jsonwebapi


def ensure_valid_ticker(ticker):
    if re.match(r'[A-Z]+', ticker) is None:
        raise ValueError(f'Symbol "{ticker}" is not a valid ticker')
    return ticker


class api(object):
    def currencies():
        opts = {
            'url': 'https://query1.finance.yahoo.com/v1/finance/currencies',
        }
        return jsonwebapi.get(**opts)

    def news(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v2/finance/news',
            'params': {
                'symbol': ensure_valid_ticker(ticker),
            },
        }
        return jsonwebapi.get(**opts)

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

    def summary_profile(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
            'params': {
                'modules': 'summaryProfile'
            },
        }
        return jsonwebapi.get(**opts)

    def recommendation_trend(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
            'params': {
                'modules': 'recommendatonTrend'
            },
        }
        return jsonwebapi.get(**opts)

    def earnings(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
            'params': {
                'modules': 'earnings'
            },
        }
        return jsonwebapi.get(**opts)

    def price(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
            'params': {
                'modules': 'price'
            },
        }
        return jsonwebapi.get(**opts)

    def financial_data(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
            'params': {
                'modules': 'financialData'
            },
        }
        return jsonwebapi.get(**opts)

    def quote_type(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v1/finance/quoteType/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
        }
        return jsonwebapi.get(**opts)

    def fundamentals_timeseries(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
            'params': {
                # TODO
                # lang, region, corsDomain, symbol, period1, period2, type, merge, padTimeSeries
            },
        }
        return jsonwebapi.get(**opts)

    def options(ticker):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v7/finance/options/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
        }
        return jsonwebapi.get(**opts)

