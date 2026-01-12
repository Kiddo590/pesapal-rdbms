import os
import json

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def table_path(table_name):
    return os.path.join(DATA_DIR, f"{table_name}.table")

def write_row(table_name, row):
    with open(table_path(table_name), "a") as f:
        f.write(json.dumps(row) + "\n")

def read_rows(table_name):
    path = table_path(table_name)
    if not os.path.exists(path):
        return []

    with open(path, "r") as f:
        return [json.loads(line) for line in f]
