#!/usr/bin/python3
"""Returns information about a employee with a given ID"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = int(argv[1])

    resp = requests.get('https://jsonplaceholder.typicode.com/todos/')
    json_repr = resp.json()
    name_resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employee_id))
    name = name_resp.json().get('name')

    with open('{}.csv'.format(employee_id), 'w') as csv_data:
        csv_writer = csv.writer(
            csv_data,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL
            )

        for task in json_repr:
            if task.get('userId') == employee_id:
                csv_writer.writerow(
                    [
                        task.get('userId'),
                        name,
                        task.get('completed'),
                        task.get('title')])
        csv_data.close()
