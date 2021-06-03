from . import _rawdata


def chart(ticker):
    return _rawdata.chart(ticker)


def key_statistics(ticker):
    return _rawdata.key_statistics(ticker)


def profile(ticker):
    return _rawdata.profile(ticker)


def financial(ticker):
    return _rawdata.financial(ticker)


def price(ticker):
    return _rawdata.price(ticker)

