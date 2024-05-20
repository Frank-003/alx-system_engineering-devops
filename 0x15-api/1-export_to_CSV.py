#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys
    def export_tasks_to_csv(tasks):
    # Define the output filename (e.g., USER_ID.csv)
    user_id = tasks[0]["USER_ID"]  # Assuming all tasks belong to the same user
    filename = f"{user_id}.csv"

    # Write data to the CSV file
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header row
        writer.writeheader()

        # Write task data
        for task in tasks:
            writer.writerow(task)

    print(f"Data exported to {filename}")
