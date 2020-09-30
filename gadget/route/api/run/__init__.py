from flask import Blueprint, jsonify, request
from flask_restful import Resource

from gadget import utils
from .model import Run

bp = Blueprint('run', __name__)


@bp.route('/', methods=['GET'])
def list():
    runs = utils.serialize_list(Run.query.all())
    return jsonify(runs)


@bp.route('/<id>', methods=['GET'])
def get(id):
    return jsonify(Run.query.get(id).serialize())


@bp.route('/<id>', methods=['POST'])
def save(id):
    run = Run.query.get(id)
    run.update(nr=request.json['nr'], suite_id=request.json['suite'])
    return ''


# @bp.route('/', methods=['POST'])
# def create():
#     run = Run(nr=request.json['nr'])
#     run.create()
#     return ''


@bp.route('/<id>', methods=['DELETE'])
def delete(id):
    run = Run.query.get(id)
    # @todo tests
    run.delete()
    return ''
