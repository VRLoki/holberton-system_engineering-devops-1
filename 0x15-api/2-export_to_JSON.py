#!/usr/bin/python3
"""Returns information about a employee with a given ID"""
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = int(argv[1])

    resp = requests.get('https://jsonplaceholder.typicode.com/todos/')
    json_repr = resp.json()
    name_resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employee_id))
    name = name_resp.json().get('name')

    with open('{}.json'.format(employee_id), 'w') as json_data:
        list_attributes = []
        dict_employee = {}
        for tasks in json_repr:
            tmp_list, tmp_dict = [], {}
            if tasks.get('userId') == employee_id:
                tmp_dict['task'] = tasks.get('title')
                tmp_dict['completed'] = tasks.get('completed')
                tmp_dict['username'] = name
                list_attributes.append(tmp_dict)
        dict_employee[employee_id] = list_attributes
        jsonString = json.dumps(dict_employee)
        json_data.write(jsonString)
        print(dict_employee)
        json_data.close()
