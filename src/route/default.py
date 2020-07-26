from flask import Blueprint, jsonify
from flask_restful import Resource
import config

default = Blueprint('default', __name__)

class Default(Resource):
  @default.route('/', methods=['GET'])
  def reportStatus():
    return jsonify({'api': 'Gadget', 'version': config.version })
