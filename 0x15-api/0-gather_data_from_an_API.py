#!/usr/bin/python3
""" A Script for a given employee ID, returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests as re
    import sys

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch Employees_Name, Todos
    employee_name = re.get(url + "users/" + employee_id).json()["name"]
    todos = re.get(url + "todos", params={"userId": employee_id}).json()

    num_of_total = 0
    num_of_complete = 0
    title_list = []

    # Get Total_Number_Of_tasks, Number_Of_Done_Tasks
    for rows in todos:
        num_of_total += 1
        if rows["completed"] is True:
            title_list.append(rows["title"])
            num_of_complete += 1

    # Print Information and data
    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_of_complete, num_of_total))
    for title in title_list:
        print("\t{}".format(title))
