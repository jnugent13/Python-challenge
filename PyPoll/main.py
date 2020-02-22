import csv
import os

csvpath = os.path.join("Downloads", "election_data.csv")

votes = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvpath, delimiter=",")
    header = next(csvreader)

    