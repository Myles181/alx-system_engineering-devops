#!/usr/bin/python3
""" A Script for a given employee ID, returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests as re
    import sys

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch Employees_Name, Todos
    employee_name = re.get(url + "users/" + employee_id).json()["username"]
    todos = re.get(url + "todos", params={"userId": employee_id}).json()

    users = {str(employee_id): []}

    for todo in todos:
        user = {"task": todo["title"], "completed": todo["completed"], "username": employee_name}
        users[str(employee_id)].append(user)

    with open("{}.json".format(employee_id), "w") as f:
        json.dump(users, f)
