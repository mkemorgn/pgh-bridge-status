import pandas as pd


def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return percentage


df = pd.read_csv("BridgeConditionReport_County-02_2022-02-07.csv")

# All bridges that are 'poor'
poor_condition = df[df[" Condition"] == "Poor"]

# What percent of bridges in Allegheny county are rated 'poor'?
total_bridges = len(df[" Location/Structure Name"])
total_poor_bridges = len(poor_condition[" Location/Structure Name"])

first = percentage(total_poor_bridges, total_bridges)
print("%.2f" % first + "%" + " of bridges in Allegeny County are 'poor'")
