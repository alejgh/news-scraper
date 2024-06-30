from typing import Callable, List, Union, Literal
from .domain import HackerNewsEntry

class EntryPipeline:
    """ Pipeline that receives a list of HackerNewsEntry objects and performs filters and sort operations on them. """

    def __init__(self, filter_fn: Callable[[HackerNewsEntry], bool],
                 sort_key: Callable[[HackerNewsEntry], any],
                 sort_order: Union[Literal["asc"], Literal["desc"]],
                 name: str = "", description: str = ""):
        """ Creates a new instance of a pipeline.

        :param filter_fn: Function used to filter entries. It receives as parameter a HackerNewsEntry object and returns a boolean
            that indicates whether the entry should be filtered or not.
        :param sort_key: Key of the HackerNewsEntry object used to sort the results.
        :param sort_order: Whether the results should be sorted in ascending ('asc') or descending ('desc') order.
        :param name: Name of the pipeline, used for logging purposes.
        :param description: Description of the pipeline, used for logging purposes.
        """
        self.filter_fn = filter_fn
        self.sort_key = sort_key
        self.sort_order = sort_order
        self.name = name
        self.description = description

    def transform(self, entries: List[HackerNewsEntry]) -> List[HackerNewsEntry]:
        """ Performs the filter and sorting of the pipeline to the given list of entries

        :param entries: List of HackerNewsEntry objects that will be transformed.
        :return: Filtered and sorted list of HackerNewsEntry objects
        """
        filtered_entries = [e for e in entries if self.filter_fn(e)]
        sorted_entries = sorted(filtered_entries, key=self.sort_key, reverse=self.sort_order == "desc")
        return sorted_entries
