import click
from ..config import CACHE_BASE
from ..models.rawdata import RawData
from ..models.rankings import Rankings
from ..models.reports import Reports
from .util import ensure_valid_ticker, pprint


@click.group()
def main():
    pass


@main.group()
def raw():
    pass


@raw.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def chart(ticker):
    data = RawData(CACHE_BASE).chart(ticker)
    pprint(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def keystats(ticker):
    data = RawData(CACHE_BASE).key_statistics(ticker)
    pprint(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def profile(ticker):
    data = RawData(CACHE_BASE).profile(ticker)
    pprint(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def financial(ticker):
    data = RawData(CACHE_BASE).financial(ticker)
    pprint(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def price(ticker):
    data = RawData(CACHE_BASE).price(ticker)
    pprint(data)


@main.group()
def report():
    pass


@report.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def risk(ticker):
    data = Reports(cache_base=CACHE_BASE).risk(ticker)
    pprint(data)


@report.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def valuation(ticker):
    data = Reports(cache_base=CACHE_BASE).valuation(ticker)
    pprint(data)


@report.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def essentials(ticker):
    data = Reports(cache_base=CACHE_BASE).essentials(ticker)
    pprint(data)


@main.group()
def rank():
    pass


@rank.command()
def pe():
    '''Price/Earnings'''
    data = Rankings(cache_base=CACHE_BASE).pe()
    pprint(data)


@rank.command()
def ev():
    '''EV/EBITDA'''
    data = Rankings(cache_base=CACHE_BASE).ev_to_ebitda()
    pprint(data)


@rank.command()
def peg():
    '''PEG ratio'''
    data = Rankings(cache_base=CACHE_BASE).peg()
    pprint(data)


@rank.command()
def growth():
    '''Quarterly Earnings Growth'''
    data = Rankings(cache_base=CACHE_BASE).growth()
    pprint(data)

