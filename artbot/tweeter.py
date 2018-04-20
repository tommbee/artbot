class Tweet:
    def __init__(self, artwork):
        self.artist = artwork.artist
        self.image = artwork.image
        self.text = artwork.text

    def publish(self):
        print('tweet ' + self.text)