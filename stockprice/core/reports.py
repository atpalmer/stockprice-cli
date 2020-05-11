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


class KeyStatistics(object):
    def __init__(self, raw):
        self._raw = raw

    def net_debt_to_enterprise_val(self, ticker):
        return (self.debt(ticker) - self.cash(ticker)) / self.enterprise_value(ticker)

    def debt_to_enterprise_val(self, ticker):
        return self.debt(ticker) / self.enterprise_value(ticker)

    def cash_to_enterprise_val(self, ticker):
        return self.cash(ticker) / self.enterprise_value(ticker)

    def cash(self, ticker):
        return self._raw.financial(ticker)['totalCash']

    def debt(self, ticker):
        return self._raw.financial(ticker)['totalDebt']

    def enterprise_value(self, ticker):
        return self._raw.key_statistics(ticker)['enterpriseValue']

    def forward_pe(self, ticker):
        return self.price(ticker) / self.forward_eps(ticker)

    def trailing_pe(self, ticker):
        return self.price(ticker) / self.trailing_eps(ticker)

    def short_pct(self, ticker):
        return self._raw.key_statistics(ticker)['shortPercentOfFloat']

    def pb(self, ticker):
        return self._raw.key_statistics(ticker)['priceToBook']

    def price_to_sales(self, ticker):
        return self.price(ticker) / self.revenue_per_share(ticker)

    def ev_to_ebitda(self, ticker):
        return self._raw.key_statistics(ticker)['enterpriseToEbitda']

    @rescue(on_fail=None)
    def ebitda_to_ev(self, ticker):
        return 1 / self.ev_to_ebitda(ticker)

    def peg(self, ticker):
        return self._raw.key_statistics(ticker)['pegRatio']

    def beta(self, ticker):
        return self._raw.key_statistics(ticker)['beta']

    def trailing_eps(self, ticker):
        return self._raw.key_statistics(ticker)['trailingEps']

    def forward_eps(self, ticker):
        return self._raw.key_statistics(ticker)['forwardEps']

    def revenue_per_share(self, ticker):
        return self._raw.financial(ticker)['revenuePerShare']

    def earnings_growth(self, ticker):
        return self._raw.financial(ticker)['earningsGrowth']

    def revenue_growth(self, ticker):
        return self._raw.financial(ticker)['revenueGrowth']

    def price(self, ticker):
        return self._raw.financial(ticker)['currentPrice']

    def roa(self, ticker):
        return self._raw.financial(ticker)['returnOnAssets']

    def roe(self, ticker):
        return self._raw.financial(ticker)['returnOnEquity']

    def quick_ratio(self, ticker):
        return self._raw.financial(ticker)['quickRatio']

    def current_ratio(self, ticker):
        return self._raw.financial(ticker)['currentRatio']

    @rescue(on_fail=None)
    def roe_pb(self, ticker):
        return self.roe(ticker) / self.pb(ticker)

    @rescue(on_fail=None)
    def beta_adj_roe_pb(self, ticker):
        return self.roe_pb(ticker) / self.beta(ticker)


class Reports(object):
    def __init__(self, cache_base):
        self._ks = KeyStatistics(RawData(cache_base))

    def risk(self, ticker):
        return {
            'ticker': ticker,
            'netDebtToEnterprise': self._ks.net_debt_to_enterprise_val(ticker),
            'debtToEnterprise': self._ks.debt_to_enterprise_val(ticker),
            'cashToEnterprise': self._ks.cash_to_enterprise_val(ticker),
            'beta': self._ks.beta(ticker),
            'priceToBook': self._ks.pb(ticker),
            'shortPercent': self._ks.short_pct(ticker),
        }

    def valuation(self, ticker):
        return {
            'ticker': ticker,
            'EvToEbitda': self._ks.ev_to_ebitda(ticker),
            'EbitdaToEv': self._ks.ebitda_to_ev(ticker),
            'trailingPe': self._ks.trailing_pe(ticker),
            'forwardPe': self._ks.forward_pe(ticker),
            'priceToSales': self._ks.price_to_sales(ticker),
            'priceToBook': self._ks.pb(ticker),
            'earningsGrowth': self._ks.earnings_growth(ticker),
            'revenueGrowth': self._ks.revenue_growth(ticker),
            'peg': self._ks.peg(ticker),
        }

    def essentials(self, ticker):
        return {
            'ticker': ticker,
            'EbitdaToEv': self._ks.ebitda_to_ev(ticker),
            'trailingPe': self._ks.trailing_pe(ticker),
            'forwardPe': self._ks.forward_pe(ticker),
            'priceToSales': self._ks.price_to_sales(ticker),
            'priceToBook': self._ks.pb(ticker),
            'earningsGrowth': self._ks.earnings_growth(ticker),
            'revenueGrowth': self._ks.revenue_growth(ticker),
            'netDebtToEnterprise': self._ks.net_debt_to_enterprise_val(ticker),
            'cashToEnterprise': self._ks.cash_to_enterprise_val(ticker),
            'beta': self._ks.beta(ticker),
            'ROA': self._ks.roa(ticker),
            'ROE': self._ks.roe(ticker),
            'roeToPriceBook': self._ks.roe_pb(ticker),
            'betaAdjRoeToPriceBook': self._ks.beta_adj_roe_pb(ticker),
            'currentRatio': self._ks.current_ratio(ticker),
        }

