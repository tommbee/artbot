import requests
import os
import shutil
from . import settings
from artbot.art_collection import ArtCollection
from artbot.art_collection import Art
from random import choice


class RijksMuseum:
    def __init__(self, key=False):
        self._key = key
        self._collection = ArtCollection()

    def prepare(self):
        os.makedirs(settings.BASE_FOLDER, exist_ok=True)
        return self

    def fetch_art_detail(self, artwork=False):
        if artwork:
            try:
                url = '/'.join((settings.BASE_URL, 'api/en/collection/' + artwork.id +
                                '?format=json')) + \
                      ('&key=' + self._key if self._key else '')

                response = requests.get(url, timeout=settings.PAINTINGS_REQUEST_TIMEOUT)
                json_object = response.json()
                return json_object['artObject']

            except Exception as error:
                print('\nError: %s' % str(error))

    def fetch_art(self):
        try:
            url = '/'.join((settings.BASE_URL, 'api/en/collection?format=json&ps=100&imgonly=True&type=painting')) + \
                  ('&key=' + self._key if self._key else '')
            response = requests.get(url, timeout=settings.PAINTINGS_REQUEST_TIMEOUT)
            json_object = response.json()

            for json_art_data in json_object['artObjects']:
                self._collection.append(Art(json_art_data['objectNumber'],
                                            json_art_data['principalOrFirstMaker'],
                                            json_art_data['webImage']['url'],
                                            json_art_data['title'],
                                            ''
                                            ))

            return self.download_artwork()

        except Exception as error:
            print('\nError: %s' % str(error))

    def download_artwork(self):
        # Get random artwork from selection
        artwork = choice(self._collection)
        artwork_obj = Art(*artwork[0:4] +
                           (str(self.fetch_art_detail(artwork)['dating']['sortingDate']),) +
                           artwork[4 + 1:])

        filename = os.path.join(settings.BASE_FOLDER,
                                'art',
                                str(artwork_obj.id) +
                                settings.SAVE_IMAGES_IN_FORMAT)

        try:
            response = requests.get(artwork_obj.image, stream=True, timeout=settings.PAINTINGS_REQUEST_TIMEOUT)

            with open(filename, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)

            return artwork_obj

        except Exception as error:
            print('\nError: %s' % str(error))
            if os.path.exists(filename): os.remove(filename)

