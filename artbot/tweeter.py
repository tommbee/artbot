import tweepy
from . import settings
import os
from . import settings


class Tweet:
    def __init__(self, artwork=False, text=False):
        self._artwork = artwork
        self._text = text
        self._api = False

    def authenticate(self):
        try:
            auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
            auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
            self._api = tweepy.API(auth)
        except Exception as error:
            print('\nError: %s' % str(error))

    def publish(self):
        self.authenticate()

        if self._api and self._artwork:
            try:
                filename = os.path.join(settings.BASE_FOLDER,
                                        'art',
                                        str(self._artwork.id) +
                                        settings.SAVE_IMAGES_IN_FORMAT)

                hash_tags = ['#'+self._artwork.artist.replace(" ", "")] + settings.HASH_TAGS

                tweet_text = '"' + self._artwork.title + '"\n' + \
                             self._artwork.artist + \
                             ' (' + self._artwork.year + ')' + \
                             '\n' + ' '.join(hash_tags)

                self._api.update_with_media(filename, tweet_text)

            except Exception as error:
                print('\nError: %s' % str(error))
        else:
            print('\nError: Could not authenticate')
