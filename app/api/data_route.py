from flask import Blueprint, jsonify, request
from data import dataBase
data_routes = Blueprint('data', __name__)


@data_routes.route('/')
def dataMine():
    data = dataBase()
    
    return data

@data_routes.route('/medvCrim')
def dataMineCrim():
    data = dataBase()
    
    return {'data': data['ZYMEDVCRIM']}


@data_routes.route('/medvAge')
def dataMineAge():
    data = dataBase()
    
    return {'data': data['ZYMEDVAGE']}


@data_routes.route('/medvPtratio')
def dataMinePtr():
    data = dataBase()
    
    return {'data': data['ZYMEDVPTRATIO']}