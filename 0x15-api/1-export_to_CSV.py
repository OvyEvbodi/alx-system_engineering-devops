#!/usr/bin/python3

"""Queries a REST API to get information on employees' todos"""

from requests import get
from sys import argv
import csv


def getTodos():
    """Gets an employee's todo data using an API"""

    if len(argv) > 1:
        user_id = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        user_url = "{}users/{}".format(url, user_id)

        response_user = get(user_url)
        username = response_user.json().get("username")

        todo_url = "{}todos?userId={}".format(url, user_id)

        response_todo = get(todo_url).json()

        path = "{}.csv".format(user_id)
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for todo in response_todo:
                writer.writerow([user_id, username, todo.get("completed"),
                                todo.get("title")])


if __name__ == '__main__':
    getTodos()
