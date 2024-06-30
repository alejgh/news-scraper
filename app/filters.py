import re

from .domain import HackerNewsEntry
from typing import Literal, Union


def filter_by_words(entry: HackerNewsEntry, num_words: int = 5, comparison: Union[Literal["gt"], Literal["lte"]] = "gt") -> bool:
    """ Returns whether an entry has a title with a number of words meeting the required comparison

    :param entry: HackerNewsEntry object to be evaluated
    :param num_words: Number of words used to perform the filter
    :param comparison: Whether the title needs to have a number of words greater than ('gt') or lower or equal to ('lte') the given number
    :return: True if the title of the entry meets the given conditions and False otherwise
    """
    tokens = entry.title.split(" ")
    words = [t for t in tokens if _is_word(t)]
    return len(words) > num_words if comparison == "gt" else len(words) <= num_words

def _is_word(token: str) -> bool:
    """ Returns whether the given token is a word or not.

    This is a näive implementation that checks if the token contains at least one alphanumeric character for it to be
    considered a word.
    :param token:
    :return: True if the token is considered to be a word, and False otherwise.
    """
    alphanumeric_str = re.sub(r'[\W_]+', '', token)
    return len(alphanumeric_str) > 0
