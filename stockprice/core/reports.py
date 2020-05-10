from . import Folder
from .rawdata import RawData


class Reports(object):
    def __init__(self, cache_base):
        self._raw = RawData(cache_base)

    def _net_debt_to_enterprise_val(self, ticker):
        return (self._debt(ticker) - self._cash(ticker)) / self._enterprise_value(ticker)

    def _debt_to_enterprise_val(self, ticker):
        return self._debt(ticker) / self._enterprise_value(ticker)

    def _cash_to_enterprise_val(self, ticker):
        return self._cash(ticker) / self._enterprise_value(ticker)

    def _cash(self, ticker):
        return self._raw.financial(ticker)['totalCash']

    def _debt(self, ticker):
        return self._raw.financial(ticker)['totalDebt']

    def _enterprise_value(self, ticker):
        return self._raw.summary(ticker)['enterpriseValue']

    def _forward_pe(self, ticker):
        return self._price(ticker) / self._forward_eps(ticker)

    def _trailing_pe(self, ticker):
        return self._price(ticker) / self._trailing_eps(ticker)

    def _short_pct(self, ticker):
        return self._raw.summary(ticker)['shortPercentOfFloat']

    def _pb(self, ticker):
        return self._raw.summary(ticker)['priceToBook']

    def _price_to_sales(self, ticker):
        return self._price(ticker) / self._revenue_per_share(ticker)

    def _ev_to_ebitda(self, ticker):
        return self._raw.summary(ticker)['enterpriseToEbitda']

    def _peg(self, ticker):
        return self._raw.summary(ticker)['pegRatio']

    def _beta(self, ticker):
        return self._raw.summary(ticker)['beta']

    def _trailing_eps(self, ticker):
        return self._raw.summary(ticker)['trailingEps']

    def _forward_eps(self, ticker):
        return self._raw.summary(ticker)['forwardEps']

    def _revenue_per_share(self, ticker):
        return self._raw.financial(ticker)['revenuePerShare']

    def _earnings_growth(self, ticker):
        return self._raw.financial(ticker)['earningsGrowth']

    def _revenue_growth(self, ticker):
        return self._raw.financial(ticker)['revenueGrowth']

    def _price(self, ticker):
        return self._raw.financial(ticker)['currentPrice']

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
            'trailingPe': self._trailing_pe(ticker),
            'forwardPe': self._forward_pe(ticker),
            'priceToSales': self._price_to_sales(ticker),
            'priceToBook': self._pb(ticker),
            'earningsGrowth': self._earnings_growth(ticker),
            'revenueGrowth': self._revenue_growth(ticker),
            'peg': self._peg(ticker),
        }

