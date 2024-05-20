#!/usr/bin/python3
import json
import requests

def fetch_user_data(user_id):
    # Fetch user information
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    user = user_response.json()
    username = user['username']

    # Fetch tasks for the user
    tasks_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    tasks = tasks_response.json()

    # Structure the data as required
    user_tasks = []
    for task in tasks:
        user_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        })

    # Create the final dictionary with the required format
    data = {str(user_id): user_tasks}

    # Save the data to a JSON file
    filename = f"{user_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Data for user ID {user_id} has been written to {filename}")

# Example usage:
fetch_user_data(1)

