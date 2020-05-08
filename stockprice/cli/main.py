import os
import click
from ..core.rawdata import RawData
from ..core.rankings import Rankings
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


@main.group()
def report():
    pass


@report.group()
def rank():
    pass


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
