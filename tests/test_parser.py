from app.parsers import parse_entries
from app.domain import HackerNewsEntry
from .utils import read_file


def test_parse_single_valid_entry():
    contents = read_file("valid_entry.txt")
    parsed_entries = parse_entries(contents)
    assert len(parsed_entries) == 1

    entry = parsed_entries[0]
    assert isinstance(entry, HackerNewsEntry)
    assert entry.title == "Bytecode Breakdown: Unraveling Factorio's Lua Security Flaws"
    assert entry.number == 1
    assert entry.points == 141
    assert entry.num_comments == 18

def test_parse_multiple_valid_entries():
    contents = read_file("valid_entries.txt")
    parsed_entries = parse_entries(contents)
    assert len(parsed_entries) == 2

    entry = parsed_entries[1]
    assert isinstance(entry, HackerNewsEntry)
    assert entry.title == "Show HN: Protect your links with a password"
    assert entry.number == 4
    assert entry.points == 17
    assert entry.num_comments == 18

def test_parse_single_entry_missing_entry_properties():
    contents = read_file("invalid_entry1.txt")
    parsed_entries = parse_entries(contents)
    assert len(parsed_entries) == 1

    entry = parsed_entries[0]
    assert isinstance(entry, HackerNewsEntry)
    assert entry.title == ""
    assert entry.number == 1
    assert entry.points == 0
    assert entry.num_comments == 0

def test_parse_without_entries():
    contents = read_file("invalid_entry2.txt")
    parsed_entries = parse_entries(contents)
    assert len(parsed_entries) == 0
