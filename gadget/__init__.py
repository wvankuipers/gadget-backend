#!/usr/bin/python3

import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    database = os.path.join(app.instance_path, 'gadget.sqlite')
    app.config.from_mapping(
        VERSION='1.0.0',
        API_VERSION='1',
        SECRET_KEY='dev',
        DATABASE_FILE=database,
        SQLALCHEMY_DATABASE_URI=f'sqlite:////{database}',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if app.config['DEBUG'] is True:
        CORS(app, resources={r'/*': {'origins': 'http://localhost:4200'}})

    # Database set-up
    db.init_app(app)
    migrate.init_app(app, db)

    # CLI commands
    from gadget import cli
    cli.init(app)

    # Project routes
    from gadget import route
    route.init(app)

    if app.config['DEBUG'] is True:
        print('\033[93mRunning in DEVELOPMENT mode!\033[0m')
        print(app.url_map)

    return app
