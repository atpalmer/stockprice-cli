from .folder import Folder
from ..docstore import DocumentStore


class Documents(object):
    def __init__(self, cache_base):
        self._store = DocumentStore(cache_base)

    @property
    def summary(self):
        return self._store.folder(Folder.SUMMARY)

