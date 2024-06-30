from dataclasses import dataclass

@dataclass
class HackerNewsEntry:
    number: int
    title: str
    points: int
    num_comments: int
