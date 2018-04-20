import argparse
import time
from . import settings, fetcher, tweeter


class Console:
    def __init__(self):
        t = argparse.ArgumentParser(
            description='Tweet piece of art')
        t.add_argument('--additional',
                       default=None, help='Additional text to appear in the tweet')
        t.add_argument('--key',
                       default=None, help='The API key')

        self.parser = t

    def interpret(self):
        elapsed = time.time()
        try:
            args = self.parser.parse_args()

            if not hasattr(args, 'func'):
                return self.main(args)

            args.func(args)
        except KeyboardInterrupt:
            print('\ncanceled')
        else:
            print('\ndone (%.2f sec)' % (time.time() - elapsed))

    def main(self, args):
        return self.fetch(args).tweet()

    def fetch(self, args):
        f = fetcher.RijksMuseum(additional=args.additional, key=args.key)
        f.prepare()
        f.fetch_art()
        return self

    def tweet(self):
        # get artwork
        artwork = []
        tweeter.Tweet(artwork).publish()
        return self


def main():
    Console().interpret()
