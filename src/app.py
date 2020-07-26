#!/usr/bin/python3

from flask import Flask, jsonify
from flask_restful import Api
from json import dumps
from flask_cors import CORS

import config

from route.default import default
from route.project import project
from route.suite import suite
from route.run import run
from route.test import test

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': 'http://localhost:4200'}})

app.register_blueprint(default)
app.register_blueprint(project, url_prefix='/project')
app.register_blueprint(suite, url_prefix='/suite')
app.register_blueprint(run, url_prefix='/run')
app.register_blueprint(test, url_prefix='/test')

if __name__ == '__main__':
  if config.DEV_MODE:
    print('\033[93mRunning in DEVELOPMENT mode!\033[0m')
    print(app.url_map)

  app.run(debug = config.DEV_MODE)
