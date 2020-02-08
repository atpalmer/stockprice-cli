import json
import re
import click


def ensure_valid_ticker(ctx, param, value):
    ticker = value.upper()
    if re.match(r'[A-Z]+', ticker) is None:
        raise click.BadParameter(ticker)
    return ticker


class out(object):
    def json(data):
        print(json.dumps(data, indent=2))

