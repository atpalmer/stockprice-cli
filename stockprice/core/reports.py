from . import Folder
from .rawdata import RawData


class Reports(object):
    def __init__(self, cache_base):
        self._raw = RawData(cache_base)

    def _net_debt_to_enterprise_val(self, ticker):
        summary = self._raw.summary(ticker)
        financial = self._raw.financial(ticker)
        ev = summary['enterpriseValue']
        cash = financial['totalCash']
        debt = financial['totalDebt']
        return (debt - cash) / ev

    def _short_pct(self, ticker):
        summary = self._raw.summary(ticker)
        return summary['shortPercentOfFloat']

    def _pb(self, ticker):
        summary = self._raw.summary(ticker)
        return summary['priceToBook']

    def _beta(self, ticker):
        summary = self._raw.summary(ticker)
        return summary['beta']

    def risk(self, ticker):
        return {
            'ticker': ticker,
            'netDebtToEnterprise': self._net_debt_to_enterprise_val(ticker),
            'beta': self._beta(ticker),
            'priceToBook': self._pb(ticker),
            'shortPercent': self._short_pct(ticker),
        }

