import tweepy, os
from tweetstreamlistener import TweetStreamListener
from tweepy import OAuthHandler
from tweepy import Stream

with open('filters.txt', 'r') as filter_file:
    filters = filter_file.readlines()

filters = [f.strip() for f in filters]


consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_secret = os.environ['TWITTER_ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitter_stream = Stream(auth, TweetStreamListener())
twitter_stream.filter(track=filters)
