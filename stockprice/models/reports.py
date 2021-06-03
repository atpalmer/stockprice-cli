from .keystatistics import KeyStatistics


ks = KeyStatistics()


def risk(ticker):
    return {
        'ticker': ticker,
        'netDebtToEnterprise': ks.net_debt_to_enterprise_val(ticker),
        'debtToEnterprise': ks.debt_to_enterprise_val(ticker),
        'cashToEnterprise': ks.cash_to_enterprise_val(ticker),
        'beta': ks.beta(ticker),
        'priceToBook': ks.pb(ticker),
        'shortPercent': ks.short_pct(ticker),
    }


def valuation(ticker):
    return {
        'ticker': ticker,
        'EvToEbitda': ks.ev_to_ebitda(ticker),
        'EbitdaToEv': ks.ebitda_to_ev(ticker),
        'trailingPe': ks.trailing_pe(ticker),
        'forwardPe': ks.forward_pe(ticker),
        'priceToSales': ks.price_to_sales(ticker),
        'priceToBook': ks.pb(ticker),
        'earningsGrowth': ks.earnings_growth(ticker),
        'revenueGrowth': ks.revenue_growth(ticker),
        'peg': ks.peg(ticker),
    }


def essentials(ticker):
    return {
        'ticker': ticker,
        'valuation': {
            'ebitdaToEv': ks.ebitda_to_ev(ticker),
            'trailingPe': ks.trailing_pe(ticker),
            'forwardPe': ks.forward_pe(ticker),
            'priceToSales': ks.price_to_sales(ticker),
            'priceToBook': ks.pb(ticker),
            'beta': ks.beta(ticker),
            'roeToPriceBook': ks.roe_pb(ticker),
            'betaAdjRoeToPriceBook': ks.beta_adj_roe_pb(ticker),
        },
        'performance': {
            'earningsGrowth': ks.earnings_growth(ticker),
            'revenueGrowth': ks.revenue_growth(ticker),
            'ROA': ks.roa(ticker),
            'ROE': ks.roe(ticker),
        },
        'balanceSheet': {
            'netDebtToEnterprise': ks.net_debt_to_enterprise_val(ticker),
            'cashToEnterprise': ks.cash_to_enterprise_val(ticker),
            'currentRatio': ks.current_ratio(ticker),
        },
    }

