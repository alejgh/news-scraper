import requests

from .domain import HackerNewsEntry
from .error import NetworkRequestError
from .parsers import parse_entries
from requests.adapters import HTTPAdapter, Retry
from typing import List

class HackerNewsScraper:
    """ This class can be used to scrape content from the hacker news website. """

    def __init__(self, base_url: str = "https://news.ycombinator.com/"):
        """ Creates a new instance of a scraper.

        :param base_url: Base url of the hackers new website to be scraped
        """
        self.base_url = base_url
        self.session = requests.Session()

        # add exponential backoff to handle network issues and server errors
        retries = Retry(total=5,
                        backoff_factor=0.1,
                        status_forcelist=[ 500, 502, 503, 504 ])
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    def get_entries(self, num_entries: int = 30, page: int = 1) -> List[HackerNewsEntry]:
        """ Gets news entries from the hacker news site.

        :param num_entries: Number of entries to be retrieved.
        :param page: Page from which the scraping will be started.
        :return: List of HackerNewsEntry objects with the contents of the scraped entries.
        :raises: NetworkRequestError if there was a network error retrieving the HTML content from the website.
        """
        if num_entries <= 0 or page < 0:
            return []

        # get html content from the site
        request_result = self.session.get(self._build_url(page))
        if not request_result.ok:
            raise NetworkRequestError()

        # parse entry objects from html
        new_entries = parse_entries(request_result.text)
        result = new_entries

        # if we have to fetch more entries, go to newer pages
        if len(result) < num_entries and len(new_entries) > 0:
            remaining_entries = num_entries - len(result)
            new_entries = self.get_entries(remaining_entries, page + 1)
            result += new_entries
        return result[:num_entries]

    def _build_url(self, page: int = 0):
        return self.base_url if page == 0 else f"{self.base_url}?p={page}"
