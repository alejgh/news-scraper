# news-scraper
This program scrapes entries from the [Hacker News](https://news.ycombinator.com/) website, applying multiple filters over those entries and storing the results on a database.

## Code structure
This repository is composed of the following files:
- **.github**: Folder containing code to run automatically the program tests when creating a pull request on the repository.
- **app**: Main code of the app, which is split into the following files:
  - domain.py: Domain model of the program.
  - error.py: Custom errors that have been defined.
  - filters.py: Functions used to filter entries based on the number of words in their title. 
  - parsers.py: Functions that parse HTML content from the website into domain model objects. 
  - pipeline.py: Pipeline class that applies filters and sort operations to entries.
  - repository.py: Repository classes that connect to the db and store usage information of the program. Currently each filtered entry is stored, as well as the request timestamp and the filter applied to that entry.
  - scraper.py: Scraper class used to fetch the html information from the website for the needed number of entries.
- **config**: Configuration files, currently consisting of the initialization script for the MongoDB database and a .env file with some environment variables used by the program.
- **tests**: Test suite of the app. It includes a data folder with mocked data and several files testing every different module of the app.
- docker-compose.yaml: Docker-compose file that can be used to launch a mongodb and mongo-express instance. 
- main.py: Main entrypoint of the program.
- requirements.txt: Python requirements of the program.

## How to run
In order to run the main script you need to have [Python](https://www.python.org/downloads/) installed on your system. The script was tested with versions 3.9, 3.10, and 3.11 of Python. After Python is installed and ready to be used, you need to install the project dependencies using the following command:
```sh
pip install -r requirements.txt
```

Once the dependencies are installed, you can run the main script with the command `python main.py`. It will print on the console the results of the operation, and store the results on a database. This program also receives the following optional arguments:
- Number of entries (-n, --num_entries): Number of new entries to be scraped and filtered from the site (default=30).
- Database (-db, --database): Database used to store the results. Available options are 'sqlite' and 'mongodb' (default=sqlite).

So, for example, if you want to scrape 50 entries and store the results on a MongoDB database you could run the command `python main.py -n 50 -db mongodb`.

> When using the default database option (sqlite) there is no need to run any additional software, but if the mongodb option is selected you need to have a MongoDB instance running in your computer and available on port 27017. A docker-compose.yml file is provided that runs a MongoDB instance with the user and database already setup. To run it you need to have Docker installed and execute the `docker-compose up` command.

## Running the tests
The test was implemented using [pytest](https://docs.pytest.org/en/8.2.x/). If you have the required dependencies installed you can run the test suite using the following command: `pytest tests`.