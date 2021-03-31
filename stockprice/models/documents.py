from .folder import Folder
from ..docstore import DocumentStore


class Documents(object):
    def __init__(self, cache_base):
        self._store = DocumentStore(cache_base)

    def folder(self, folder):
        return self._store.folder(folder)

    @property
    def chart(self):
        return self.folder(Folder.CHART)

    @property
    def key_statistics(self):
        return self.folder(Folder.KEY_STATISTICS)

    @property
    def profile(self):
        return self.folder(Folder.PROFILE)

    @property
    def financial(self):
        return self.folder(Folder.FINANCIAL)

    @property
    def price(self):
        return self.folder(Folder.PRICE)

    @property
    def summary(self):
        return self.folder(Folder.SUMMARY)


