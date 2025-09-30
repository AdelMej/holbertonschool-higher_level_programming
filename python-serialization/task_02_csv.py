"""
File containing a function that convert csv files into json
"""
import csv
import json


def convert_csv_to_json(filename):
    """Function that convert csv to json"""
    try:
        with open(filename, "r") as f:
            csv_iter = csv.DictReader(f)
            rows = list(csv_iter)

        with open("data.json", "w", encoding="utf-8") as f:
            f.write("[\n")
            for i, row in enumerate(rows):
                line = "    " + json.dumps(row)
                if i < len(rows) - 1:
                    line += ','
                f.write(line + "\n")
            f.write("]\n")
    except FileNotFoundError:
        return False
