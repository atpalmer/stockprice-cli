'''
This is a placeholder for more sophisticated treatment of numeric values.

If we want to work with decimal values, we need safe conversion from JSON
and, most likely, some cacheable format with a rich type system.

If this all gets too complicated, working with floats may end up being
the right solution.
'''
from decimal import Decimal
from functools import partial
import json as _json


class _JSONEncoder(_json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)


class _Json(object):
    def __getattr__(self, name):
        return getattr(_json, name)

    load = partial(_json.load, parse_float=Decimal)
    loads = partial(_json.loads, parse_float=Decimal)
    dump = partial(_json.dump, cls=_JSONEncoder)
    dumps = partial(_json.dumps, cls=_JSONEncoder)


json = _Json()
