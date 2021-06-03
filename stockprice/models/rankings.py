from ._schemas import schemas


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


def pe():
    return _sortby(
        schemas.summary.documents(),
        ['forwardPE', 'earningsQuarterlyGrowth'],
        sortkey='forwardPE')


def ev_to_ebitda():
    return _sortby(
        schemas.summary.documents(),
        ['enterpriseToEbitda', 'forwardPE'],
        sortkey='enterpriseToEbitda')


def peg():
    return _sortby(
        schemas.summary.documents(),
        ['pegRatio', 'forwardPE'],
        sortkey='pegRatio')


def growth():
    return _sortby(
        schemas.summary.documents(),
        ['earningsQuarterlyGrowth'],
        sortkey='earningsQuarterlyGrowth',
        reverse=True)

