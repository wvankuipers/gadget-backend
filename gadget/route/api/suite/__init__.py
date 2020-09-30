from flask import Blueprint, jsonify, request
from flask_restful import Resource

from gadget import utils
from .model import Suite

bp = Blueprint('suite', __name__)


@bp.route('/', methods=['GET'])
def list():
    suites = utils.serialize_list(Suite.query.all())
    return jsonify(suites)


@bp.route('/<id>', methods=['GET'])
def get(id):
    return jsonify(Suite.query.get(id).serialize())


@bp.route('/<id>', methods=['POST'])
def save(id):
    suite = Suite.query.get(id)
    suite.update(name=request.json['name'], slug=request.json['slug'], project_id=request.json['project'])
    return ''


@bp.route('/', methods=['POST'])
def create():
    suite = Suite(name=request.json['name'], slug=request.json['slug'])
    suite.create()
    return ''


@bp.route('/<id>', methods=['DELETE'])
def delete(id):
    suite = Suite.query.get(id)
    suite.delete()
    # @todo remove runs
    return ''
