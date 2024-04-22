#!/usr/bin/python3
""" exports to json using todo_all_employees.json """
import json
import requests

if __name__ == '__main__':
    # Fetch user information
    user_response = requests.get('https://jsonplaceholder.typicode.com/users')
    user_data = user_response.json()

    # Fetch TODO list
    todos_response = requests.get
    ('https://jsonplaceholder.typicode.com/todos')
    todos = todos_response.json()

    # Prepare JSON data
    json_data = {}
    for user in user_data:
        user_id = str(user['id'])
        username = user['username']
        json_data[user_id] = []

        for task in todos:
            if task['userId'] == user['id']:
                json_data[user_id].append({
                    'username': username,
                    'task': task['title'],
                    'completed': task['completed']
                })

    # Export to JSON file
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(json_data, file)

    print('Data exported to {}'.format(filename))
