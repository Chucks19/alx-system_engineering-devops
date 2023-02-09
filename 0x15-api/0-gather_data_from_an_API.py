#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
from sys import argv


if __name__ == '__main__':
    us_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    url_user = url + "users/{}".format(us_id)

    users = requests.get(url_user).json()
    employeeName = users.get('name')

    todoUrl = url + "todos"
    todos  = requests.get(todoUrl).json()
    done = 0
    completed = []

    for task in todos:
        if task.get('completed') is True:
            completed.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task.get('title')))
