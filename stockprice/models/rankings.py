from .documents import Documents


def _sortby(docs, keys, *, sortkey=None, reverse=False):
    if sortkey is None:
        sortkey = keys[0]
    items = (
        {
            'filename': doc.filename,
            **{key: doc.contents['quoteSummary']['result'][0]['defaultKeyStatistics'][key].get('raw') for key in keys},
        }
        for doc in docs)
    return sorted(
        (item for item in items if item[sortkey] is not None),
        key=lambda x: x[sortkey],
        reverse=reverse)


class Rankings(object):
    def __init__(self):
        self._docs = Documents()

    def pe(self):
        return _sortby(
            self._docs.summary.documents(),
            ['forwardPE', 'earningsQuarterlyGrowth'],
            sortkey='forwardPE')

    def ev_to_ebitda(self):
        return _sortby(
            self._docs.summary.documents(),
            ['enterpriseToEbitda', 'forwardPE'],
            sortkey='enterpriseToEbitda')

    def peg(self):
        return _sortby(
            self._docs.summary.documents(),
            ['pegRatio', 'forwardPE'],
            sortkey='pegRatio')

    def growth(self):
        return _sortby(
            self._docs.summary.documents(),
            ['earningsQuarterlyGrowth'],
            sortkey='earningsQuarterlyGrowth',
            reverse=True)

