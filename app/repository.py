import time
import sqlite3
import uuid

from typing import List
from .domain import HackerNewsEntry


class SQLiteRepository:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self._init_db()

    def save_entries(self, entries: List[HackerNewsEntry], filter_name: str):
        curr_timestamp = int(time.time())
        with self.conn as c:
            for idx, entry in enumerate(entries):
                c.execute("INSERT INTO EntryRecord (id, entry_order, title, created_at, filter) VALUES (?, ?, ?, ?, ?)",
                          (str(uuid.uuid4()), idx, entry.title, curr_timestamp, filter_name))

    def _init_db(self):
        with self.conn as c:
            c.execute("CREATE TABLE IF NOT EXISTS EntryRecord(id TEXT PRIMARY KEY, entry_order INTEGER, title TEXT, created_at INTEGER, filter TEXT)")
