import pandas as pd


def read_df():
    df = pd.read_csv("bridge_data/BridgeConditionReport_County-02_2022-02-07.csv")
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
