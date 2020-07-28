# Gadget Backend

The Python REST backend project build in Docker.


## Running development server

The project requires Python 3.6.x or newer.

### Requirements

Make sure you install the dependencies using pip:

```bash
pip install -r requirements.txt
```

### Create development database

To create a development database containing test data run `create_test_db.sh`. This will crate a SQLite database file named `gadget.db` with test data in the root of the project.
If you want to create a DB without the test data run `create_test_db.sh --skip-data`


### Run the project

To run the project start `run_dev.sh`.


## Database migrations

This project uses [Alembic](https://alembic.sqlalchemy.org/) to handle database migrations.


### Creating a migration

If you need to create a new DB migration run the following command

```bash
$ alembic revision -m "<MESSAGE>"
```

### Applying migrations

To apply the migrations to your development database run

```bash
$ alembic upgrade head
```

For production you need to run the same command with the production flag

```bash
$ alembic --name production upgrade head
```
