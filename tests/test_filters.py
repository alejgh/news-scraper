from app.filters import filter_by_words, _is_word
from .utils import SAMPLE_ENTRIES


def test_filter_by_word_greater_than():
    assert filter_by_words(SAMPLE_ENTRIES[0], 5)
    assert filter_by_words(SAMPLE_ENTRIES[0], 5, "gt")

    assert not filter_by_words(SAMPLE_ENTRIES[2], 5, "gt")
    assert filter_by_words(SAMPLE_ENTRIES[2], 4, "gt")

    assert not filter_by_words(SAMPLE_ENTRIES[5], 15, "gt")
    assert filter_by_words(SAMPLE_ENTRIES[5], 12, "gt")


def test_filter_by_word_lower_than():
    assert not filter_by_words(SAMPLE_ENTRIES[0], 5, "lte")
    assert filter_by_words(SAMPLE_ENTRIES[0], 5)

    assert filter_by_words(SAMPLE_ENTRIES[2], 5, "lte")
    assert not filter_by_words(SAMPLE_ENTRIES[2], 4, "lte")

    assert filter_by_words(SAMPLE_ENTRIES[5], 15, "lte")
    assert not filter_by_words(SAMPLE_ENTRIES[5], 12, "lte")


def test_filter_by_word_negative_length():
    assert not filter_by_words(SAMPLE_ENTRIES[1], -6, "lte")
    assert filter_by_words(SAMPLE_ENTRIES[1], -6, "gt")

def test_is_word():
    assert _is_word("example")
    assert _is_word("23")
    assert _is_word("self-explained")
    assert _is_word("A")

    assert not _is_word("")
    assert not _is_word("   ")
    assert not _is_word("-,'!")
