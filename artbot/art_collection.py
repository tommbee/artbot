import collections

Art = collections.namedtuple('Art', ['id', 'artist', 'image'])


class ArtCollection:

    def __init__(self):
        self._collection = []

    def __len__(self):
        return len(self._collection)

    def __getitem__(self, position):
        return self._collection[position]

    def __setitem__(self, key, value):
        self._collection[key] = value
