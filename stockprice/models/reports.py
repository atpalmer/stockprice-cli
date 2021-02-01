from .rawdata import RawData
from .keystatistics import KeyStatistics


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

