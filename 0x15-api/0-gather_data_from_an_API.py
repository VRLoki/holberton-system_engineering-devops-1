#!/usr/bin/python3
"""Returns information about a employee with a given ID"""
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = int(argv[1])

    resp = requests.get('https://jsonplaceholder.typicode.com/todos/')
    json_repr = resp.json()
    name_resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_id))
    name = name_resp.json().get('name')
    tasks_done, total_task = 0, 0

    for task in json_repr:
        if task.get('userId') == employee_id:
            total_task = total_task + 1
            if task.get('completed') is True:
                tasks_done = tasks_done + 1
    print('Employee {} is done with tasks({}/{}):'.format(
        name,
        tasks_done,
        total_task
        ))
    for task in json_repr:
        if task.get('userId') == employee_id and task.get('completed') is True:
            print("\t " + task.get('title'))
