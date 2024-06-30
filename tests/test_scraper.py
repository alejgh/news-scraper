import pytest

from app.error import NetworkRequestError
from app.scraper import HackerNewsScraper
from .fixtures import mocked_scraper, mocked_scraper_no_content, mocked_scraper_network_error


def test_get_entries_valid(mocked_scraper: HackerNewsScraper):
    entries = mocked_scraper.get_entries(num_entries=10)
    assert len(entries) == 10
    sample_entry = entries[0]
    assert sample_entry.points == 141
    assert sample_entry.number == 1
    assert sample_entry.title == "Bytecode Breakdown: Unraveling Factorio's Lua Security Flaws"
    assert sample_entry.num_comments == 18

    expected_url = mocked_scraper.base_url
    assert mocked_scraper.session.get.called_once_with(expected_url)

def test_get_entries_with_invalid_inputs(mocked_scraper: HackerNewsScraper):
    entries = mocked_scraper.get_entries(num_entries=-5)
    assert entries == []

    entries = mocked_scraper.get_entries(page=-1)
    assert entries == []

def test_get_entries_with_multiple_pages(mocked_scraper: HackerNewsScraper):
    entries = mocked_scraper.get_entries(num_entries=50)
    assert len(entries) == 50

def test_get_entries_with_no_content(mocked_scraper_no_content: HackerNewsScraper):
    entries = mocked_scraper_no_content.get_entries(num_entries=50)
    assert entries == []

def test_get_entries_with_network_error(mocked_scraper_network_error: HackerNewsScraper):
    with pytest.raises(NetworkRequestError):
        mocked_scraper_network_error.get_entries()
