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

    def _debt_to_enterprise_val(self, ticker):
        summary = self._raw.summary(ticker)
        financial = self._raw.financial(ticker)
        ev = summary['enterpriseValue']
        debt = financial['totalDebt']
        return debt / ev

    def _cash_to_enterprise_val(self, ticker):
        summary = self._raw.summary(ticker)
        financial = self._raw.financial(ticker)
        ev = summary['enterpriseValue']
        cash = financial['totalCash']
        return cash / ev

    def _short_pct(self, ticker):
        summary = self._raw.summary(ticker)
        return summary['shortPercentOfFloat']

    def _pb(self, ticker):
        summary = self._raw.summary(ticker)
        return summary['priceToBook']

    def _fwd_pe(self, ticker):
        summary = self._raw.summary(ticker)
        return summary['forwardPE']

    def _price_to_sales(self, ticker):
        summary = self._raw.summary(ticker)
        return summary['priceToSalesTrailing12Months']

    def _ev_to_ebitda(self, ticker):
        summary = self._raw.summary(ticker)
        return summary['enterpriseToEbitda']

    def _peg(self, ticker):
        summary = self._raw.summary(ticker)
        return summary['pegRatio']

    def _beta(self, ticker):
        summary = self._raw.summary(ticker)
        return summary['beta']

    def risk(self, ticker):
        return {
            'ticker': ticker,
            'netDebtToEnterprise': self._net_debt_to_enterprise_val(ticker),
            'debtToEnterprise': self._debt_to_enterprise_val(ticker),
            'cashToEnterprise': self._cash_to_enterprise_val(ticker),
            'beta': self._beta(ticker),
            'priceToBook': self._pb(ticker),
            'shortPercent': self._short_pct(ticker),
        }

    def valuation(self, ticker):
        return {
            'ticker': ticker,
            'EvToEbitda': self._ev_to_ebitda(ticker),
            'priceToBook': self._pb(ticker),
            'forwardPe': self._fwd_pe(ticker),
            'priceToSales': self._price_to_sales(ticker),
            'peg': self._peg(ticker),
        }

