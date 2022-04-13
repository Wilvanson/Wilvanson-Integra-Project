from flask import Blueprint, jsonify, request

data_routes = Blueprint('data', __name__)


@data_routes.route('/')
def data():
    
    
    return {}