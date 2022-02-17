import datetime
import bridge
import web
import api


def main():
    # web.get_df()
    latest_file = bridge.get_latest_df()
    df = bridge.read_df(latest_file)
    poor_condition = bridge.poor_bridges(df)
    percent_of_poor_bridges = bridge.poor_bridge_percent(df, poor_condition)
    print(
        "%.0f" % percent_of_poor_bridges
        + "%"
        + " of bridges in Allegeny County are rated 'poor'"
    )
    poor_bridges_by_municipality = bridge.most_poor_bridges_by_municipality(
        poor_condition
    )
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

    status = api.update_status(
        percent_of_poor_bridges, poor_bridges_by_municipality, poor_status_percentage
    )


if __name__ == "__main__":
    main()
