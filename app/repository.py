import datetime
import time
import sqlite3
import uuid

from pymongo import MongoClient
from typing import List
from .domain import HackerNewsEntry


class SQLiteRepository:
    """ Repository that inserts entries data in a SQLite database """
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self._init_db()

    def save_entries(self, entries: List[HackerNewsEntry], filter_name: str):
        """ Save the given entries in the database.

        Currently, the following information is saved: order of each entry, title, UNIX timestamp with the current time,
        and name of the filter applied to obtain the entry.

        :param entries: List of entries to be saved
        :param filter_name: Name of the filter used to obtain the entries
        :return: None
        """
        curr_timestamp = int(time.time())
        with self.conn as c:
            for idx, entry in enumerate(entries):
                c.execute("INSERT INTO EntryRecord (id, entry_order, title, created_at, filter) VALUES (?, ?, ?, ?, ?)",
                          (str(uuid.uuid4()), idx+1, entry.title, curr_timestamp, filter_name))

    def _init_db(self):
        with self.conn as c:
            c.execute("CREATE TABLE IF NOT EXISTS EntryRecord(id TEXT PRIMARY KEY, entry_order INTEGER, title TEXT, created_at INTEGER, filter TEXT)")


class MongoDBRepository:
    """ Repository that inserts entries data in a Mongo database """
    def __init__(self, mongo_db_uri: str):
        client = MongoClient(mongo_db_uri)
        db = client.records_db
        self.collection = db.entries

    def save_entries(self, entries: List[HackerNewsEntry], filter_name: str):
        """ Save the given entries in the database.

        The following information is saved: order of each entry, title, current datetime, and name of the filter applied to obtain the entry.

        :param entries: List of entries to be saved
        :param filter_name: Name of the filter used to obtain the entries
        :return: None
        """
        curr_date = datetime.datetime.now()
        entries_docs = [
            {
                "order": idx+1,
                "title": e.title,
                "filter_name": filter_name,
                "created_at": curr_date
            }
            for idx, e in enumerate(entries)
        ]
        self.collection.insert_many(entries_docs)
