import requests
import os
from . import settings


class Artsy:
    def __init__(self, additional=False):
        self.text = additional

    def prepare(self):
        os.makedirs(settings.BASE_FOLDER, exist_ok=True)
        return self

    def fetch_art(self):
        url = '/'.join((settings.BASE_URL, 'api/artworks'))
        print(url)
        response = requests.get(url)
        print(response)
