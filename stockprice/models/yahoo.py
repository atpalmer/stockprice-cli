from datetime import datetime, timezone


class Chart(object):
    def __init__(self, data):
        self._data = data

    def get_items(self):
        unwrapped_data = self._data['chart']['result'][0]
        indicators = unwrapped_data['indicators']['quote'][0]
        timestamps = (
            datetime.fromtimestamp(ts).replace(tzinfo=timezone.utc).isoformat()
            for ts in unwrapped_data['timestamp'])
        return [
            {k: v  for k, v in zip((*indicators.keys(), 'timestamp'), row)}
            for row in zip(*indicators.values(), timestamps)
        ]

