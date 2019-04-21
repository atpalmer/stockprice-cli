import json
import os
import click
from .core import get
from . import validation


def validate_ticker(ctx, param, value):
    ticker = value.upper()
    if not validation.ticker_is_valid(ticker):
        raise click.BadParameter(ticker)
    return ticker


@click.command()
@click.option('--ticker', required=True, type=str, callback=validate_ticker)
def main(ticker):
    args = {
        'ticker': ticker,
        'cache_base': os.path.join(os.environ['HOME'], '.tickercache'),
    }
    data = get(**args)
    print(json.dumps(data, indent=2))
