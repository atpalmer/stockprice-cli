import re
import click
from ..decimaljson import json


def ensure_valid_ticker(ctx, param, value):
    ticker = value.upper()
    if re.match(r'[A-Z]+', ticker) is None:
        raise click.BadParameter(ticker)
    return ticker


def pprint(data):
    print(json.dumps(data, indent=2))

