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

    def _quote_summary_module(ticker, module):
        opts = {
            'url': 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}'.format(
                ticker=ensure_valid_ticker(ticker)),
            'params': {
                'modules': module,
            },
        }
        return jsonwebapi.get(**opts)

    @classmethod
    def summary(cls, ticker):
        return cls._quote_summary_module(ticker, 'defaultKeyStatistics')

    @classmethod
    def summary_profile(cls, ticker):
        return cls._quote_summary_module(ticker, 'summaryProfile')

    @classmethod
    def recommendation_trend(cls, ticker):
        return cls._quote_summary_module(ticker, 'recommendatonTrend')

    @classmethod
    def earnings(cls, ticker):
        return cls._quote_summary_module(ticker, 'earnings')

    @classmethod
    def price(cls, ticker):
        return cls._quote_summary_module(ticker, 'price')

    @classmethod
    def financial_data(cls, ticker):
        return cls._quote_summary_module(ticker, 'financialData')

    @classmethod
    def calendar_events(cls, ticker):
        return cls._quote_summary_module(ticker, 'calendarEvents')

    @classmethod
    def summary_detail(cls, ticker):
        return cls._quote_summary_module(ticker, 'summaryDetail')

    @classmethod
    def esg(cls, ticker):
        return cls._quote_summary_module(ticker, 'esgScores')

    @classmethod
    def upgrade_downgrade_history(cls, ticker):
        return cls._quote_summary_module(ticker, 'upgradeDowngradeHistory')

    @classmethod
    def page_views(cls, ticker):
        return cls._quote_summary_module(ticker, 'pageViews')

    @classmethod
    def financials_template(cls, ticker):
        return cls._quote_summary_module(ticker, 'financialsTemplate')

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

