from ..docstore import DocumentStore
from . import Folder


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
        self._summary_store = DocumentStore.from_path_segments(cache_base, Folder.SUMMARY)

    def pe(self):
        return _sortby(
            self._summary_store.documents(),
            ['forwardPE', 'earningsQuarterlyGrowth'],
            sortkey='forwardPE')

    def peg(self):
        return _sortby(
            self._summary_store.documents(),
            ['pegRatio', 'forwardPE'],
            sortkey='pegRatio')

    def growth(self):
        return _sortby(
            self._summary_store.documents(),
            ['earningsQuarterlyGrowth'],
            sortkey='earningsQuarterlyGrowth',
            reverse=True)

