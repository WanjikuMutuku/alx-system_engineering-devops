#!/usr/bin/python3
""" export data in the CSV format. """
import csv
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee.id>")
        exit(1)

    employee_id = int(argv[1])

    #fetch user information
    user_response = requests.get(
        'https://jsonplaceholder.typicode.com/users{}'.format(employee_id))

    if user_response.status_code != 200:
        print('User not found')
        exit(1)

    user_data = user_response.json()
    employee_name = user_data.get('name')

    #fetch the TODO list
    todos_response = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id))

    if todos_response.status_code != 200:
        prit('TODO list not found')
        exit(1)

    todos = todos_response.json()

    #prepare CSV data
    csv_data = []
    for task in todos:
        csv_data.append([
            employee_id,
            user_data.get('username'),
            str(task.get('completed')),
            task.get('title')
        ])
    # export to CSV file
    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer/writerows(csv_data)

    print('Data exported to {}'.format(filename))
