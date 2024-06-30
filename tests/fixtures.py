import functools
import pytest

from app.filters import filter_by_words
from app.scraper import HackerNewsScraper
from unittest import mock
from .utils import read_file

class MockedResponse:
    def __init__(self, ok_result: bool, text: str):
        self.ok = ok_result
        self.text = text


@pytest.fixture
def mocked_scraper():
    scraper = HackerNewsScraper(base_url="http://www.example.com")
    scraper.session.get = mock.MagicMock(return_value=MockedResponse(ok_result=True, text=read_file("sample_page.html")))
    return scraper

@pytest.fixture
def mocked_scraper_no_content():
    scraper = HackerNewsScraper(base_url="http://www.example.com")
    scraper.session.get = mock.MagicMock(return_value=MockedResponse(ok_result=True, text=read_file("empty_page.html")))
    return scraper

@pytest.fixture
def mocked_scraper_network_error():
    scraper = HackerNewsScraper(base_url="http://www.example.com")
    scraper.session.get = mock.MagicMock(return_value=MockedResponse(ok_result=False, text=""))
    return scraper

@pytest.fixture
def filter_entries_greater_than_5_words():
    return functools.partial(filter_by_words, num_words=5, comparison="gt")

@pytest.fixture
def filter_entries_leq_than_5_words():
    return functools.partial(filter_by_words, num_words=5, comparison="lte")
