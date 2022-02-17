import pandas as pd
import glob
import os


def get_latest_df():
    list_of_files = glob.glob("/home/mikem/Documents/code/bridge_bot/bridge_data/*.csv")
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def read_df(latest_file):
    df = pd.read_csv(latest_file)
    return df


def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return percentage


def poor_bridges(df):
    # All bridges that are 'poor'
    poor_condition = df[df[" Condition"] == "Poor"]
    return poor_condition


def poor_bridge_percent(df, poor_condition):
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


def poor_open_no_restrictions(poor_condition):
    # group 'poor' bridges by posting status
    poor_grouped = poor_condition.groupby([" Posting Status"]).count()

    # Find percentage of bridges that are rated 'poor' but open with no restrictions
    poor_open = poor_grouped[" Location/Structure Name"]
    poor_open_count = poor_open[1]
    poor_condition_count = len(poor_condition[" Location/Structure Name"])

    poor_status_percentage = percentage(poor_open_count, poor_condition_count)
    return poor_status_percentage
