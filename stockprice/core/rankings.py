from . import Folder
from .rawdata import RawData


def _sortby(contents, keys, *, sortkey=None, reverse=False):
    if sortkey is None:
        sortkey = keys[0]
    items = (
        {
            'filename': data.filename,
            **{key: data.contents['quoteSummary']['result'][0]['defaultKeyStatistics'][key].get('raw') for key in keys},
        }
        for data in contents)
    return sorted(
        (item for item in items if item[sortkey] is not None),
        key=lambda x: x[sortkey],
        reverse=reverse)


class Rankings(object):
    def __init__(self, cache_base):
        self._raw = RawData(cache_base)

    def pe(self):
        return _sortby(
            self._raw.documents(Folder.SUMMARY),
            ['forwardPE', 'earningsQuarterlyGrowth'],
            sortkey='forwardPE')

    def ev_to_ebitda(self):
        return _sortby(
            self._raw.documents(Folder.SUMMARY),
            ['enterpriseToEbitda', 'forwardPE'],
            sortkey='enterpriseToEbitda')

    def peg(self):
        return _sortby(
            self._raw.documents(Folder.SUMMARY),
            ['pegRatio', 'forwardPE'],
            sortkey='pegRatio')

    def growth(self):
        return _sortby(
            self._raw.documents(Folder.SUMMARY),
            ['earningsQuarterlyGrowth'],
            sortkey='earningsQuarterlyGrowth',
            reverse=True)

