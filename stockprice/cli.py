import json
import os
import click
from . import rawdata
from . import aggregates
from . import validation


CACHE_BASE = os.path.join(os.environ['HOME'], '.tickercache')


def validate_ticker(ctx, param, value):
    ticker = value.upper()
    if not validation.ticker_is_valid(ticker):
        raise click.BadParameter(ticker)
    return ticker


class out(object):
    def json(data):
        print(json.dumps(data, indent=2))


@click.group()
def main():
    pass


@main.command()
@click.option('--ticker', required=True, type=str, callback=validate_ticker)
def chart(ticker):
    args = {
        'ticker': ticker,
        'cache_base': CACHE_BASE,
    }
    data = rawdata.chart(**args)
    out.json(data)


@main.command()
@click.option('--ticker', required=True, type=str, callback=validate_ticker)
def summary(ticker):
    args = {
        'ticker': ticker,
        'cache_base': CACHE_BASE,
    }
    data = rawdata.summary(**args)
    out.json(data)


@main.command()
def pe():
    data = aggregates.pe(cache_base=CACHE_BASE)
    out.json(data)
