#!/usr/bin/python3

"""Queries a REST API to get information on employees' todos"""

from requests import get
from sys import argv

def getTodos():
    """Gets an employee's todo data using an API"""

    if len(argv) > 1:
        url = "https://jsonplaceholder.typicode.com/"
        user_url = "{}users/{}".format(url, argv[1])

        response_user = get(user_url)
        name = response_user.json().get("name")

        todo_url = "{}todos?userId={}".format(url, argv[1])

        response_todo = get(todo_url).json()
        total_no_of_tasks = len(response_todo)
        completed_tasks = [task for task in response_todo if task
                           .get("completed")]
        no_of_completed_tasks = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):"
              .format(name, no_of_completed_tasks, total_no_of_tasks))
        for task in completed_tasks:
            print("\t {}".format(task.get("title")))

if __name__ == '__main__':
    getTodos()
