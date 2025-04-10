import json
import os

filename = os.path.expanduser("~/tasker.json")


def save_data(data: dict[str, dict], path: str) -> None:
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def load_data(path: str) -> dict[str, dict]:
    try:
        with open(path) as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data


def main():
    print("testing")
