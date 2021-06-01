from ..config import CACHE_BASE
from ..docstore import DocumentStore


class Documents(object):
    def __init__(self, cache_base=CACHE_BASE):
        self._store = DocumentStore(cache_base)

    def folder(self, folder):
        return self._store.folder(folder)

    @property
    def chart(self):
        return self.folder('chart')

    @property
    def key_statistics(self):
        return self.folder('keystats')

    @property
    def profile(self):
        return self.folder('profile')

    @property
    def financial(self):
        return self.folder('financial')

    @property
    def price(self):
        return self.folder('price')

    @property
    def summary(self):
        return self.folder('summary')

