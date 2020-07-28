#!/usr/bin/python3

from flask import Flask, jsonify
from flask_restful import Api
from json import dumps
from flask_cors import CORS

from db import Database
from config import config

from route.default import default
from route.api.project import project
from route.api.suite import suite
from route.api.run import run
from route.api.test import test

app = Flask(__name__)

# DEV_MODE = os.getenv('DEV_MODE', False)

if config['App'].getboolean('DevMode') is True:
    CORS(app, resources={r'/*': {'origins': 'http://localhost:4200'}})

API_BASE = f"/api/v{config['Api']['Version']}"

app.register_blueprint(default)

app.register_blueprint(project, url_prefix=f"{API_BASE}/project")
app.register_blueprint(suite, url_prefix=f"{API_BASE}/suite")
app.register_blueprint(run, url_prefix=f"{API_BASE}/run")
app.register_blueprint(test, url_prefix=f"{API_BASE}/test")

if __name__ == '__main__':
    if config['App']['DevMode'] is True:
        print('\033[93mRunning in DEVELOPMENT mode!\033[0m')
        print(app.url_map)

    app.run(debug=config['App'].getboolean('DevMode'))
