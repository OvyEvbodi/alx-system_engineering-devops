#!/usr/bin/python3

"""Queries a REST API to get information on employees' todos"""

from requests import get
from sys import argv
import json


def getTodos():
    """Gets an employee's todo data using an API"""
    url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users".format(url)
    response_user = get(user_url).json()
    tasks_dict = {}
    for user in response_user:
        user_id = user.get("id")
        username = user.get("username")
        todo_url = "{}todos?userId={}".format(url, user_id)
        response_todo = get(todo_url).json()
        tasks_list = [{"username": "{}".format(username),
                      "task": "{}".format(todo.get("title")),
                       "completed": todo.get("completed")
                       } for todo in response_todo]
        tasks_dict["{}".format(user_id)] = tasks_list
    path = "todo_all_employees.json"
    with open(path, 'w') as file:
        json.dump(tasks_dict, file)


if __name__ == '__main__':
    getTodos()
