from tweepy.streaming import StreamListener

class TweetStreamListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print(str.format('Error on_data: {0}', str(e)))
        return True

    def on_error(self, status):
        print(status)
        return True
