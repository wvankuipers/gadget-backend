from flask import Blueprint, jsonify
from flask_restful import Resource

run = Blueprint('run', __name__)

class Run(Resource):
  @run.route('/<id>', methods=['GET'])
  def get(id):
    return jsonify({
      'id': id,
      'nr': 'run.nr',
      'created': 'run.created',
      'updated': 'run.updated',
      'suite': 'run.suite.id',
      'tests': ['run.test.id']
    })
