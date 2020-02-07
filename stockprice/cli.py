import json
import os
import click
from .core.rawdata import RawData
from .core.rankings import Rankings
from . import validation


CACHE_BASE = os.path.join(os.environ['HOME'], '.tickercache')


def validate_ticker(ctx, param, value):
    ticker = value.upper()
    try:
        validation.ensure_valid_ticker(ticker)
    except:
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
    data = RawData(CACHE_BASE).chart(ticker)
    out.json(data)


@main.command()
@click.option('--ticker', required=True, type=str, callback=validate_ticker)
def summary(ticker):
    data = RawData(CACHE_BASE).summary(ticker)
    out.json(data)


@main.group()
def rank():
    pass


@rank.command()
def pe():
    data = Rankings(cache_base=CACHE_BASE).pe()
    out.json(data)


@rank.command()
def peg():
    data = Rankings(cache_base=CACHE_BASE).peg()
    out.json(data)


@rank.command()
def growth():
    data = Rankings(cache_base=CACHE_BASE).growth()
    out.json(data)
