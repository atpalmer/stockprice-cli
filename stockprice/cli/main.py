import os
import click
from ..core.rawdata import RawData
from ..core.rankings import Rankings
from ..core.reports import Reports
from . import util


CACHE_BASE = os.path.join(os.environ['HOME'], '.tickercache')


@click.group()
def main():
    pass


@main.group()
def raw():
    pass


@raw.command()
@click.option('--ticker', required=True, type=str, callback=util.ensure_valid_ticker)
def chart(ticker):
    data = RawData(CACHE_BASE).chart(ticker)
    util.out.json(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=util.ensure_valid_ticker)
def summary(ticker):
    data = RawData(CACHE_BASE).summary(ticker)
    util.out.json(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=util.ensure_valid_ticker)
def profile(ticker):
    data = RawData(CACHE_BASE).profile(ticker)
    util.out.json(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=util.ensure_valid_ticker)
def financial(ticker):
    data = RawData(CACHE_BASE).financial(ticker)
    util.out.json(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=util.ensure_valid_ticker)
def price(ticker):
    data = RawData(CACHE_BASE).price(ticker)
    util.out.json(data)


@main.group()
def report():
    pass


@report.group()
def rank():
    pass


@report.command()
@click.option('--ticker', required=True, type=str, callback=util.ensure_valid_ticker)
def risk(ticker):
    data = Reports(cache_base=CACHE_BASE).risk(ticker)
    util.out.json(data)


@report.command()
@click.option('--ticker', required=True, type=str, callback=util.ensure_valid_ticker)
def valuation(ticker):
    data = Reports(cache_base=CACHE_BASE).valuation(ticker)
    util.out.json(data)


@rank.command()
def pe():
    '''Price/Earnings'''
    data = Rankings(cache_base=CACHE_BASE).pe()
    util.out.json(data)


@rank.command()
def ev():
    '''EV/EBITDA'''
    data = Rankings(cache_base=CACHE_BASE).ev_to_ebitda()
    util.out.json(data)


@rank.command()
def peg():
    '''PEG ratio'''
    data = Rankings(cache_base=CACHE_BASE).peg()
    util.out.json(data)


@rank.command()
def growth():
    '''Quarterly Earnings Growth'''
    data = Rankings(cache_base=CACHE_BASE).growth()
    util.out.json(data)
