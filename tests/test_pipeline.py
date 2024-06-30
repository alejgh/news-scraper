from app.pipeline import EntryPipeline
from .fixtures import filter_entries_greater_than_5_words, filter_entries_leq_than_5_words
from .utils import SAMPLE_ENTRIES


def test_pipeline_sort_by_title(filter_entries_greater_than_5_words):
    pipeline = EntryPipeline(filter_entries_greater_than_5_words, lambda e: e.title, "asc")
    result = pipeline.transform(SAMPLE_ENTRIES)
    assert len(result) == 2
    assert result[0].title.startswith("Figma defaults")
    assert result[1].title.startswith("Show HN")

def test_pipeline_sort_order(filter_entries_greater_than_5_words):
    pipeline = EntryPipeline(filter_entries_greater_than_5_words, lambda e: e.title, "desc")
    result = pipeline.transform(SAMPLE_ENTRIES)
    assert len(result) == 2
    assert result[0].title.startswith("Show HN")
    assert result[1].title.startswith("Figma defaults")

def test_pipeline_filter_fns(filter_entries_greater_than_5_words, filter_entries_leq_than_5_words):
    pipe_a = EntryPipeline(filter_entries_greater_than_5_words, lambda e: e.num_comments, "desc")
    result_a = pipe_a.transform(SAMPLE_ENTRIES)
    assert len(result_a) == 2
    assert result_a[0].title.startswith("Show HN")
    assert result_a[1].title.startswith("Figma defaults")

    pipe_b = EntryPipeline(filter_entries_leq_than_5_words, lambda e: e.points, "desc")
    result_b = pipe_b.transform(SAMPLE_ENTRIES)
    assert len(result_b) == 4
    assert result_b[0].title.startswith("This is")
    assert result_b[-1].title.startswith("That Editor")
    assert result_b[1].points > result_b[2].points
