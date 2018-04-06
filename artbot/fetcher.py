import requests
import os
import random
import shutil
from . import settings


class RijksMuseum:
    def __init__(self, additional=False, key=False):
        self.text = additional
        self.key = key

    def prepare(self):
        os.makedirs(settings.BASE_FOLDER, exist_ok=True)
        return self

    def fetch_art(self):
        try:
            url = '/'.join((settings.BASE_URL, 'api/en/collection?format=json')) + ('&key=' + self.key if self.key else '')
            response = requests.get(url, timeout=settings.PAINTINGS_REQUEST_TIMEOUT)
            json_object = response.json()
            object_count = len(json_object['artObjects'])
            random_key = random.randint(0, object_count)
            image = json_object['artObjects'][random_key]
            self.download_artwork(image)

        except Exception as error:
            print('\nError %s' % str(error))

    def download_artwork(self, artwork):
        artwork_url = artwork['webImage']['url']
        filename = os.path.join(settings.BASE_FOLDER,
                                'images',
                                str(artwork['objectNumber']) +
                                settings.SAVE_IMAGES_IN_FORMAT)

        try:
            response = requests.get(artwork_url, stream=True, timeout=settings.PAINTINGS_REQUEST_TIMEOUT)

            with open(filename, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)

        except Exception as error:
            print('\nError %s' % str(error))
            if os.path.exists(filename): os.remove(filename)
