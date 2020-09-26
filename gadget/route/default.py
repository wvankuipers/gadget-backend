from flask import Blueprint, jsonify, send_from_directory, current_app
from flask_restful import Resource

bp = Blueprint('default', __name__)


class Default(Resource):
    @bp.route('/<path:path>', methods=['GET'])
    def static_proxy(path):
        return send_from_directory('static/gadget/', path)

    @bp.errorhandler(404)
    @bp.route('/')
    def root(*args):
        return send_from_directory('static/gadget/', 'index.html')

    @bp.route('/version', methods=['GET'])
    def reportStatus():
        return jsonify({'api': 'Gadget', 'version': current_app.config['VERSION']})
