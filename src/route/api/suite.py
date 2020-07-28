from flask import Blueprint, jsonify
from flask_restful import Resource

suite = Blueprint('suite', __name__)


class Suite(Resource):
    @suite.route('/<id>', methods=['GET'])
    def get(id):
        return jsonify({
            'id': id,
            'name': 'suite.name',
            'created': 'suite.created',
            'updated': 'suite.updated',
            'slug': 'suite.slug',
            'project': 'suite.project.id'
        })
