import pandas as pd
import glob
import os


def get_latest_df():
    list_of_files = glob.glob(
        "/home/mikem/Documents/code/bridge_bot/bridge_data/*.csv"
    )  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file


def read_df(latest_file):
    df = pd.read_csv(latest_file)
    return df


def poor_bridges(df):
    # All bridges that are 'poor'
    poor_condition = df[df[" Condition"] == "Poor"]
    return poor_condition


def poor_bridge_percent(df, poor_condition):
    def percentage(part, whole):
        percentage = 100 * float(part) / float(whole)
        return percentage

    # What percent of bridges in Allegheny county are rated 'poor'?
    total_bridges = len(df[" Location/Structure Name"])
    total_poor_bridges = len(poor_condition[" Location/Structure Name"])

    total = percentage(total_poor_bridges, total_bridges)
    return total


def most_poor_bridges_by_municipality(poor_condition):
    # shows which neighborhood has the most 'poor' bridges
    poor_by_hood = poor_condition.groupby([" Municipality"]).count()
    poor_by_hood_sorted = poor_by_hood.sort_values(
        by=" Location/Structure Name", ascending=False
    )
    top_5 = poor_by_hood_sorted.head().index.tolist()

    top_5_str = ", ".join(top_5)
    return top_5_str
