from flask import Blueprint, jsonify, request
from flask_restful import Resource

from gadget import utils
from .model import Project

bp = Blueprint('project', __name__)


@bp.route('/', methods=['GET'])
def list():
    projects = utils.serialize_list(Project.query.all())
    return jsonify(projects)


@bp.route('/<id>', methods=['GET'])
def get(id):
    return jsonify(Project.query.get(id).serialize())


@bp.route('/<id>', methods=['POST'])
def save(id):
    project = Project.query.get(id)
    project.update(name=request.json['name'], slug=request.json['slug'])
    return ''


@bp.route('/', methods=['POST'])
def create():
    project = Project(name=request.json['name'], slug=request.json['slug'])
    project.create()
    return ''


@bp.route('/<id>', methods=['DELETE'])
def delete(id):
    project = Project.query.get(id)
    project.delete()
    # @todo remove suites
    return ''
