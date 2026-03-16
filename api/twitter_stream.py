import tweepy

class TwitterStream:

    def __init__(self, bearer_token):

        self.client = tweepy.Client(bearer_token)

    def search_crypto(self, query="bitcoin OR btc OR ethereum"):

        tweets = self.client.search_recent_tweets(
            query=query,
            max_results=100
        )

        return [t.text for t in tweets.data]
