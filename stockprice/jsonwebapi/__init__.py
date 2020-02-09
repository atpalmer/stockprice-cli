import requests


class _RequestsWrapper(object):
    def __getattr__(self, name):
        def result(*args, **kwargs):
            func = getattr(requests, name)
            response = func(*args, **kwargs)
            response.raise_for_status()
            return response.json()
        return result


jsonwebapi = _RequestsWrapper()

