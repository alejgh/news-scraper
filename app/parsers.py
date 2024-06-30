from bs4 import BeautifulSoup
from .domain import HackerNewsEntry
from typing import List
from unicodedata import normalize


def parse_entries(html_doc: str) -> List[HackerNewsEntry]:
    """ Parse the contents of an html page into news entries objects.

    :param html_doc: String content of the html document to be parsed.
    :return: List of HackerNewEntry objects.
    """
    soup = BeautifulSoup(html_doc, "lxml")
    html_entries = soup.find_all("tr", class_="athing")
    return [_parse_entry(e) for e in html_entries]

def _parse_entry(element) -> HackerNewsEntry:
    rank_element = element.find(class_="rank")
    try:
        rank = int(rank_element.text.split('.')[0]) if rank_element is not None else 0
    except ValueError:
        rank = 0

    heading_element = element.find(class_="titleline")
    title_element = heading_element.find("a") if heading_element is not None else None
    title = title_element.text if title_element is not None else ""

    sibling = element.find_next_sibling()
    score_element = sibling.find(class_="score")
    try:
        score = int(score_element.text.split(" point")[0]) if score_element is not None else 0
    except ValueError:
        score = 0

    links_elements = sibling.find_all("a")
    comments_element = links_elements[-1] if len(links_elements) > 0 else None
    try:
        comments_text = normalize('NFKD', comments_element.text) if comments_element is not None else ""
        num_comments = int(comments_text.split(" comment")[0]) if "comment" in comments_text else 0
    except ValueError:
        num_comments = 0

    return HackerNewsEntry(rank, title, score, num_comments)
