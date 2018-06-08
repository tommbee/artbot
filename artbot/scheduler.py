from artbot.console import main
from . import settings
import schedule
import time


class Scheduler:
    def __init__(self):
        self._time_interval = settings.TWEET_WAIT_TIME

    def start(self):
        main()
        # schedule.every(self._time_interval).minutes.do(main)
        #
        # while 1:
        #     schedule.run_pending()
        #     time.sleep(1)


def start():
    Scheduler().start()
