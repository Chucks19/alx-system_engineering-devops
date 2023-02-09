#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    url_user = url + "users/" + "employeeId"

    users = requests.get(url_user).json()
    employeeName = users.get('name')

    todoUrl = url + "todos"
    todos  = requests.get(todoUrl).json()
    done = 0
    completed = []

    for task in todos:
        if task.get('completed'):
            completed.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(todos)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
