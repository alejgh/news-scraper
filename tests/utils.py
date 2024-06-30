import os

DATA_DIR = os.path.join("tests", "data")

def read_file(filename: str):
    with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
        return f.read()
