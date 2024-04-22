#!/usr/bin/python3
""" export data in the CSV format. """
import csv
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = requests.get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for i in data2:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in data:

            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                writ.writerow(row)
