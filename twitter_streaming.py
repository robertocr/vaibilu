# -*- coding: utf-8 -*-
from twython import Twython
from twython import TwythonStreamer
from _config import twitter_streaming_conf as config
from twitter_mystreamer import MyStreamer

def tstream():
  while True:
    stream = MyStreamer(config.APP_KEY, config.APP_SECRET, config.OAUTH_TOKEN, config.OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track='@vaibilu')
#if __name__ == "__main__":
#    app.run()

from twitter_streaming import tstream