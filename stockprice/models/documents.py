from .folder import Folder


class Documents(object):
    def __init__(self, rawdata):
        self._raw = rawdata

    def summary(self):
        return self._raw.documents(Folder.SUMMARY)

