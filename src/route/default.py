from flask import Blueprint, jsonify, send_from_directory
from flask_restful import Resource
import config

default = Blueprint('default', __name__)


class Default(Resource):
    @default.route('/<path:path>', methods=['GET'])
    def static_proxy(path):
        return send_from_directory('static/gadget/', path)

    @default.errorhandler(404)
    @default.route('/')
    def root(*args):
        return send_from_directory('static/gadget/', 'index.html')

    @default.route('/version', methods=['GET'])
    def reportStatus():
        return jsonify({'api': 'Gadget', 'version': config['Version']})
