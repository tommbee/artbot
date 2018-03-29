import argparse
import time
from . import settings, fetcher


class Console:
    def __init__(self):
        t = argparse.ArgumentParser(
            description='Tweet piece of art')
        t.add_argument('--additional',
                       default=None, help='Additional text to appear in the tweet')
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
        #return self.fetch(args).convert(args)
        return self.fetch(args)


    def fetch(self, args):
        f = fetcher.Artsy(additional=args.additional)
        f.prepare()
        f.fetch_art()
        return self


def main():
    Console().interpret()
