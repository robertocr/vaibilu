# -*- coding: utf-8 -*-
from twython import TwythonStreamer
from router import router
from twitter_service import send_tweet

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            user = data['user']['screen_name']
            message = data['text'].encode('utf-8')
            status_id = data['id']
            response = router(message, "twitter")
            # print response
            response = '@' + user + ' ' + response
            send_tweet(response[:140], status_id)

    def on_error(self, status_code, data):
        print status_code
