#!/usr/bin/python3
""" A Script for a given employee ID, returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests as re
    import sys
    import csv

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch Employees_Name, Todos
    employee_name = re.get(url + "users/" + employee_id).json()["username"]
    todos = re.get(url + "todos", params={"userId": employee_id}).json()

    # Write data into 2.csv
    with open("2.csv", "a") as f:
        writer = csv.writer(f)
        for todo in todos:
            writer.writerow((employee_id, employee_name, todo["completed"], todo["title"]))

