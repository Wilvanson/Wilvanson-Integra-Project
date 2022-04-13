from flask import Blueprint, jsonify, request
from data import dataBase
data_routes = Blueprint('data', __name__)


@data_routes.route('/')
def dataMine():
    data = dataBase()
    # print('\n \n Hey \n \n')
    
    return data

