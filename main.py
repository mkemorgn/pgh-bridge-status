import datetime
import glob
import os
import bridge
import web
import api


def get_latest_df():
    list_of_files = glob.glob("/home/mikem/Documents/code/bridge_bot/bridge_data/*.csv")
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def main():
    latest_file_check = str(get_latest_df())
    current_date = str(datetime.date.today())
    if latest_file_check[-14:-4] == current_date:
        print("Data up to date.")
    else:
        web.get_df()

    latest_file = get_latest_df()
    df = bridge.read_df(latest_file)
    poor_condition = bridge.poor_bridges(df)
    percent_of_poor_bridges = bridge.poor_bridge_percent(df, poor_condition)
    poor_bridges_by_municipality = bridge.most_poor_bridges_by_municipality(
        poor_condition
    )
    poor_status_percentage = bridge.poor_open_no_restrictions(poor_condition)
    print(
        "%.0f" % percent_of_poor_bridges
        + "%"
        + " of bridges in Allegeny County are rated 'poor'"
    )
    print(
        "These municipalities have the most bridges rated 'poor': "
        + poor_bridges_by_municipality
    )
    print(
        "%.0f" % poor_status_percentage
        + "%"
        + " of bridges rated 'poor' are open with no restrictions"
    )
    should_tweet = input("Would you like to tweet these stats?").lower()
    if should_tweet == "yes":
        api.update_status(
            percent_of_poor_bridges,
            poor_bridges_by_municipality,
            poor_status_percentage,
        )


if __name__ == "__main__":
    main()
