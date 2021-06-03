import click
from ..models.rawdata import RawData
from ..models import rankings
from ..models import reports
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
    data = RawData().chart(ticker)
    pprint(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def keystats(ticker):
    data = RawData().key_statistics(ticker)
    pprint(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def profile(ticker):
    data = RawData().profile(ticker)
    pprint(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def financial(ticker):
    data = RawData().financial(ticker)
    pprint(data)


@raw.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def price(ticker):
    data = RawData().price(ticker)
    pprint(data)


@main.group()
def report():
    pass


@report.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def risk(ticker):
    pprint(reports.risk(ticker))


@report.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def valuation(ticker):
    pprint(reports.valuation(ticker))


@report.command()
@click.option('--ticker', required=True, type=str, callback=ensure_valid_ticker)
def essentials(ticker):
    pprint(reports.essentials(ticker))


@main.group()
def rank():
    pass


@rank.command()
def pe():
    '''Price/Earnings'''
    pprint(rankings.pe())


@rank.command()
def ev():
    '''EV/EBITDA'''
    pprint(rankings.ev_to_ebitda())


@rank.command()
def peg():
    '''PEG ratio'''
    pprint(rankings.peg())


@rank.command()
def growth():
    '''Quarterly Earnings Growth'''
    pprint(rankings.growth())

