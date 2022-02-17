import tweepy
import datetime
import bridge
import config
import web

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():
    # web.get_df()
    latest_file = bridge.get_latest_df()
    df = bridge.read_df(latest_file)
    poor_condition = bridge.poor_bridges(df)
    percent_of_poor_bridges = bridge.poor_bridge_percent(df, poor_condition)
    """
    api.update_status(
        "%.2f" % percent_of_poor_bridges
        + "%"
        + " of bridges in Allegeny County are 'poor'"
    )
    """
    print(
        "%.2f" % percent_of_poor_bridges
        + "%"
        + " of bridges in Allegeny County are rated 'poor'"
    )
    poor_bridges_by_municipality = bridge.most_poor_bridges_by_municipality(
        poor_condition
    )
    """
    api.update_status(
        "These municipalities have the most bridges rated 'poor': "
        + poor_bridges_by_municipality
    )
    """
    print(
        "These municipalities have the most bridges rated 'poor': "
        + poor_bridges_by_municipality
    )
    poor_status_percentage = bridge.poor_open_no_restrictions(poor_condition)
    print(
        "%.0f" % poor_status_percentage
        + "%"
        + " of bridges rated 'poor' are open with no restrictions"
    )


if __name__ == "__main__":
    main()
