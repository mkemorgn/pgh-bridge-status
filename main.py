import tweepy
import datetime
import bridge
import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():
    def publictweet():
        tweettopublish = "Hello world 1"
        api.update_status(tweettopublish)
        print(tweettopublish)

    def percentage(part, whole):
        percentage = 100 * float(part) / float(whole)
        return percentage

    publictweet()


if __name__ == "__main__":
    main()
