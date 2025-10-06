#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts", "get")
    print("Status Code: {}".format(response.status_code))
    fetched = response.json()
    for value in fetched:
        print(f"{value['title']}")


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts", "get")
    print("Status Code: {}".format(response.status_code))
    fetched = response.json()

    with open("posts.csv", "w", encoding="utf-8") as f:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for d in fetched:
            writer.writerow(
                {
                    "id": d["id"],
                    "title": d["title"],
                    "body": d["body"],
                }
            )
