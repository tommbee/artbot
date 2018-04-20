class Tweet:
    def __init__(self, artwork=False, text=False):
        self._artist = artwork.artist
        self._image = artwork.image
        self._text = text

    def publish(self):
        print('tweet ' + self._text)