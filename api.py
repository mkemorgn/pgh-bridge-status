import tweepy
import config


consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def update_status(
    percent_of_poor_bridges, poor_bridges_by_municipality, poor_status_percentage
):
    api.update_status(
        "%.0f" % percent_of_poor_bridges
        + "%"
        + " of bridges in Allegeny County are 'poor'"
    )

    api.update_status(
        "These municipalities have the most bridges rated 'poor': "
        + poor_bridges_by_municipality
    )

    api.update_status(
        "%.0f" % poor_status_percentage
        + "%"
        + " of bridges rated 'poor' are open with no restrictions"
    )
