import requests
from ..decimaljson import json


class _RequestsWrapper(object):
    def __getattr__(self, name):
        def result(*args, **kwargs):
            func = getattr(requests, name)
            response = func(*args, **kwargs)
            response.raise_for_status()
            test = response.text
            return json.loads(test)
        return result


jsonwebapi = _RequestsWrapper()

