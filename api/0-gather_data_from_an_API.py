#!/usr/bin/python3
'''returns information about his/her TODO list progress.'''
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee whose progress is to be fetched.

    Returns:
        None
    """

    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct URLs for user and todos data
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user data and todos data from the API
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        # Parse JSON responses
        user_data = user_response.json()
        todos_data = todos_response.json()

        # Extract relevant information
        employee_name = user_data["name"]
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task["completed"]]
        num_done_tasks = len(done_tasks)

        # Print employee's TODO list progress
        print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        # Parse employee ID from command-line argument
        employee_id = int(sys.argv[1])
        # Fetch and display employee's TODO list progress
        get_employee_todo_progress(employee_id)
