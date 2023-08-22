#!/usr/bin/python3
""" Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress. """

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{sys.argv[1]}").json()
    to_dos = requests.get(f"{url}/todos",
                          params={"userId": sys.argv[1]}).json()
    total_tasks = len(to_dos)
    completed_tasks = sum(1 for to_do in to_dos if to_do["completed"])

    print(f"Employee {user.get('name')} is done with tasks\
({completed_tasks}/{total_tasks}):")

    [print(f"\t {to_do['title']}") for to_do in to_dos if to_do["completed"]]
