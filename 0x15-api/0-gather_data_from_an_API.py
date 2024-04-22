#!/usr/bin/python3
""" Returns information about and employee's TODO list progress"""
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])

    # Fetch user information
    user_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))

    if user_response.status_code != 200:
        print('User not found')
        exit(1)

    employee_name = user_response.json().get('name')

    # Fetch TODO list
    todos_response = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id))

    if todos_response.status_code != 200:
        print('TODO list not found')
        exit(1)

    todos = todos_response.json()
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print('\t', task['title'])
