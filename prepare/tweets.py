# -*- coding: utf-8 -*-
import configparser
import requests
import json
import sys
import gzip
from requests_oauthlib import OAuth1
import utils

"""
prepare twitter_config.ini file before executing the program.

[consumer]
key = (your consumer key)
secret = (your consumer secret key)
[access]
token =  (your access token)
secret = (your secret token)

You have to create twitter account and application from here.
https://apps.twitter.com/
"""

TWITTER_INI = "twitter_config.ini"
TWITTER_TXT = "tweets.txt.gz"


def main(tweet_count=10000):
    tweets = []
    twitter = read_ini()
    meter_size = 10

    for tweet in twitter.streaming():
        if "text" not in tweet:
            continue
        tweets.append(tweet["text"])

        progress = round(len(tweets) * 100 / tweet_count)
        meter = ("#" * (progress // meter_size)).ljust(meter_size, "-")
        sys.stdout.write("\r|{0}|  {1}% ".format(meter, progress))

        if len(tweets) == tweet_count:
            break

    if len(tweets) > 0:
        with gzip.open(utils.DATASET_HOME + TWITTER_TXT, 'wb') as f:
            # line break in tweet is \n, and between tweet is \r\n
            # https://dev.twitter.com/streaming/overview/processing
            f.write("\r\n".join(tweets).encode("utf-8"))
    else:
        print("can not get any tweets.")

def read_ini():
    config = configparser.ConfigParser()
    twitter = None
    try:
        config.read(TWITTER_INI)
        twitter = TwitterStream(config)
    except Exception as ex:
        print("You have to prepare {0} file on same directory.".format(TWITTER_INI))

    return twitter


class TwitterStream():

    # use streaming api
    # https://dev.twitter.com/streaming/reference/get/statuses/sample
    TWITTER_ENDPOINT = "https://stream.twitter.com/1.1/statuses/sample.json"

    def __init__(self, config):
        self.auth = OAuth1(client_key=config["consumer"]["key"],
                           client_secret=config["consumer"]["secret"],
                           resource_owner_key=config["access"]["token"],
                           resource_owner_secret=config["access"]["secret"],
                           signature_type='auth_header')

    def streaming(self):
        params = {"language": "ja", "filter_level": "medium"}
        r = requests.get(self.TWITTER_ENDPOINT, auth=self.auth, params=params, stream=True)

        for line in r.iter_lines():
            if line:
                yield json.loads(line.decode("utf-8"))


if __name__ == "__main__":
    main()
