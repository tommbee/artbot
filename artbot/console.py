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

        self._selected_art = False
        self.parser = t

    def parse(self):
        elapsed = time.time()
        try:
            args = self.parser.parse_args()
            if args.key is None:
                args.key = settings.ART_API_KEY

            if not hasattr(args, 'func'):
                return self.main(args)

            args.func(args)
        except KeyboardInterrupt:
            print('\ncanceled')
        else:
            print('\ndone (%.2f sec)' % (time.time() - elapsed))

    def main(self, args):
        return self.fetch(args).tweet(args)

    def fetch(self, args):
        f = fetcher.RijksMuseum(key=args.key)
        f.prepare()
        self._selected_art = f.fetch_art()
        return self

    def tweet(self, args):
        text = args.additional
        tweeter.Tweet(self._selected_art, text).publish()
        return self


def main():
    Console().parse()
