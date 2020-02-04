import json
import os
import click
from . import core
from . import validation


CACHE_BASE = os.path.join(os.environ['HOME'], '.tickercache')


def validate_ticker(ctx, param, value):
    ticker = value.upper()
    if not validation.ticker_is_valid(ticker):
        raise click.BadParameter(ticker)
    return ticker


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
    data = core.get_chart_data(**args)
    print(json.dumps(data, indent=2))


@main.command()
@click.option('--ticker', required=True, type=str, callback=validate_ticker)
def summary(ticker):
    args = {
        'ticker': ticker,
    }
    data = core.get_summary(**args)
    print(json.dumps(data, indent=2))
