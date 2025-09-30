"""
File containing a function that convert csv files into json
"""
import csv
import json


def convert_csv_to_json(filename):
    """Function that convert csv to json"""
    try:
        list_csv = []
        with open(filename, "r") as f:
            csv_iter = csv.DictReader(f)
            for row in csv_iter:
                list_csv.append(row)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(list_csv, f, indent=4)
    except FileNotFoundError:
        return False
