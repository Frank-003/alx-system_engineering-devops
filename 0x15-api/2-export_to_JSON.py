#!/usr/bin/python3
import json
import requests
import sys
def fetch_user_data(user_id):
    # Fetch user information
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}")
    user_data = user_response.json()
    username = user_data['username']

    # Fetch user's tasks
    tasks_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")
    tasks_data = tasks_response.json()

    # Prepare the data to be exported
    tasks_list = [{
        "task": task['title'],
        "completed": task['completed'],
        "username": username
    } for task in tasks_data]

    # Prepare the final data structure
    data = {str(user_id): tasks_list}

    # Export to JSON file
    with open(f"{user_id}.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    user_id = 1  # Example user_id, replace with the desired user_id
    fetch_user_data(user_id)
    print(f"Data for user {user_id} has been exported to {user_id}.json")

