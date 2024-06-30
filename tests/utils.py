import os

from app.domain import HackerNewsEntry

DATA_DIR = os.path.join("tests", "data")

SAMPLE_ENTRIES = [
    HackerNewsEntry(title="Figma defaults to train AI models on personal data ", num_comments=5, points=2, number=1),
    HackerNewsEntry(title="Python toolkit for quantitative finance", num_comments=8, points=32, number=2),
    HackerNewsEntry(title="This is - a self-explained example", num_comments=68, points=41, number=3),
    HackerNewsEntry(title="Alphatab.net", num_comments=2, points=7, number=4),
    HackerNewsEntry(title="That Editor", num_comments=6, points=1, number=5),
    HackerNewsEntry(title="Show HN: Conway's Game of Life, but as a div full of Braille characters", num_comments=15, points=2, number=6),
]

def read_file(filename: str):
    with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
        return f.read()
