import json
import os
from datetime import datetime

filename = os.path.expanduser("~/tasker.json")


def __init__(self):
    self.data = self.load_data()


def save_tasks(data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_tasks():
    if not os.path.isfile(filename):
        with open(filename, "w") as file:
            json.dump([], file)
        return []

    with open(filename, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def get_id(tasks):
    # Creates a list of all IDs
    # Finds the highest number (id) then add 1
    # default starts from 0
    return max([task["id"] for task in tasks], default=0) + 1


def add_task(description):
    tasks = load_tasks()
    id = get_id(tasks)
    currentTime = datetime.now().isoformat()
    status = "Todo"
    print(f"Task added successfully (ID: {id})")


def main():
    print("Welcome to Tasker")
