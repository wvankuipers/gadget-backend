import click

from os import path, remove
from flask import Blueprint, current_app

from gadget import db

from gadget.route.api.project.model import Project
from gadget.route.api.suite.model import Suite
from gadget.route.api.run.model import Run
from gadget.route.api.test.model import Test

bp = Blueprint('dev', __name__)


@bp.cli.command("create-db")
def create():
    current_app.config['DEBUG'] = True

    click.echo(f"Checking for existing database at {current_app.config['DATABASE_FILE']}")

    if path.exists(current_app.config['DATABASE_FILE']):
        click.confirm('The current database will be removed! Do you want to continue?', abort=True)
        remove(current_app.config['DATABASE_FILE'])

    db.create_all()

    click.echo('SQLIte database created!')

    if click.confirm('Do you want to insert the fixtures data set?'):
        project_fixtures = Project.fixtures()
        suite_fixtures = Suite.fixtures()
        run_fixtures = Run.fixtures()
        test_fixtures = Test.fixtures()

        db.session.bulk_save_objects(project_fixtures + suite_fixtures + run_fixtures + test_fixtures)
        db.session.commit()
