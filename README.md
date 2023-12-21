### Hexlet tests and linter status:
[![Actions Status](https://github.com/Raphael703/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Raphael703/python-project-83/actions)
[![PyCI](https://github.com/Raphael703/python-project-83/actions/workflows/pyci.yml/badge.svg)](https://github.com/Raphael703/python-project-83/actions/workflows/pyci.yml)



_____

# Page Analyzer
Page Analyzer is a simple SEO utility tool designed to quickly analyze the on-page SEO elements of a given URL. 

With Page Analyzer, you can effortlessly add a webpage, and the tool will extract essential SEO elements such as h1, title, and meta description. This information can be valuable for tailoring your content to align with common search queries on the internet.




## Content
- [Used packages](#used-packages)
- [For Dev](#for-dev)
- [Author](#author)

## Requirements
- [Python 3.10+](https://www.python.org/downloads/release/python-3100/)
- [Poetry](https://python-poetry.org/)
- [Postgres](https://www.postgresql.org/)

## Used packages
 - [Flask](https://flask.palletsprojects.com/en/3.0.x/) 
 - [gunicorn](https://gunicorn.org/)
 - [psycopg2-binary](https://www.psycopg.org/docs/install.html)
 - [python-dotenv](https://github.com/theskumar/python-dotenv)
 - [validators](https://pypi.org/project/validators/)
 - [requests](https://pypi.org/project/requests/)
 - [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)




______
## For Dev
#### Clone this repository:
```sh
git clone https://github.com/Raphael703/python-project-83.git
```

#### Install dependencies
```sh
make install
```

#### Create .env file in sources root and fill it (example)
```dotenv
DATABASE_URL=postgresql://pguser:pgpass@localhost:5432/pgdb
SECRET_KEY=notsosecret
```

#### Up postgres DB (Docker for example):
```sh
docker run -d \
    --name dev_page_analyzer \
    -e POSTGRES_USER=pguser \
    -e POSTGRES_PASSWORD=pgpass \
    -e POSTGRES_DB=pgdb \
    -p 5432:5432 \
    postgres:latest
```

#### Run local server:
```shell
make dev
```

#### Run local linter
```sh
make lint
```


## Author
- [Rafael Mukhametshin](https://github.com/Raphael703)