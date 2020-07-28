from flask import Blueprint, jsonify, request
from flask_restful import Resource
from db import Database

project = Blueprint('project', __name__)


class Project(Resource):
    @project.route('/', methods=['GET'])
    def list():
        return jsonify([{
            'id': '1',
            'name': 'project.name',
            'created': 'project.created',
            'updated': 'project.updated',
            'slug': 'project.slug',
            'suites': ['suite.id']
        }, {
            'id': '2',
            'name': 'project.name',
            'created': 'project.created',
            'updated': 'project.updated',
            'slug': 'project.slug',
            'suites': ['suite.id']
        }, {
            'id': '3',
            'name': 'project.name',
            'created': 'project.created',
            'updated': 'project.updated',
            'slug': 'project.slug',
            'suites': ['suite.id']
        }])

    @project.route('/<id>', methods=['GET'])
    def get(id):
        return jsonify({
            'id': id,
            'name': 'project.name',
            'created': 'project.created',
            'updated': 'project.updated',
            'slug': 'project.slug',
            'suites': ['suite.id']
        })

    @project.route('/<id>', methods=['POST'])
    def save(id):
        return ''

    @project.route('/', methods=['POST'])
    def create():
        print(request.json)
        Database().write(
                         "INSERT INTO project(name, slug) VALUES ('%s', '%s')"
                         % (request.json['name'], request.json['slug'])
        )
        return ''

    @project.route('/<id>', methods=['DELETE'])
    def delete(id):
        return ''
