#!/usr/bin/python3

"""Queries a REST API to get information on employees' todos"""

from requests import get
from sys import argv
import json


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

        path = "{}.json".format(user_id)
        with open(path, 'w') as file:
            tasks_list = [{"task": "{}".format(todo.get("title")),
                          "completed": "{}".format(todo.get("completed")),
                           "username": "{}"
                           .format(username)} for todo in response_todo]
            tasks_dict = {"{}".format(user_id): tasks_list}
            json.dump(tasks_dict, file)


if __name__ == '__main__':
    getTodos()
