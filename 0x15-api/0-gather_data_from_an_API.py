#!/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
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

    else:
        print(f"Error fetching data for employee {employee_id}. Status code: {response.status_code}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)

