import argparse
import functools
import os

from app.filters import filter_by_words
from app.pipeline import EntryPipeline
from app.repository import MongoDBRepository, SQLiteRepository
from app.scraper import HackerNewsScraper
from dotenv import dotenv_values


def load_params():
    parser = argparse.ArgumentParser(prog="HackerNewsScraper")
    parser.add_argument('-n', '--num_entries', type=int, required=False, default=30,
                        help="Number of entries to be scraped from the site")
    parser.add_argument('-db', '--database', type=str, choices=["sqlite", "mongodb"], default="sqlite", required=False,
                        help="Database used to store information about the entries")
    return parser.parse_args()


if __name__ == "__main__":
    # load input arguments and config
    args = load_params()
    config = dotenv_values(os.path.join("config", ".env"))

    # Get entries from hacker news
    scraper = HackerNewsScraper(base_url=config["BASE_URL"])
    entries = scraper.get_entries(page=1, num_entries=args.num_entries)

    # define entry processing pipelines
    pipelines = [
        EntryPipeline(filter_fn=functools.partial(filter_by_words, num_words=5, comparison="gt"),
                      sort_key=lambda x: x.num_comments, sort_order="desc",
                      name="filter_a", description="Filter all entries with more than five words in the title ordered by the number of comments"),
        EntryPipeline(filter_fn=functools.partial(filter_by_words, num_words=5, comparison="lte"),
                      sort_key=lambda x: x.points, sort_order="desc",
                      name="filter_b", description="Filter all entries with less than or equal to five words in the title ordered by points")
    ]

    # process entries
    repository = SQLiteRepository(config["SQLITE_DATABASE"]) if args.database == "sqlite" else MongoDBRepository(config["MONGODB_URI"])
    for pipe in pipelines:
        print(f"Filtering entries with {pipe.name}: '{pipe.description}'")
        print("-" * 150)
        result = pipe.transform(entries)
        for idx, entry in enumerate(result):
            print(f"{idx + 1}. {entry}")

        print("\nSaving results to database...")
        repository.save_entries(result, pipe.name)
        print("Results saved\n\n")
