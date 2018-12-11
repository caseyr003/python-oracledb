# Python Oracle DB Template

This project is a flask api built with Python, Flask and Oracle Database to be used as a starter template.

## Built With

* [Python 3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Docker](https://www.docker.com/)
* [Oracle Database 18c](https://www.oracle.com/technetwork/database/enterprise-edition/downloads/index.html)

## Prerequisites

You will need the following things properly installed on your computer:

* [Git](http://git-scm.com/)
* [Docker](https://www.docker.com/)

## Installation

* run `git clone https://github.com/caseyr003/python-oracledb.git`

## Running

To run the project locally follow the following steps:

* change into the project directory
* `docker build -t python/oracledb18 .`
* `docker run -p 5000:5000 python/oracledb18`

## JSON API

The JSON API has sample endpoints to start development
Must configure `app.py` to connect to your Oracle DB and update the SQL query

* `http://localhost:5000/api/test`
(returns data from Oracle DB connection)
