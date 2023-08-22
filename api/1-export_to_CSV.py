#!/usr/bin/python3
"""Using API and export it in csv file"""

from sys import argv
import requests

url_base = 'https://jsonplaceholder.typicode.com/users/'


def export_csv(id):
    """Export csv file"""

    user = requests.get(url_base + id).json()
    tasks = requests.get(url_base + id + "/todos/").json()
    file_name = id + ".csv"

    for task in tasks:
        data = '"' + str(user['id']) + '",' + '"' + user['username'] + '",' +\
            '"' + str(task['completed']) + '",' + '"' + task['title'] +\
               '"\n'

        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(data)


if __name__ == "__main__":
    export_csv(argv[1])
