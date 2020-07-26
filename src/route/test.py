from flask import Blueprint, jsonify
from flask_restful import Resource

test = Blueprint('test', __name__)

class Test(Resource):
  @test.route('/<id>', methods=['GET'])
  def get(id):
    return jsonify({
      'id': id,
      'name': 'test.name',
      'browser': 'test.browser',
      'size': 'test.size',
      'key': 'test.key',
      'state': 'test.state',
      'created': 'run.created',
      'run': 'test.run.id'
    })
