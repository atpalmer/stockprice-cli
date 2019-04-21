import re


def ticker_is_valid(ticker):
    return True if re.match(r'[A-Z]+', ticker) else False


def is_valid_filename(ticker):
    return True if re.match(r'[A-Z]+', ticker) else False
