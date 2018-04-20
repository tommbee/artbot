import requests
import os
import random
import shutil
from . import settings
import artbot.art_collection
from random import choice


class RijksMuseum:
    def __init__(self, key=False):
        self._key = key
        self._collection = artbot.art_collection

    def prepare(self):
        os.makedirs(settings.BASE_FOLDER, exist_ok=True)
        return self

    def fetch_art(self):
        try:
            url = '/'.join((settings.BASE_URL, 'api/en/collection?format=json')) + ('&key=' + self._key if self._key else '')
            response = requests.get(url, timeout=settings.PAINTINGS_REQUEST_TIMEOUT)
            json_object = response.json()

            for json_art_data in json_object['artObjects']:
                self._collection.append(json_art_data['objectNumber'], json_art_data['principalOrFirstMaker'],
                                        json_art_data['webImage']['url'])

            self.download_artwork()

        except Exception as error:
            print('\nError %s' % str(error))

    def download_artwork(self):
        # Get random artwork from selection
        artwork = choice(self._collection)

        filename = os.path.join(settings.BASE_FOLDER,
                                'images',
                                str(artwork.id) +
                                settings.SAVE_IMAGES_IN_FORMAT)

        try:
            response = requests.get(artwork.image, stream=True, timeout=settings.PAINTINGS_REQUEST_TIMEOUT)

            with open(filename, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)

        except Exception as error:
            print('\nError %s' % str(error))
            if os.path.exists(filename): os.remove(filename)
