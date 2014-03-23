# -*- coding: utf-8 -*-
from twython import Twython
from _config import twitter_streaming_conf as config

def send_tweet(message,status_id):
  twitter = Twython(config.APP_KEY, config.APP_SECRET, config.OAUTH_TOKEN, config.OAUTH_TOKEN_SECRET)
  try:
    twitter.update_status(status=message, in_reply_to_status_id=status_id)
  except:
    return False
  return True
