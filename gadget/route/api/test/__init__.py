from flask import Blueprint, jsonify, request
from flask_restful import Resource

from gadget import utils
from .model import Test

bp = Blueprint('test', __name__)


@bp.route('/', methods=['GET'])
def list():
    tests = utils.serialize_list(Test.query.all(), True)
    return jsonify(tests)


@bp.route('/<id>', methods=['GET'])
def get(id):
    return jsonify(Test.query.get(id).serialize())


# @bp.route('/<id>', methods=['POST'])
# def save(id):
#     test = Test.query.get(id)
#     test.update(name=request.json['name'], slug=request.json['slug'])
#     return ''


# @bp.route('/', methods=['POST'])
# def create():
#     test = Test(name=request.json['name'], slug=request.json['slug'])
#     test.create()
#     return ''


@bp.route('/<id>', methods=['DELETE'])
def delete(id):
    test = Test.query.get(id)
    test.delete()
    # @todo remove screenshots
    return ''
