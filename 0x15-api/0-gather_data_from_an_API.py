#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

def install_missing_module(module_name):
    """
    Installs the specified Python module using pip.
    """
    try:
        import importlib
        importlib.import_module(module_name)
    except ImportError:
        print(f"Trying to install required module: {module_name}")
        subprocess.call(["python", "-m", "pip", "install", module_name])
        importlib.import_module(module_name)

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays an employee's TODO list progress.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        None
    """
    base_url = "https://api.example.com/todo/api/v1.0/tasks"  # Replace with the actual API endpoint
    response = requests.get(f"{base_url}/{employee_id}")

    if response.status_code == 200:
        data = response.json()
        employee_name = data.get("employee_name")
        total_tasks = len(data.get("tasks"))
        done_tasks = sum(task.get("done") for task in data.get("tasks"))

        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        for task in data.get("tasks"):
            if task.get("done"):
                print(f"\t{task.get('title')}")

if __name__ == "__main__":
    # Check and install required modules
    install_missing_module("requests")

    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
