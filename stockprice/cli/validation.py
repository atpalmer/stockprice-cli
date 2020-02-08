import re


def _ticker_is_valid(ticker):
    return True if re.match(r'[A-Z]+', ticker) else False


def ensure_valid_ticker(ticker):
    if not _ticker_is_valid(ticker):
        raise ValueError(f'Symbol "{ticker}" is not a valid ticker')