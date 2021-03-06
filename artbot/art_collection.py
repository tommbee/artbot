import collections

Art = collections.namedtuple('Art', ['id', 'artist', 'image', 'title', 'year'])


class ArtCollection:

    def append(self, value):
        self._collection.append(value)

    def __init__(self):
        self._collection = []

    def __len__(self):
        return len(self._collection)

    def __getitem__(self, position):
        return self._collection[position]

    def __setitem__(self, key, value):
        self._collection[key] = value
