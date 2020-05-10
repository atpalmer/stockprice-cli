from . import Folder
from .rawdata import RawData


def rescue(*, on_fail=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                return on_fail
        return wrapper
    return decorator


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

    def _ebitda_to_ev(self, ticker):
        return 1 / self._ev_to_ebitda(ticker)

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

    def _roa(self, ticker):
        return self._raw.financial(ticker)['returnOnAssets']

    def _roe(self, ticker):
        return self._raw.financial(ticker)['returnOnEquity']

    def _quick_ratio(self, ticker):
        return self._raw.financial(ticker)['quickRatio']

    def _current_ratio(self, ticker):
        return self._raw.financial(ticker)['currentRatio']

    @rescue(on_fail=None)
    def _roe_pb(self, ticker):
        return self._roe(ticker) / self._pb(ticker)

    @rescue(on_fail=None)
    def _beta_adj_roe_pb(self, ticker):
        return self._roe_pb(ticker) / self._beta(ticker)

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
            'EbitdaToEv': self._ebitda_to_ev(ticker),
            'trailingPe': self._trailing_pe(ticker),
            'forwardPe': self._forward_pe(ticker),
            'priceToSales': self._price_to_sales(ticker),
            'priceToBook': self._pb(ticker),
            'earningsGrowth': self._earnings_growth(ticker),
            'revenueGrowth': self._revenue_growth(ticker),
            'peg': self._peg(ticker),
        }

    def essentials(self, ticker):
        return {
            'ticker': ticker,
            'EbitdaToEv': self._ebitda_to_ev(ticker),
            'trailingPe': self._trailing_pe(ticker),
            'forwardPe': self._forward_pe(ticker),
            'priceToSales': self._price_to_sales(ticker),
            'priceToBook': self._pb(ticker),
            'earningsGrowth': self._earnings_growth(ticker),
            'revenueGrowth': self._revenue_growth(ticker),
            'netDebtToEnterprise': self._net_debt_to_enterprise_val(ticker),
            'cashToEnterprise': self._cash_to_enterprise_val(ticker),
            'beta': self._beta(ticker),
            'ROA': self._roa(ticker),
            'ROE': self._roe(ticker),
            'roeToPriceBook': self._roe_pb(ticker),
            'betaAdjRoeToPriceBook': self._beta_adj_roe_pb(ticker),
            'currentRatio': self._current_ratio(ticker),
        }

