# -*- coding: utf-8 -*-
#
# Copyright 2018 Amir Hadifar. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import json

import requests
import time
from tweepy import StreamListener
from sys import stderr
from app import config


class Listener(StreamListener):
    ENDPOINT = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"

    def on_data(self, data):
        all_data = json.loads(data)
        print(all_data)
        try:
            text = all_data['text']
            user = all_data["user"]["id"]
            user_id = all_data["user"]["screen_name"]
            tweet_id = all_data["id_str"]
            if not text.startswith("RT") and str(user) == "2324847996":
                tweet = "https://twitter.com/" + user_id + "/status/" + tweet_id
                req = self.ENDPOINT.format(config.TELEGRAM_BOT_API_KEY, config.TELEGRAM_CHANNEL_NAME, tweet)
                requests.get(req)
        except:
            pass

        return True

    def on_disconnect(self, notice):
        # Print timeout message
        print(stderr, "Disconnect...")

        # Wait 10 seconds
        time.sleep(10)
        return

    def on_timeout(self):
        # Print timeout message
        print(stderr, "Timeout...")

        # Wait 10 seconds
        time.sleep(10)

        # Return nothing
        return

    def on_error(self, status):
        print ('error with status code' + str(status))
