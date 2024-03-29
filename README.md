[![Coverage Status](https://coveralls.io/repos/github/wvankuipers/gadget-backend/badge.svg)](https://coveralls.io/github/wvankuipers/gadget-backend)
[![Build Status](https://travis-ci.org/wvankuipers/gadget-backend.svg?branch=master)](https://travis-ci.org/wvankuipers/gadget-backend)
[![Known Vulnerabilities](https://snyk.io/test/github/wvankuipers/gadget-backend/badge.svg)](https://snyk.io/test/github/wvankuipers/gadget-backend)

# Gadget Backend

The Python REST backend project build in Docker.
It is build using the [Flask](https://palletsprojects.com/p/flask/) framework.

## Contributing

If you want to contribute to the project please read our [code of conduct](.github/CODE_OF_CONDUCT.md) and [contributing guidelines](.github/CONTRIBUTING.md).

## Running development server

The project requires Python 3.6.x or newer.

### Requirements

Make sure you install the dependencies using pip:

```bash
virtualenv gadget
pip install -r requirements.txt
pip install -e .
```

### Create development database

To (re)create a developer/test DB in SQLite run

```bash
flask dev create-db
```

During this process you will be asked to remove the current database and fill the database with sample data.

### Run the project

To run the project in development mode run:

```bash
./run_dev.sh
```

### Run tests

To run the tests using Pytest run:

```bash
pytest tests/
```

## Database migrations

This project uses [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) to handle database migrations.


### Creating a migration

If you need to create a new DB migration run the following command:

```bash
flask db migrate -m "<message>"
```

### Applying migrations

To apply the migrations to your development database run:

```bash
flask db upgrade
```
