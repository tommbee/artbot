import os

# Base Settings
BASE_URL = 'https://www.rijksmuseum.nl'
BASE_FOLDER = './downloaded/'
SAVE_IMAGES_IN_FORMAT = '.jpg'

# Request Settings
PAINTINGS_REQUEST_TIMEOUT = 300

# API Settings
TWEET_WAIT_TIME = 720
ART_API_KEY = os.environ['ART_API_KEY']
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
HASH_TAGS = ['#DutchArt', '#Art']
