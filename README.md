# Dutch Art Bot
Tweet random artwork from Dutch masters.

## Docker
The docker image will install all relevant dependencies and start the Twitter service as a Daemon.
Logs from the supervisor are displayed and updated with any activity.
```
docker-compose up
```

## Change tweet interval
in  `artbot/settings.py` change the following value:
```
TWEET_WAIT_TIME = 1440
```